# import numpy as np

# def output_fn(prediction, content_type):
#     # prediction is usually array([29.], dtype=float32)
#     if isinstance(prediction, (list, tuple, np.ndarray)):
#         pred = prediction[0]
#     else:
#         pred = prediction

#     return str(int(round(float(pred))))
import os
import xgboost as xgb
import numpy as np

# This will hold the loaded model
model = None

def model_fn(model_dir):
    """
    Load the XGBoost model from the model_dir.
    SageMaker calls this once at container startup.
    """
    global model
    model_path = os.path.join(model_dir, "xgboost-model")
    booster = xgb.Booster()
    booster.load_model(model_path)
    model = booster
    return model

def predict_fn(input_data, model):
    """
    Apply the model to the input data.
    input_data is already deserialized (DMatrix if using CSVSerializer)
    """
    return model.predict(input_data)

def output_fn(prediction, content_type):
    """
    Format the prediction for the client.
    Converts float to integer class label string.
    """
    pred = prediction[0] if hasattr(prediction, "__getitem__") else prediction
    result = str(int(round(float(pred))))
    return result, "text/csv"
