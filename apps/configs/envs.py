from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_HOST = os.getenv('DATABASE_HOST')
DATABASE_NAME = os.getenv('DATABASE_NAME')
DATABASE_PORT = os.getenv('DATABASE_PORT')
DATABASE_USERNAME = os.getenv('DATABASE_USERNAME')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')

INPUT_PATH = os.getenv('INPUT_PATH')
OUTPUT_PATH = os.getenv('OUTPUT_PATH')

REDDIT_SECRET_KEY = os.getenv('REDDIT_SECRET_KEY')
REDDIT_CLIENT_ID = os.getenv('REDDIT_CLIENT_ID')

AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_REGION = os.getenv('AWS_REGION')
AWS_BUCKET_NAME = os.getenv('AWS_BUCKET_NAME')

BATCH_SIZE = os.getenv('BATCH_SIZE')
ERROR_HANDLING = os.getenv('ERROR_HANDLING')
LOG_LEVEL = os.getenv('LOG_LEVEL')
