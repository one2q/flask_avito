import os

# basedir = os.path.abspath(os.path.dirname(__file__))
# os.environ['DATABASE_URL']

class Config:
	SQLALCHEMY_DATABASE_URI = 'sqlite:///avito.db'
	# SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:root@localhost:5432/postgres'
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	SQLALCHEMY_ECHO = True
	DEBUG = True
	RESTX_JSON = {'ensure_ascii': False, 'indent': 4}
