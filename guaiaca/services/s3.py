import logging
import boto3
from botocore.exceptions import ClientError

from guaiaca.config import VERIFY, REGION, BUCKET_NAME


def create_bucket(bucket_name, region=None):
    """Create an S3 bucket in a specified region

    If a region is not specified, the bucket is created in the S3 default
    region (us-east-1).

    :param bucket_name: Bucket to create
    :param region: String region to create bucket in, e.g., 'us-west-2'
    :return: True if bucket created, else False
    """

    # Create bucket
    try:
        if region is None:
            s3_client = boto3.client('s3', verify=VERIFY)
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            s3_client = boto3.client('s3', verify=VERIFY, region_name=REGION)
            location = {'LocationConstraint': region}
            s3_client.create_bucket(Bucket=bucket_name,
                                    CreateBucketConfiguration=location)
    except ClientError as e:
        logging.error(e)
        return False
    return True


def list_files():
    s3 = boto3.resource('s3', verify=VERIFY)
    my_bucket = s3.Bucket(BUCKET_NAME)

    for object_summary in my_bucket.objects.filter(Prefix=""):
        print(object_summary.key)


def upload_file(file_name, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = file_name

    # Upload the file
    s3_client = boto3.client('s3', verify=VERIFY)
    try:
        response = s3_client.upload_file(file_name, BUCKET_NAME, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True


def download_file(file_name):
    s3 = boto3.client('s3', verify=VERIFY)
    s3.download_file(BUCKET_NAME, file_name, file_name)
