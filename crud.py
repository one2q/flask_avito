from constants import ITEMS_PER_PAGE
from model import Advert, AdvertSchema
from setup_db import db


def get_by_id(session: db.session, pk):
	return session.query(Advert).get(pk)


def get_all(session: db.session, filters):

	price = filters['price']
	created_at = filters['created_at']
	print(price, created_at)
	page = int(filters['page'])
	offset = (page - 1) * ITEMS_PER_PAGE

	order_by_price = None
	order_by_created = None

	if price == 'asc':
		order_by_price = Advert.price
	if price == 'desc':
		order_by_price = Advert.price.desc()
	if created_at == 'asc':
		order_by_created = Advert.created
	if created_at == 'desc':
		order_by_created = Advert.created.desc()

	return session.query(Advert).order_by(order_by_price, order_by_created).offset(offset).limit(ITEMS_PER_PAGE).all()


def create_advert(session: db.session, data) -> AdvertSchema:
	advert = Advert(**data)
	session.add(advert)
	session.commit()
	return advert
