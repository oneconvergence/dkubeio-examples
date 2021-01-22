## Arvados S3 Example

1. Dataset
-  Name : Arv-s3
-  Versioning: None 
-  Dataset Source: S3, Don’t check the AWS checkbox.
-  Endpoint: https://download.ce8i5.arvadosapi.com 
-  Access Key ID: 3dnjzwsn4y8mhg03u0mdpucp2jrdcwlskvpmrd1ytdvfippou8
-  Secret Access Key: 3dnjzwsn4y8mhg03u0mdpucp2jrdcwlskvpmrd1ytdvfippou8
-  Bucket: ce8i5-4zz18-j45o88d58u7js60

## Note: Dataset link https://dev.arvados.org/issues/16668#note-6

2: Project:
-  Name: Arv-s3
-  Git URL: https://github.com/oneconvergence/dkubeio-examples/tree/master/arv-examples 
-  Branch: arvados-s3

3: Launch Notebook
-  Project: Arv-s3
-  Dataset: Arv-s3
-  Mount point: /opt/dkube/input
-  When the status is running, open the notebook and in the notebook open terminal and run the following commands in sequence. 
-  pip3 install boto3 --user
-  python work/workspace/arv-examples/arvados-s3-test.py
-  Open work/workspace/arv-examples and run the notebook arvados-s3-test.ipynb. 

