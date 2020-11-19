import os

while True:
    print("\n") 
    os.system("tput setaf 1")
    print("\t\t\t\t\t\t\tWELCOME TO HADOOP MENU")
    print("\t\t\t\t\t\t\t----------------------")
    os.system("tput setaf 7")
    print("""
                                                    Press 1: To configure and start namenode of Hadoop
                                                    Press 2: To configure and start datanode of Hadoop
                                                    Press 3: To configure client
                                                    Press 4: To stop namenode
                                                    Press 5: To start namenode which is already configured
                                                    Press 6: To stop datanode
                                                    Press 7: To start datanode which is already configured
                                                    Press 8: To see the report
                                                    Press 9: To copy any file from the client
                                                    Press 10: To read any file from the client
                                                    Press 11: To exit
    """)
    print("\n")
    opt = int(input("Enter your choice :"))
    if opt == 1:
        print("clear")
        remote_ip = input("Enter the ip of the system which you want to setup as namenode :")
        print("\t\n Software should be present under / directory")
        os.system("ssh -l root {} rpm -ivh /jdk-8u171-linux-x64.rpm".format(remote_ip))
        os.system("ssh -l root {} rpm -ivh /hadoop-1.2.1-1.x86_64.rpm --force".format(remote_ip))

        
        #Configuring core-site.xml file 

        os.system("ssh -l root {} \"cd /etc/hadoop ;echo \<configuration\> >> core-site.xml\"".format(remote_ip))
    
        os.system("ssh -l root {} \"cd /etc/hadoop ;echo \<property\> >> core-site.xml\"".format(remote_ip))
    
    
        os.system("ssh -l root {} \"cd /etc/hadoop ;echo \<name\>fs.default.name\<\/name\> >> core-site.xml\"".format(remote_ip))
    

        os.system("ssh -l root {} \"cd /etc/hadoop ;echo \<value\>hdfs://0.0.0.0:9001\<\/value\> >> core-site.xml\"".format(remote_ip))
    
        os.system("ssh -l root {} \"cd /etc/hadoop ;echo \<\/property\> >> core-site.xml\"".format(remote_ip))
    
        os.system("ssh -l root {} \"cd /etc/hadoop ;echo \<\/configuration\> >> core-site.xml\"".format(remote_ip))
    
        #configuring hdfs-site.xml file
    
    
        os.system("ssh -l root {} \"cd /etc/hadoop ;echo \<configuration\> >> hdfs-site.xml\"".format(remote_ip))
    
        os.system("ssh -l root {} \"cd /etc/hadoop ;echo \<property\> >> hdfs-site.xml\"".format(remote_ip))
    
    
        os.system("ssh -l root {} \"cd /etc/hadoop ;echo \<name\>dfs.name.dir\<\/name\> >> hdfs-site.xml\"".format(remote_ip))
    
        dir = input("Enter the name of the directory you want to create for the name node ")
        os.system("ssh -l root {} mkdir /{}".format(remote_ip,dir) )
       
        os.system("ssh -l root {} \"cd /etc/hadoop ;echo \<value\>/{}\<\/value\> >> hdfs-site.xml\"".format(remote_ip,dir))
    
        os.system("ssh -l root {} \"cd /etc/hadoop ;echo \<\/property\> >> hdfs-site.xml\"".format(remote_ip))
    
        os.system("ssh -l root {} \"cd /etc/hadoop ;echo \<\/configuration\> >> hdfs-site.xml\"".format(remote_ip))
    
        #starting the namenode 
              
        os.system("ssh -l root {} hadoop namenode -format ".format(remote_ip))
    
        os.system("ssh -l root {} hadoop-daemon.sh start namenode ".format(remote_ip))

    elif opt==2:
        print("clear")
        remote_ip = input("Enter the ip of the system which you want to setup as namenode :")
        print("\t\n Software should be present under / directory")
        os.system("ssh -l root {} rpm -ivh /jdk-8u171-linux-x64.rpm".format(remote_ip))
        os.system("ssh -l root {} rpm -ivh /hadoop-1.2.1-1.x86_64.rpm --force".format(remote_ip))

        
        #configure hdfs-site.xml file

        os.system("ssh -l root {} \"cd /etc/hadoop ;echo \<configuration\> >> hdfs-site.xml\"".format(remote_ip))
    
        os.system("ssh -l root {} \"cd /etc/hadoop ;echo \<property\> >> hdfs-site.xml\"".format(remote_ip))
    
    
        os.system("ssh -l root {} \"cd /etc/hadoop ;echo \<name\>dfs.data.dir\<\/name\> >> hdfs-site.xml\"".format(remote_ip))
    
        dir = input("Enter the name of the directory you want to create for the name node ")
        os.system("ssh -l root {} mkdir /{}".format(remote_ip,dir) )

        
        os.system("ssh -l root {} \"cd /etc/hadoop ;echo \<value\>/{}\<\/value\> >> hdfs-site.xml\"".format(remote_ip,dir))
    
        os.system("ssh -l root {} \"cd /etc/hadoop ;echo \<\/property\> >> hdfs-site.xml\"".format(remote_ip))
    
        os.system("ssh -l root {} \"cd /etc/hadoop ;echo \<\/configuration\> >> hdfs-site.xml\"".format(remote_ip))


        #configure core-site.xml file

        os.system("ssh -l root {} \"cd /etc/hadoop ;echo \<configuration\> >> core-site.xml\"".format(remote_ip))
    
        os.system("ssh -l root {} \"cd /etc/hadoop ;echo \<property\> >> core-site.xml\"".format(remote_ip))
    
    
        os.system("ssh -l root {} \"cd /etc/hadoop ;echo \<name\>fs.default.name\<\/name\> >> core-site.xml\"".format(remote_ip))
    
        n_ip = input("Enter the namenode ip:")
    
     

        os.system("ssh -l root {} \"cd /etc/hadoop ;echo \<value\>hdfs://{}:9001\<\/value\> >> core-site.xml\"".format(remote_ip,n_ip))
    
        os.system("ssh -l root {} \"cd /etc/hadoop ;echo \<\/property\> >> core-site.xml\"".format(remote_ip))
    
        os.system("ssh -l root {} \"cd /etc/hadoop ;echo \<\/configuration\> >> core-site.xml\"".format(remote_ip))
        
        os.system("systemctl stop firewalld;setenforce 0;hadoop-daemon.sh start datanode")
        print("\t\t\t------------------DataNode started----------------\t\t\t")


    elif opt==3:
        print("clear")
        remote_ip=input("Enter the ip of the system which you want to setup as client")
        print("\t\t \n\n Software should be present under / directory")
        os.system("shh -l root {} rpm -ivh /jdk-8u171-linux-x64.rpm".format(remote_ip))
        os.system("ssh -l root {} rpm -ivh /hadoop-1.2.1.-1.x86_64.rpm --force".format(remote_ip))
        
        #configure core-site.xml file

        os.system("ssh -l root {} \"cd /etc/hadoop ;echo \<configuration\> >> core-site.xml\"".format(remote_ip))
    
        os.system("ssh -l root {} \"cd /etc/hadoop ;echo \<property\> >> core-site.xml\"".format(remote_ip))
    
    
        os.system("ssh -l root {} \"cd /etc/hadoop ;echo \<name\>fs.default.name\<\/name\> >> core-site.xml\"".format(remote_ip))
    

        os.system("ssh -l root {} \"cd /etc/hadoop ;echo \<value\>hdfs://0.0.0.0:9001\<\/value\> >> core-site.xml\"".format(remote_ip))
    
        os.system("ssh -l root {} \"cd /etc/hadoop ;echo \<\/property\> >> core-site.xml\"".format(remote_ip))
    
        os.system("ssh -l root {} \"cd /etc/hadoop ;echo \<\/configuration\> >> core-site.xml\"".format(remote_ip))
        os.system("clear")


    elif opt==4:
        remote_ip=input("Enter the namenode ip which you want to stop :")
        os.system("ssh -l root {} hadoop-daemon.sh stop namenode".format(remote_ip))
        os.system("clear")

    elif opt==5:
        remote_ip=input("Enter the namenode ip which you want to stop :")
        os.system("ssh -l root {} hadoop-daemon.sh start namenode".format(remote_ip))
        os.system("clear")


    elif opt==6:
        remote_ip=input("Enter the datanode ip which you want to stop :")
        os.system("ssh -l root {} hadoop-daemon.sh stop datanode".format(remote_ip))
        os.system("clear")
    
    elif opt==7:
        remote_ip=input("Enter the namenode ip which you want to stop :")
        os.system("ssh -l root {} hadoop-daemon.sh start datanode".format(remote_ip))
        os.system("clear")
          
    elif opt==8:
        remote_ip=input("Enter the ip whose report you want to see :")
        os.system("ssh -l root {} hadoop dfsadmin -report".format(remote_ip))


    elif opt==9:
        file_name=input("Enter the filename which you want to put in datanode")
        remote_ip=input("Enter the client ip :")
        os.system("ssh -l root {} hadoop fs -put {} /".format(remote_ip,filename))
        os.system("clear")

    elif opt==10:
        file_name=input("Enter the filename which you want to read from datanode")
        remote_ip=input("Enter the client ip :")
        os.system("ssh -l root {} hadoop fs -cat {} /".format(remote_ip,filename))
        os.system("clear")


    elif opt==11:
        os.system("exit")
        break


    else:
        print("Invalid Option")
    input("Enter to run more hadoop menu")
    os.system("clear")
