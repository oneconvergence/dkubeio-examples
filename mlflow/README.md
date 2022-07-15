Example taken from https://github.com/mlflow/mlflow/tree/master/examples/tensorflow/tf2

### Setup
1. Create a code with url- https://github.com/rahul-179/dkubeio-examples/tree/mlflow/mlflow branch -mlflow
2. Create an output model 

### Traning from VS code
1. Create a vs code IDE with tensorflow 2.6.0 cpu image
2. cd to the code directory where we have the requirements.txt file
3. pip3 install virtualenv
4. export PATH=$PATH:$HOME/.local/bin
5. export MLFLOW_TRACKING_INSECURE_TLS="true"
6. export MLFLOW_TRACKING_URI="<https://<ip>:32222>"
7. export MLFLOW_TRACKING_TOKEN="<Token>" 
8. virtualenv -p python3 env
9. . env/bin/activate
10. pip3 install -r requirements.txt
11. python train_predict.py

## Building Image outside dkube
1. Download the model to local directory
```
mlflow artifacts  download -r <run-id> -d <local-path>
eg: mlflow artifacts  download -r c263bdaa-9505-4dd5-81fa-f9dbf40190fc -d ./output
```
2. Update the conda.yaml file in the downloaded path and add protobuf==3.19.4 in pip dependenicies
3. Run the below command to build the image
```
mlflow models build-docker -n <image-name> -m <local-path>/decision-tree-classifier
eg: mlflow models build-docker -n lucifer001/mlflow-sklearn-demo:demo1 -m output/decision-tree-classifier
```
4.Push the image

### Deployment
1. Select serving image which was build in the previous step.
2. Serving Port: 8000
3. Serving Url Prefix: /invocations
4. Min CPU/Max CPU: 1
5. Min Memory/Max Memory: 5G

### Prediction
1. Copy the curl command from the deployment page
2. Change the data section to
-d '{
    "columns": ["SepalLength", "SepalWidth", "PetalLength", "PetalWidth"],
    "data": [[5.1, 3.3, 1.7, 0.5], [5.9, 3.0, 4.2, 1.5], [6.9, 3.1, 5.4, 2.1]]
}'
