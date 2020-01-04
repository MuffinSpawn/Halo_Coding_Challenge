import os
import tempfile

import pytest

from kv_store import app

pytest_plugins = ['test.kv_store.route.fixture']


def test_health_check(client):
	response = client.get('/api/health_check')

	assert response.status_code == 200

