from flask import request
from flask_restx import Resource,Namespace
from model import AdvertSchema, AdvertSchemaExtend
from crud import get_all, create_advert, get_by_id
from setup_db import db

advert_ns = Namespace('advert')


@advert_ns.route('/')
class AdvertsView(Resource):
	def get(self):
		filters = {
			"price": request.args.get("price"),
			"page": request.args.get("page"),
			"created_at": request.args.get("created_at"),
		}

		try:
			adverts = get_all(db.session, filters)
			return AdvertSchema(many=True).dump(adverts)
		except Exception as e:
			print(e)

	def post(self):
		data = request.json
		try:
			advert = create_advert(db.session, data)
			return advert.id, 200
		except Exception as e:
			print(e)


@advert_ns.route('/<int:pk>')
class AdvertView(Resource):
	def get(self, pk):
		fields = request.args.get("fields")
		try:
			print(fields)
			advert = get_by_id(db.session, pk)
			if fields:
				return AdvertSchemaExtend().dump(advert)
			return AdvertSchema().dump(advert)
		except Exception as e:
			print(e)
