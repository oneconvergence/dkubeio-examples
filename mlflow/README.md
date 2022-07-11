Example taken from https://github.com/mlflow/mlflow/tree/master/examples/tensorflow/tf2

### Setup
1. Create a code with url- https://github.com/rahul-179/dkubeio-examples/tree/mlflow/mlflow branch `rm-mlflow`
2. Create an output model 

### Traning
1. Create a vs code IDE with tensorflow 2.6.0 cpu image
2. cd to the code directory where we have the requirements.txt file
3. pip3 install virtualenv
4. export PATH=$PATH:$HOME/.local/bin
5. virtualenv -p python3 env
6. . env/bin/activate
7. pip3 install -r requirements.txt
8. python train_predict.py --code {code name} --output {output model name}

### Building Image
1. Go to the model details page which was given as output in the above training run. A new version will be there in the version list.
2. Click on the build model image icon which is on the version's row at the right.
3. Select code
4. Select registry
5. Submit to create image build

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

