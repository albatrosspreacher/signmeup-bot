import logging, boto3, os
from dotenv import load_dotenv
from botocore.exceptions import ClientError

load_dotenv()

client = boto3.client(
    's3',
    region_name=os.getenv('REGION'),
    aws_access_key_id=os.getenv('ACCESS_KEY'),
    aws_secret_access_key=os.getenv('SECRET_KEY')
)
    
# Creating the high level object oriented interface
resource = boto3.resource(
    's3',
    region_name=os.getenv('REGION'),
    aws_access_key_id=os.getenv('ACCESS_KEY'),
    aws_secret_access_key=os.getenv('SECRET_KEY')
)

def upload_file(file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # get server id and use that as file name
    if object_name is None:
        object_name = os.path.basename(file_name)

    try:
        response = client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True


def create_presigned_url(bucket_name, object_name, expiration=3600):
    """Generate a presigned URL to share an S3 object

    :param bucket_name: string
    :param object_name: string
    :param expiration: Time in seconds for the presigned URL to remain valid
    :return: Presigned URL as string. If error, returns None.
    """

    # Generate a presigned URL for the S3 object
    try:
        response = client.generate_presigned_url('get_object',
                                                    Params={'Bucket': bucket_name,
                                                            'Key': object_name},
                                                    ExpiresIn=expiration)
        print(response)
    except ClientError as e:
        logging.error(e)
        return None

    # The response contains the presigned URL
    return response

# upload_file("index.html", os.getenv('BUCKET_NAME'))
# create_presigned_url(os.getenv('BUCKET_NAME'), "index.html")