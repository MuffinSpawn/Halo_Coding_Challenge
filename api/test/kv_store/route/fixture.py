import os
import tempfile

import pytest

from kv_store.app import create_app
from kv_store.model.value import Base


@pytest.fixture
def client():
    db_file,db_path = tempfile.mkstemp(suffix='.db')
    app = create_app(config=dict(TESTING=True), db_path=db_path)

    Base.metadata.create_all(app.config['db'])

    yield app.test_client()

    os.close(db_file)
    os.unlink(db_path)


    # db_fd, flaskr.app.config['DATABASE'] = tempfile.mkstemp()
    # flaskr.app.config['TESTING'] = True

    # with flaskr.app.test_client() as client:
    #     with flaskr.app.app_context():
    #         flaskr.init_db()
    #     yield client

    # os.close(db_fd)
    # os.unlink(flaskr.app.config['DATABASE'])

