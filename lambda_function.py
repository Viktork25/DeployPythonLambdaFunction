import boto3
from s3utils import S3utils

s3utils = S3utils(
AWS_ACCESS_KEY_ID = 'Your_Access_Key',
AWS_SECRET_ACCESS_KEY = 'Your_Secret_Key',
AWS_STORAGE_BUCKET_NAME = 'Your_Bucket',
S3UTILS_DEBUG_LEVEL = 1,  #change it to 0 for less verbose
)
folders = s3utils.ls("Your Folder that you want to check the files")
lst=len(folders)
lst=lst-1
print(lst)

region = 'Your Region'

# Enter your instances here: ex. ['X-XXXXXXXX', 'X-XXXXXXXX']

def lambda_handler(event, context):
	instances = ['Your Instance_Id']
	ec2 = boto3.client('ec2', region_name=region)
	if lst > 2: #Check if the files or folders inside you folder are more than 2, if it is more then Instance Starting(otherwise is stopping the python script)
   		ec2.start_instances(InstanceIds=instances)
		print 'started your instances: ' + str(instances)
	else:
   		print "Instances will not start"
   		exit()
