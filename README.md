# assetstorageservice

## Steps to Run:
1. Clone the repository: https://github.com/priteshgudge/assetstorageservice.git
 
2. Setup Virtual Environment: $virtualenv python3asststr -p python3.4 $source python3asststr/bin/activate

3. Install Requirements File: pip install -r requirements.txt

4. Change Directory to go to project folder

5. Run Below Export Command:

$export AWS_ACCESS_KEY_ID="<AWS_ACCESS_KEY_ID>";export AWS_SECRET_ACCESS_KEY="<AWS_SECRET_ACCESS_KEY>";export PYTHONPATH=$PWD

6. Run service app: $python assetstorageservice/conf/service_app.py

7. Use the PostMan Collections to hit the APIs: 

Postman Collection:
https://www.getpostman.com/collections/29e71952fd3e4a434c46 

8. Use the sample Curl command to Upload the file: curl -v -XPUT -T /path/to/sample_file.txt 'https://priteshassetstemp.s3.amazonaws.com/a3e6cabb-f068-4272-9876-aa3a2687682a?AWSAccessKeyId=AKIAJ-------------------------------------w%3D' 

Eg. curl -v -XPUT -T /tmp/go-code-check 'https://priteshassetstemp.s3.amazonaws.com/b3618bae-a159-4766-8d1e-b862f5993a60?AWSAccessKeyId=AKIAJUZP62CNW6RDUIWQ&Expires=1533346979&Signature=6NKEVHYgIPk%2F3vKmHDq%2BWAxXJKE%3D'

## UnitTests
python -m unittest /home/pritesh/codes/assignment/assetstorageservice/assetstorageservice/tests/test_asset_dao.py
