Example taken from https://github.com/mlflow/mlflow/tree/master/examples/tensorflow/tf2

### Setup
1. Create a code with url- https://github.com/oneconvergence/dkubeio-examples/tree/mlflow/mlflow branch -mlflow
2. Create an output model 

### Traning
1. wget https://repo.anaconda.com/miniconda/Miniconda3-py37_4.12.0-Linux-x86_64.sh
2. bash Miniconda3-py37_4.12.0-Linux-x86_64.sh
3. source ~/miniconda3/etc/profile.d/conda.sh
4. conda env create -f conda.yaml
5. conda activate tensorflow-example
6. python train_predict.py --code {code name} --output {output model name}

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
