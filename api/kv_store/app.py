from flask import Flask
from sqlalchemy import create_engine

from kv_store.route import health_check, value


def create_app(config=None, db_path=None):
    app = Flask(__name__)
    if config:
        app.config.update(config)

    # app.config['db'] = Database(path=db_path)
    if not db_path:
        db_path = 'kv_store.db'
    app.config['db'] = create_engine('sqlite:///{}'.format(db_path))

    app.register_blueprint(health_check.blueprint, url_prefix='/api')
    app.register_blueprint(value.blueprint, url_prefix='/api')
    # print(app.url_map)

    return app
