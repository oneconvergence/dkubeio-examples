Example taken from https://github.com/mlflow/mlflow/tree/master/examples/pytorch/torchscript/IrisClassification

### Setup
1. Create a code with url- https://github.com/rahul-179/dkubeio-examples/tree/mlflow/mlflow branch `rm-mlflow`
2. Create an output model 

### Traning
1. Create a vs code IDE with pytorch 1.6 cpu image
2. cd to the code directory where we have the conda.yaml file
3. conda env create -f conda.yaml
4. conda activate pytorch-example
5. python iris_classification.py

## Building Image outside dkube
1. Download the model to local directory
```
mlflow artifacts  download -r <run-id> -d <local-path>
eg: mlflow artifacts  download -r c263bdaa-9505-4dd5-81fa-f9dbf40190fc -d ./output
```
2. Update the conda.yaml file in the downloaded path and add protobuf==3.19.4 in pip dependenicies
3. Run the below command to build the image
```
mlflow models build-docker -n <image-name> -m <path to the directory conatining MLModel file>
eg: mlflow models build-docker -n lucifer001/mlflow-pytorch-demo:demo1 -m output/model
```
4.Push the image

### Deployment
1. Select serving image which was build in the previous step.
2. Serving Port: 8000
3. Serving Url Prefix: /invocations
4. Min CPU/Max CPU: 1
5. Min Memory/Max Memory: 5G

### Prediction
1. Copy the curl command from the deployment page and append --insecure
2. Change the data section to
--data-raw '{ "instances": [4.4, 3, 1.3, 0.2] }'
