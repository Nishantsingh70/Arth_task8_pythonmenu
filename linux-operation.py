import os

while True:  

    print("\n")
    os.system("tput setaf 1")
    print("\t\t\t\t\t\t\tWELCOME TO LINUX MENU")
    print("\t\t\t\t\t\t\t---------------------")
    os.system("tput setaf 7")
    print("""
                                                    Press 1. To see date
                                                    Press 2. To see calendar
                                                    Press 3. To run calculator
                                                    Press 4. Create User
                                                    Press 5. Create Directory
                                                    Press 6. See the RAM Usage
                                                    Press 7. See the CPU Information
                                                    Press 8. Check the IP address
                                                    Press 9. Create file
                                                    Press 10. To scan ip using nmap
                                                    Press 11. To go out from linux operations
    """)
    print("\n")

    ch = input("Enter your choice:")
    if ch == "1":
        os.system("date")
        print()

    elif ch == "2":
        os.system("cal")
        print()

    elif ch == "3":
        os.system("bc")
        print()

    elif ch == "4":
        print("Enter user name :",end ='')
        u_name = input()
        os.system("useradd {}".format(create_user))
        print()

    elif ch == "5":
        print("Enter directory name :",end ='')
        d_name = input()
        os.system("mkdir {}".format(d_name))
        print()

    elif ch == "6":
        os.system("free -m")

    elif ch == "7":
        os.system("lscpu")

    elif ch == "8":
        os.system("ifconfig")

    elif ch == "9":
        print("Enter file name :",end = '')
        f_name = input("Enter the file name")
        location = input("Enter the location :")
        os.system("touch {}/{}".format(location,f_name))
        print()
  
    elif ch == "10":
        print("Enter IP :",end = '')
        ip = input()
        os.system("ping {}".format(ip))
        print()

    elif ch == "11":
        os.system("exit")
        break
       
    else:
        print("Invalid Choice")
    input("Enter to run more linux menu...")
    os.system("clear")

