from sqlalchemy import create_engine

from kv_store.model.value import Base


def main(**kwargs):
	engine = create_engine('sqlite:///{}'.format(kwargs['db_path']))

	Base.metadata.create_all(engine)


if __name__ == '__main__':
	main(db_path='kv_store.db')
