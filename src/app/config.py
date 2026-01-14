from dotenv import load_dotenv
import os

load_dotenv()

rabbitmq_user = os.getenv('RABBITMQ_USER', 'guest')
rabbitmq_password = os.getenv('RABBITMQ_PASSWORD', 'guest')
rabbitmq_host = os.getenv('RABBITMQ_HOST', '127.0.0.1')
rabbitmq_port = os.getenv('RABBITMQ_PORT', '5672')
rabbitmq_vhost = os.getenv('RABBITMQ_VHOST', '/')

broker = f'amqp://{rabbitmq_user}:{rabbitmq_password}@rabbitmq:{rabbitmq_port}{rabbitmq_vhost}'

postgres_user = os.getenv('PG_USER')
postgres_password = os.getenv('PG_PASSWORD')
postgres_host = os.getenv('PG_HOST', 'localhost')
postgres_port = os.getenv('PG_PORT', '5432')
postgres_db = os.getenv('PG_DB')

backend = f'db+postgresql://{postgres_user}:{postgres_password}@db:{postgres_port}/{postgres_db}'

DB_CONFIG = {
    "host": os.getenv("PG_HOST", "db"),
    "port": int(os.getenv("PG_PORT", 5432)),
    "dbname": os.getenv("PG_DB"),
    "user": os.getenv("PG_USER"),
    "password": os.getenv("PG_PASSWORD"),
}
