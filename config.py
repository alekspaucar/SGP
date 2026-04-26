import os
from dotenv import load_dotenv
load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY', 'dev')
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///sgp.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
DEBUG = True