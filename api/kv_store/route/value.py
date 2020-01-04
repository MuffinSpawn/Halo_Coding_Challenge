from flask import current_app, blueprints, request, jsonify
from marshmallow import Schema, fields, post_load
from sqlalchemy.orm import sessionmaker

from kv_store.controller.value import ValueController
from kv_store.model.value import Value

blueprint = blueprints.Blueprint('value', __name__)


@blueprint.route('/value', methods=['POST'])
@blueprint.route('/value/<key>', methods=['PUT'])
def set(key=None):
    status_code = None
    controller = ValueController()
    schema = ValueAccessorSchema()
    value = schema.load(request.get_json())

    if key:
        value.key = key
        new_value = controller.update(value)
        status_code = 200
    else:
        new_value = controller.create(value)
        status_code = 201

    return schema.dump(new_value), status_code


@blueprint.route('/value/<key>', methods=['GET'])
def get(key):
    response = None
    status_code = 400
    controller = ValueController()
    schema = ValueAccessorSchema()

    value = controller.retrieve(key)
    if value:
        response = schema.dump(value)
        status_code = 200
    else:
        response = {'detail': f"A value for key '{key}' was not found."}
        status_code = 404

    return response, status_code


class ValueAccessorSchema(Schema):
    key = fields.String()
    value = fields.String(required=True)

    @post_load
    def create_value(self, data, **kwargs):
        return Value(**data)
