from celery import Celery
from app.config import broker, backend

app = Celery('run_fraud_inference',
             broker=broker,
             backend=backend,
             include=['worker.tasks']
             )

app.conf.update(
    task_serializer='json',
    accept_content=['json'],
    result_serializer='json',
    timezone='Europe/Moscow',
    enable_utc=True,
    task_track_started=True,
    result_persistent=True,
    worker_prefetch_multiplier=1,
)