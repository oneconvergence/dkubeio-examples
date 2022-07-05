from prediction import TreeModel
from dkube.sdk import mlflow as m
import argparse
import sys

#max_depths = [5, 8, 10]
max_depths = [5]

parser = argparse.ArgumentParser()
parser.add_argument("--code", required=True, help="input code name")
parser.add_argument("--dataset", help="input dataset name")
parser.add_argument("--output", required=True, help="output model name")

if __name__ == '__main__':
    args = parser.parse_args(sys.argv[1:])
    for n in max_depths:
        params = {"max_depth": n, "random_state": 42}
        dtc = TreeModel.create_instance(**params)
        run_id = m.create_run(code=args.code, output=args.output)
        exp_id, run_id = dtc.mlflow_run(run_id)
        print(f"MLflow Run completed with run_id {run_id} and experiment_id {exp_id}")
        print("<->" * 40)
