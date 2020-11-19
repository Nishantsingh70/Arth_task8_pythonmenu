import os

while True:

    print("\n")
    os.system("tput setaf 1")
    print("\t\t\t\t\t\t\tWELCOME TO DOCKER MENU")
    print("\t\t\t\t\t\t\t----------------------")
    os.system("tput setaf 7")
    print("""
                                                    Press 1. For installing docker
                                                    Press 2. For checking docker is installed
                                                    Press 3. To start docker service
                                                    Press 4. To see the downloaded docker images
                                                    Press 5. For download any docker image
                                                    Press 6. To launch container
                                                    Press 7. To see total running docker container
                                                    Press 8. To stop the container
                                                    Press 9. To delete any docker image
                                                    Press 10. To configure web server in container
                                                    Press 11. To exit from docker operations
    """)
    print("\n")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        os.system("sudo yum install docker-ce --nobest")
        print()

    elif ch == 2:
        os.system("sudo rpm -qa | grep docker")
        print()

    elif ch == 3:
        os.system("sudo systemctl start docker")
        os.system("sudo systemctl enable docker")
        os.system("sudo systemctl status docker")
        print()
            
    elif ch == 4:
        os.system("sudo docker images")
        print()

    elif ch == 5:
        print("Enter image name :")
        img_name = input()
        os.system("sudo docker pull {}".format(img_name))
        print()

    elif ch == 6:
        os_name = input("Enter container name :")
        img_name = input("Enter image name :")
        os.system("sudo docker run -dit --name {} {}".format(os_name,img_name))
        print()

    elif ch == 7:
        os.system("sudo docker ps")

    elif ch == 8:
         os_name = input("Enter container name :")
         os.system("sudo docker stop {}".format(os_name))
         print()

    elif ch == 9:
         img_name = input("Enter image name :")
         os.system("sudp docker rmi {}".format(img_name))
         print()
               
    elif ch == 10:
         os.system("sudo yum install httpd")
         os.system("sudo systemctl start httpd")
         print()

    elif ch == 11:
         os.system("exit")
         break
    
    else:
         print("Invalid choice")
    input("Enter to run more docker menu...")
    os.system("clear")


