import boto3
from assetstorageservice.constants import s3_constants
import os

# Reference
# https://stackoverflow.com/questions/10044151/how-to-generate-a-temporary-url-to-upload-file-to-amazon-s3-with-boto-library

class S3Client():
    def get_s3_client(self):
        AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY_ID")
        AWS_SECRET_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
        return boto3.client('s3',s3_constants.REGION,aws_access_key_id=AWS_ACCESS_KEY,aws_secret_access_key=AWS_SECRET_KEY)

    def generate_presigned_put_url(self,object_key):
        s3_client = self.get_s3_client()
        presigned_url = s3_client.generate_presigned_url('put_object', Params={'Bucket': s3_constants.S3_BUCKET, 'Key': object_key},
                                  ExpiresIn=3600, HttpMethod='PUT')

        return presigned_url

    def generate_presigned_get_url(self,object_key,timeout=3600):
        s3_client = self.get_s3_client()
        presigned_url = s3_client.generate_presigned_url('get_object', Params={'Bucket': s3_constants.S3_BUCKET, 'Key': object_key},
                                                         ExpiresIn=timeout, HttpMethod='GET')

        return presigned_url