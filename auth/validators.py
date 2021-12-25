import json
from json import dumps, loads
from flask import Flask, jsonify, request
from marshmallow import Schema, fields, ValidationError
from flask import request

class UserSchema(Schema):
    username = fields.String(required=True)
    email = fields.String(required=True)
    password = fields.String(required=True)

def validate_schema(schema):
    def decorator(func):
        def inner(*args, **kwargs):
            try:
                data = schema.load(data=json.loads(request.data))
            except ValidationError as err:
                return jsonify(err.messages), 400
            return func(**data)
        return inner
    return decorator


