import random
import time
import pandas as pd
from app.app import app

CSV_PATH = '/app/data/inference_data.csv'

def load_transactions_from_csv():
    """
    Worker. Send transactions data from CSV file
    """
    df = pd.read_csv(CSV_PATH)

    for index, row in df.iterrows():
        data_dict = row[df.columns].to_dict()

        data_dict = {k.lower(): float(v) for k, v in data_dict.items()}
        app.send_task(
            'run_fraud_inference',
            kwargs=data_dict,
            countdown=1
        )

        time.sleep(random.uniform(0.1, 1.5))

if __name__ == "__main__":
    load_transactions_from_csv()
