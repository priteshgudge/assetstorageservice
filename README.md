# assetstorageservice
This service provides an interface to S3 for anonymous upload/download of assets.

## UnitTests
Setup Virual Env and Install requirements as given in Method 2 below:

python -m unittest /assetstorageservice/tests/test_asset_dao.py


## Steps to Run:
### Method 1
Use the provided docker compose file and run the command:

1. docker-compose -f app_compose.yml up

2. Use Postman Collection for APIs: https://www.getpostman.com/collections/29e71952fd3e4a434c46

3. For File Upload: curl -v -XPUT -T /path/to/file 'https://url-provided-by-post'


### Method 2
1. Clone the repository: https://github.com/priteshgudge/assetstorageservice.git and install/run mongo 3.6
 
2. Setup Virtual Environment: $virtualenv python3asststr -p python3.4 $source python3asststr/bin/activate

3. Install Requirements File: pip install -r requirements.txt

4. Change Directory to go to project folder

5. Run Below Export Command:

$export AWS_ACCESS_KEY_ID="<AWS_ACCESS_KEY_ID>";export AWS_SECRET_ACCESS_KEY="<AWS_SECRET_ACCESS_KEY>";export PYTHONPATH=$PWD

6. Run service app: $python assetstorageservice/conf/service_app.py

7. Use the PostMan Collections to hit the APIs: 

Postman Collection:
https://www.getpostman.com/collections/29e71952fd3e4a434c46 

8. Use the sample Curl command to Upload the file: curl -v -XPUT -T /path/to/sample_file.txt 'https://s3urlprovidedbyservice' 

Eg. curl -v -XPUT -T /tmp/go-code-check 'https://s3urlprovidedbyservice'

### References:
https://medium.com/backticks-tildes/restful-api-design-put-vs-patch-4a061aa3ed0b
