Example taken from https://github.com/mlflow/mlflow/tree/master/examples/tensorflow/tf2

### Setup
1. Create a code with url- https://github.com/oneconvergence/dkubeio-examples/tree/mlflow/mlflow branch -mlflow
2. Create an output model 

### Training with Conda environment
1. Create a vs code IDE with tensorflow 2.6.0 cpu image
2. cd to the code directory where we have the conda.yaml file
3. conda env create -f conda.yaml
4. conda activate tensorflow-example
5. python train_predict.py --code {code name} --output {output model name}

### Training from VS code inside DKube
1. Create a vs code IDE with tensorflow 2.6.0 cpu image
2. cd to the code directory where we have the requirements.txt file
3. sudo apt-get update -y; sudo apt-get install -y make build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev \
libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev python-openssl
4. curl https://pyenv.run | bash
5. exec "$SHELL"
6. export PATH=$HOME/.pyenv/bin:$PATH
7. pyenv install 3.7.2
8. pyenv virtualenv 3.7.2 env
9. source $HOME/.pyenv/versions/env/bin/activate
10. pip install --upgrade pip
11. pip install -r requirements.txt
12. export MLFLOW_TRACKING_INSECURE_TLS="true"
13. export MLFLOW_TRACKING_URI="<https://<ip>:32222>"
14. export MLFLOW_TRACKING_TOKEN="<Token>" 
15. python train_predict.py

### Traning from VS code outside DKube
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
    
`Note: Python 3.7 or higher version is required`

### Building Image inside DKube
1. Go to the model details page which was given as output in the above training run. A new version will be there in the version list.
2. Click on the build model image icon which is on the version's row at the right.
3. Select code
4. Select registry
5. Submit to create image build
    
### Building Image outside DKube
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
