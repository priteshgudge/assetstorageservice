# assetstorageservice

Steps to Run:
1. Clone the repository: https://github.com/priteshgudge/assetstorageservice.git
 
2. Setup Virtual Environment: $virtualenv python3asststr -p python3.4 $source python3asststr/bin/activate

3. Install Requirements File: pip install -r requirements.txt

4. Go to project directory: Run Below Export Command:
$export AWS_ACCESS_KEY_ID="<AWS_ACCESS_KEY_ID>";export AWS_SECRET_ACCESS_KEY="<AWS_SECRET_ACCESS_KEY>";export PYTHONPATH=$PWD

5. python assetstorageservice/conf/service_app.py

6. Use the PostMan Collections to hit the APIs

7. Use the sample python script provided for S3 upload.

Postman Collection:

https://www.getpostman.com/collections/29e71952fd3e4a434c46 
