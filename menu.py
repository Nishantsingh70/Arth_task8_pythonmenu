import os
import getpass

password = getpass.getpass("Password : ")
if password != "menu":
    print("Wrong Password")
    exit()
else:
    print("\t\t\twelcome to my menu !!")
    while True:
         print("""

                     Press 1 : To run Linux Operations
                     Press 2 : To run Docker Opearations
                     Press 3 : To AWS Opearations
                     Press 4 : To hadoop Operations
                     Press 5 : To exit
         """)

         ch = int(input("Enter your choice :"))
         if ch==1:
             os.system("python3 linux-operation.py")

         elif ch==2:
             os.system("python3 docker.py")

         elif ch==3:
             os.system("python3 aws-operation.py")

         elif ch==4:
             os.system("python3 hadoop.py")

         elif ch==5:
             os.system("exit")
             break

         else:
             print("Invalid Option")
         
         








