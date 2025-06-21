from app import create_app
from  app.constants.config import env
import os
from flask_cors import CORS

app = create_app()

frontend_url = os.getenv('APP_FRONTEND_URL')

CORS(app, resources={r"/api/*": {"origins": frontend_url }})

if __name__ == '__main__':
    app.run(debug=env == 'development')
