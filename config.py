class Config:
	SQLALCHEMY_DATABASE_URI = 'sqlite:///avito.db'
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	SQLALCHEMY_ECHO = True
	DEBUG = True
	RESTX_JSON = {'ensure_ascii': False, 'indent': 4}