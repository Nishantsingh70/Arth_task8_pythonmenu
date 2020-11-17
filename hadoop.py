import os

print("""
                    Press 1: To configure and start namenode of Hadoop
                    Press 2: To configure and start datanode of Hadoop
                    Press 3: To configure client
                    Press 4: To stop namenode
                    Press 5: To stop datanode
                    Press 6: To see the report
                    Press 7: To copy any file from the client
                    Press 8: To read any file from the client
""")

while True:
    opt = int(input("Enter your choice :"))
    
    if opt == 1:
        print("clear")
        remote_ip = input("Enter the ip of the system which you want to setup as namenode")
        print("\t\t \n\n Software should be present under / directory")
        os.system("shh -l root {} rpm -ivh /jdk-8u171-linux-x64.rpm".format(remote_ip))
        os.system("ssh -l root {} rpm -ivh /hadoop-1.2.1.-1.x86_64.rpm --force".format(remote_ip))

        os.system("rm /etc/hadoop/hdfs-site.xml;rm /etc/hadoop/core-site.xml")
        d_port=int(input("Enter the port :"))
        d_folder=input("Enter the directory :")
        
        #configure hdfs-site.xml file

        datafile=open("/etc/hadoop/hdfs-site.xml","w")
        datafile.write(f'''<?xml version="1.0"?>
        <?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

        <!-- Put site-specific property overrides in this file. -->

        <configuration>
        <property>
        <name>dfs.name.dir</name>
        <value>/{d_folder}</value>
        </property>
        </configuration>''')
        datafile.close()

        #configure core-site.xml file

        datafile1=open("/etc/hadoop/core-site.xml","w")
        datafile1.write(f'''<?xml version="1.0"?>
        <?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

        <!-- Put site-specific property overrides in this file. -->

        <configuration>
        <property>
        <name>fs.default.name</name>
        <value>hdfs://{remote_ip}:{d_port}</value>
        </property>
        </configuration>''')

        datafile1.close()
        os.system("hadoop namenode -format;systemctl stop firewalld;setenforce 0;hadoop-daemon.sh start namenode")
        print("\t\t\t------------------NameNode started----------------\t\t\t")

    elif opt==2:    
        print("clear")
        remote_ip=input("Enter the ip of the system which you want to setup as datanode :")
        print("\t\t \n\n Software should be present under / directory")
        os.system("shh -l root {} rpm -ivh /jdk-8u171-linux-x64.rpm".format(remote_ip))
        os.system("ssh -l root {} rpm -ivh /hadoop-1.2.1.-1.x86_64.rpm --force".format(remote_ip))
        
        os.system("rm /etc/hadoop/hdfs-site.xml;rm /etc/hadoop/core-site.xml")
        d_port=int(input("Enter the port :"))
        d_folder=input("Enter the directory :")
        
        #configure hdfs-site.xml file

        datafile=open("/etc/hadoop/hdfs-site.xmk","w")
        datafile.write(f'''<?xml version="1.0"?>
        <?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

        <!-- Put site-specific property overrides in this file. -->

        <configuration>
        <property>
        <name>dfs.data.dir</name>
        <value>/{d_folder}</value>
        </property>
        </configuration>''')
        datafile.close()

        #configure core-site.xml file

        datafile1=open("/etc/hadoop/core-site.xml","w")
        datafile1.write(f'''<?xml version="1.0"?>
        <?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

        <!-- Put site-specific property overrides in this file. -->

        <configuration>
        <property>
        <name>fs.default.name</name>
        <value>hdfs://{remote_ip}:{d_port}</value>
        </property>
        </configuration>''')

        datafile1.close()
        os.system("systemctl stop firewalld;setenforce 0;hadoop-daemon.sh start datanode")
        print("\t\t\t------------------DataNode started----------------\t\t\t")

    elif opt==3:
        print("clear")
        remote_ip=input("Enter the ip of the system which you want to setup as client")
        print("\t\t \n\n Software should be present under / directory")
        os.system("shh -l root {} rpm -ivh /jdk-8u171-linux-x64.rpm".format(remote_ip))
        os.system("ssh -l root {} rpm -ivh /hadoop-1.2.1.-1.x86_64.rpm --force".format(remote_ip))

        os.system("rm /etc/hadoop/hdfs-site.xml;rm /etc/hadoop/core-site.xml")
        d_port=int(input("Enter the port :"))
        
        #configure core-site.xml file

        datafile=open("/etc/hadoop/core-site.xml","w")
        datafile.write(f'''<?xml version="1.0"?>
        <?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

        <!-- Put site-specific property overrides in this file. -->

        <configuration>
        <property>
        <name>fs.default.name</name>
        <value>hdfs://{remote_ip}:{d_port}</value>
        </property>
        </configuration>''')

        datafile.close()
        os.system("clear")

    elif opt==4:
        remote_ip=input("Enter the namenode ip which you want to stop :")
        os.system("ssh -l root -o PasswordAuthentication=yes {} hadoop-daemon.sh stop namenode".format(remote_ip))
        os.system("clear")

    elif opt==5:
        remote_ip=input("Enter the datanode ip which you want to stop :")
        os.system("ssh -l root -o PasswordAuthentication=yes {} hadoop-daemon.sh stop datanode".format(remote_ip))
        os.system("clear")
          
    elif opt==6:
        remote_ip=input("Enter the ip whose report you want to see :")
        os.system("ssh -l root -o PasswordAuthentication=yes {} hadoop dfsadmin -format".format(remote_ip))
        os.system("clear")

    elif opt==7:
        file_name=input("Enter the filename which you want to put in datanode")
        remote_ip=input("Enter the client ip :")
        os.system("ssh -l root -o PasswordAuthentication=yes {} hadoop fs -put {} /".format(remote_ip,filename))
        os.system("clear")

    elif opt==8:
        file_name=input("Enter the filename which you want to read from datanode")
        remote_ip=input("Enter the client ip :")
        os.system("ssh -l root -o PasswordAuthentication=yes {} hadoop fs -cat {} /".format(remote_ip,filename))
        os.system("clear")

    elif opt==9:
        os.system("exit")
        break

    else:
        print("Invalid Option")

