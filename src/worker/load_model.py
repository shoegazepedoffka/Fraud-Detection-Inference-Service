import joblib

model_path = '/app/models/xgb_final.joblib'

def load_model():
    """
    Loads the XGBoost model
    """
    model = joblib.load(model_path)
    return model
