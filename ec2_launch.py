import sys
import boto3
import os
from secrets import access_key_id, secret_access_key

# ------------------------------------------------------------------------------
def main():
    ec2 = boto3.client("ec2",
                             'us-east-1',
                             aws_access_key_id=access_key_id,
                             aws_secret_access_key=secret_access_key)

    print(script_purpose())

    instance_type = prompt_user_for_instance_type()
    instance_name = prompt_user_for_instance_name()

    create_ec2_instance(ec2, instance_type, instance_name)

    sys.exit(0)
#------------------------------------------------------------------------------

def create_ec2_instance(ec2, instance_type, instance_name):
    conn = ec2.run_instances(InstanceType=instance_type,
                             MaxCount=1,
                             MinCount=1,
                             ImageId="ami-0cff7528ff583bf9a",
                             TagSpecifications=[
                                 {
                                     'ResourceType': 'instance',
                                     'Tags': [
                                         {
                                             'Key': 'Name',
                                             'Value': instance_name
                                         },
                                     ]
                                 },
                             ],
                             )
    print("\nEC2 creation response:\n")
    print(conn)
#------------------------------------------------------------------------------

def prompt_user_for_instance_type():

    print("\nEnter 'q' to quit.")

    instance_type = input("\nEnter the EC2 instance type you want to create: ")

    if not instance_type:
        sys.exit("No EC2 instance type entered by user. Exiting.")
    elif instance_type == 'q' or instance_type == 'Q':
        sys.exit(0)

    return instance_type

#------------------------------------------------------------------------------

def prompt_user_for_instance_name():

    instance_name = input("\nEnter the EC2 instance name: ")

    if not instance_name:
        sys.exit("No instance name entered by user. Exiting.")
    elif instance_name == 'q' or instance_name == 'Q':
        sys.exit(0)

    return instance_name

#------------------------------------------------------------------------------

def script_purpose():
    script_purpose = ("\n*************************************************************************************\n"
                  "***************************************************************************************\n"
                  "***                                                                                 ***\n"
                  "*** This script launches an Amazon EC2 instance using values passed by the user.    ***\n"
                  "***                                                                                 ***\n"
                  "***************************************************************************************\n"
                  "***************************************************************************************")

    return script_purpose

# ------------------------------------------------------------------------------
if __name__ == '__main__':
    main()