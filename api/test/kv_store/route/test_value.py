import json
import os
import tempfile

import pytest

from kv_store import app

pytest_plugins = ['test.kv_store.route.fixture']


def test_response_contains_correct_value_after_set(client):
	value = dict(key='foo', value='bar')
	print(f"Value: {value}")
	response = client.post('/api/value', json=value)

	assert response.status_code == 201
	assert response.json['key'] == value['key']
	assert response.json['value'] == value['value']

