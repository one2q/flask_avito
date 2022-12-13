from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_restx import Api

from config import Config
from setup_db import db
from view import advert_ns


def create_app(config: Config) -> Flask:
	application = Flask(__name__)
	application.config.from_object(config)
	register_extensions(application)
	return application


def register_extensions(app: Flask):
	db.init_app(app)
	app.app_context().push()
	api = Api(app, doc='/docs', title='API')
	api.add_namespace(advert_ns)


app = create_app(Config())
CORS(app)
migrate = Migrate(app, db, render_as_batch=True)

with app.app_context():
	db.create_all()

if __name__ == '__main__':
	app.run(port=5000)
