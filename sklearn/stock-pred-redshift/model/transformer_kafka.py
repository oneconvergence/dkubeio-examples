import json
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

DEFAULT_MODEL_NAME = "model"

parser = argparse.ArgumentParser(parents=[kfserving.kfserver.parser])
parser.add_argument('--model_name', default=DEFAULT_MODEL_NAME,
                    help='The name that the model is served under.')
parser.add_argument('--predictor_host', help='The URL for the model predict function', required=True)

args, _ = parser.parse_known_args()

from kafka import KafkaProducer
import json
import pandas as pd

class MessageProducer:
    broker = ""
    topic = ""
    producer = None

    def __init__(self, broker, topic):
        self.broker = broker
        self.topic = topic
        self.producer = KafkaProducer(bootstrap_servers=self.broker,
        value_serializer=lambda v: json.dumps(v).encode('utf-8'),
        acks='all',
        retries = 3)


    def send_msg(self, msg):
        print("sending message...")
        try:
            future = self.producer.send(self.topic,msg)
            self.producer.flush()
            future.get(timeout=60)
            print("message sent successfully...")
            return {'status_code':200, 'error':None}
        except Exception as ex:
            return ex



class Transformer(kfserving.KFModel):
    def __init__(self, name: str, predictor_host: str):
        super().__init__(name)
        self.predictor_host = predictor_host

    def preprocess(self, inputs: Dict) -> Dict:
        print(inputs)

        data = json.loads(inputs)
        dates = data['Date'].values()
        dates = [date.split('-')[0] for date in dates]
        l = len(dates)
        dates = np.asarray(dates).reshape(l,1)
        token = os.getenv("DKUBE_USER_ACCESS_TOKEN")
        payload = {"instances": dates.tolist() , "token": token}
        return payload
    
    def postprocess(self, predictions: List) -> List:
        preds = predictions["predictions"]
        l = len(preds)
        st = 'Stock values :->'
        for i in range(l):
            st += str(round(preds[i],3))
            if i != l-1:
                st += ',  '
        st += '.'

        broker = 'dkube-kafka-cp-kafka-headless.default.svc.cluster.local:9092'
        topic = 'kafkademo-result'
        message_producer = MessageProducer(broker,topic)

        data = {"result": st}
        resp = message_producer.send_msg(data)
        print(resp)

        return {"result": st}


if __name__ == "__main__":
    transformer = Transformer(args.model_name, predictor_host=args.predictor_host)
    kfserver = kfserving.KFServer()
    kfserver.start(models=[transformer])

