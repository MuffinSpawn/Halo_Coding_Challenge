from flask import current_app
from sqlalchemy.orm import sessionmaker

from kv_store.model.value import Value


class ValueController:
    def __init__(self):
        Session = sessionmaker(bind=current_app.config['db'])

        self._session = Session()

    def create(self, value):
        self._session.add(value)

        self._session.commit()

        return value

    def retrieve(self, key):
        value = None
        results = self._session.query(Value).filter_by(key=key)

        if results.count() == 1:
            value = results.first()

        return value

    def update(self, value):
        current_value = self.retrieve(value.key)

        current_value.value = value.value

        self._session.commit()

        return current_value

    def delete(self, value):
        self._session.delete(value)
