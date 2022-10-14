import json
import csv
import numpy as np
import requests
import kfserving
import argparse
from typing import List, Dict
import logging
import io
import base64
import sys,json
import os
import pandas as pd
import boto3

DEFAULT_MODEL_NAME = "model"

parser = argparse.ArgumentParser(parents=[kfserving.kfserver.parser])
parser.add_argument('--model_name', default=DEFAULT_MODEL_NAME,
                    help='The name that the model is served under.')
parser.add_argument('--predictor_host', help='The URL for the model predict function', required=True)

args, _ = parser.parse_known_args()

filename = '/tmp/temp.csv'
img = ""

session = boto3.Session()
client = session.client('s3', endpoint_url='http://dkube-minio-server.dkube-infra.svc.cluster.local:9000', aws_access_key_id='dkube',
                        aws_secret_access_key='l06dands19s')

class Transformer(kfserving.KFModel):
    def __init__(self, name: str, predictor_host: str):
        super().__init__(name)
        self.predictor_host = predictor_host
        self._bucket = "default"
        self._key = "result"

    def preprocess(self, inputs: Dict) -> Dict:
        if inputs['EventName'] == 's3:ObjectCreated:Put':
            bucket = inputs['Records'][0]['s3']['bucket']['name']
            key = inputs['Records'][0]['s3']['object']['key']
            self._key = key
            self._bucket = bucket
            client.download_file(bucket, key, '/tmp/' + key)
            logging.info("Downloaded file from minio bucket")
        filename = "/tmp/" + key

        data = pd.read_csv(filename)
        dates = data['Date']
        dates = [date.split('-')[0] for date in dates]
        l = len(dates)
        dates = np.asarray(dates).reshape(l,1)
        token = os.getenv("DKUBE_USER_ACCESS_TOKEN")
        payload = {"instances": dates.tolist() , "token":token}
        return payload
    
    def postprocess(self, predictions: List) -> List:
        preds = predictions["predictions"]
        l = len(preds)
        for i in range(l):
            st += str(round(preds[i],3))
            if i != l-1:
                st += ',  '
        st += '.'
        client.upload_fileobj(io.BytesIO(st.encode("utf-8")), self._bucket, "result-"+self._key)
        return {"result": st}


if __name__ == "__main__":
    transformer = Transformer(args.model_name, predictor_host=args.predictor_host)
    kfserver = kfserving.KFServer()
    kfserver.start(models=[transformer])

