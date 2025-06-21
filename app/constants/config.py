import os
from dotenv import load_dotenv


load_dotenv(override=True)
openai_api_key = os.getenv('OPENAI_API_KEY')
db_url = os.getenv('DB_URL')
env = os.getenv('FLASK_ENV')