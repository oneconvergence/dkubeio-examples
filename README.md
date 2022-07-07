# dkubeio-examples
This example is a modified version of https://github.com/saurabh2mishra/mlflow-demo/tree/master/sklearn-demo
Modified to run and show MLflow and Dkube integration.

## Prediction
1. Copy the curl command from the deployment page
2. Change the data section to
-d '{"columns": ["mean radius", "mean texture", "mean perimeter", "mean area", "mean smoothness", "mean compactness", "mean concavity", "mean concave points", "mean symmetry", "mean fractal dimension", "radius error", "texture error", "perimeter error", "area error", "smoothness error", "compactness error", "concavity error", "concave points error", "symmetry error", "fractal dimension error", "worst radius", "worst texture", "worst perimeter", "worst area", "worst smoothness", "worst compactness", "worst concavity", "worst concave points", "worst symmetry", "worst fractal dimension"], "data": [[17.42, 25.56, 114.5, 948.0, 0.1006, 0.1146, 0.1682, 0.06597, 0.1308, 0.05866, 0.5296, 1.667, 3.767, 58.53, 0.03113, 0.08555, 0.1438, 0.03927, 0.02175, 0.01256, 18.07, 28.07, 120.4, 1021.0, 0.1243, 0.1793, 0.2803, 0.1099, 0.1603, 0.06818]]}'

