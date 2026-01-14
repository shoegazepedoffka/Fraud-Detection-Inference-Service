from app.app import app
from worker.load_model import load_model
from worker.transform import insert_transaction
import numpy as np
import pandas as pd

model = load_model()

@app.task(name='run_fraud_inference')
def run_fraud_inference(**data_dict):
    """
    Celery task: makes a prediction for a single transaction

    Kwargs:
        data_dict: dictionary of features
    """
    try:
        df = pd.DataFrame([data_dict])
        features = df.values

        X = np.array(features).reshape(1, -1)

        prediction = model.predict(X)[0]
        probability = model.predict_proba(X)[0][1]

        enriched_data = data_dict.copy()
        enriched_data['is_fraud'] = bool(prediction)

        transaction_id = insert_transaction(enriched_data)
        result = {
            'transaction_id': transaction_id,
            'is_fraud': bool(prediction),
            'fraud_probability': float(probability)
        }


        return result

    except Exception as e:
        raise run_fraud_inference.retry(exc=e, countdown=60, max_retries=3)

