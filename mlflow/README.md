Example taken from https://github.com/mlflow/mlflow/tree/master/examples/tensorflow/tf2

### Traning
1. wget https://repo.anaconda.com/miniconda/Miniconda3-py37_4.12.0-Linux-x86_64.sh
2. bash Miniconda3-py37_4.12.0-Linux-x86_64.sh
3. export PATH=/home/ocdkube/miniconda3/bin/:$PATH
4. source ~/miniconda3/etc/profile.d/conda.sh
5. conda env create -f conda.yaml
6. conda activate tensorflow-example
7. python train_predict.py

### Deployment
1. Serving Port: 8000
2. Serving Url Prefix: /invocations
3. Min CPU/Max CPU: 1
4. Min Memory/Max Memory: 5G
