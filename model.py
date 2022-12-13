from sqlalchemy import Column, Integer, String, DateTime, Float, func
from marshmallow import Schema, fields

from setup_db import db


class Advert(db.Model):
	__tablename__ = 'advert'

	id = Column(Integer, primary_key=True, autoincrement=True)
	name = Column(String(200), nullable=False)
	price = Column(Float, nullable=False)
	main_photo = Column(String, nullable=False)
	describe = Column(String(1000))
	photos = Column(String)
	created = Column(DateTime, nullable=False, default=func.now())
	updated = Column(DateTime, default=func.now(), onupdate=func.now())


class AdvertSchema(Schema):
	id = fields.Int()
	name = fields.Str()
	price = fields.Float()
	main_photo = fields.Str()


class AdvertSchemaExtend(AdvertSchema):
	describe = fields.Str()
	photos = fields.Str()