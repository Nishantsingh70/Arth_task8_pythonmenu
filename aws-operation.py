import os

print("""
                    Press 1. To create key pair
                    Press 2. To create security group
                    Press 3. To launch an instance
                    Press 4. To create S3 bucket
                    Press 5. To delete key pair
                    Press 6. To delete S3 bucket
                    Press 7. To start an instance
                    Press 8. To stop an instance
                    Press 9. To attach extra volume to the instance
                    Press 10. To exit from the AWS operations
""")

while True:
    
    ch = int(input("Enter your choice :"))
    if ch==1:
       key_name = input("Enter key name :")
       os.system("aws ec2 create-key-pair  --key-name {}".format(key_name))
       print()

    elif ch==2:
       desc = input("Enter the description :")
       group_name = input("Enter a group name :")
       os.system("aws ec2 create-security-group --group-name {}  --description {}".format(group_name,desc))
       print()

    elif ch==3:
       img_name = input("Enter your image:")
       i_type = input("Enter instance type :")
       key_name = input("Enter your key pair :")
       sg_group = input("Enter Security group id :")
       sub = input("Enter subnet-id :")
       os.system("aws ec2 run-instances --image-id {} --instance-type {} --key-name {} --security-group-ids {} --subnet-id {} --count 1 ".format(img_name,i_type,key_name,sg_group,sub))
       print()

    elif ch==4:
       buc_name = input("Unique bucket name :")
       ac_list = input("Unique Access Control List :")
       reg = input("Region for the bucket to be deployed :")
       os.system("aws s3api create-bucket --bucket {} --acl {} --create-bucket-configuration LocationConstraint={} ".format(buc_name,ac_list,reg))       
    elif ch==5:
       key_name = input("Name of the key-pair which you want to delete :")
       os.system("aws ec2 delete-key-pair --key-name {} ".format(key_name))
       print()

    elif ch==6:
       buc_name = input("Unique bucket name which you want to delete :")
       os.system("aws s3api delete-bucket --bucket {}".format(buc_name))
       print()

    elif ch==7:
       ins_id = input("Enter instance id which you want to start :")
       os.system("aws ec2 start-instances --instance-ids {}".format(ins_id))
       print()

    elif ch==8:
       ins_id = input("Enter instance id which you want to stop :")
       os.system("aws ec2 stop-instances --instance-ids {}".format(ins_id))
       print()

    elif ch==9:
       vol_name = input("Enter the device name of the volume which you want to attach ex. /dev/sdh :")
       ins_id = input("Enter your instance id :")
       vol_id = input("Enter volume id :")
       os.system("aws ec2 attach-volume --device {} --instance-id {} --volume-id {}".format(vol_name,ins_id,vol_id))
       print()

    elif ch==10:
       os.system("exit")
       break

    else:
       print("Invalid option")
