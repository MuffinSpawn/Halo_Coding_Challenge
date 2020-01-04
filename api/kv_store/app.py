from flask import Flask

# from family_tree.database import Database
from kv_store.views import health_check


def create_app(config=None, db_path=None):
    app = Flask(__name__)
    if config:
        app.config.update(config)

    # app.config['db'] = Database(path=db_path)

    app.register_blueprint(health_check.blueprint, url_prefix='/api')
    # print(app.url_map)

    return app
