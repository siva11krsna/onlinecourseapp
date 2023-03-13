from flask import jsonify, make_response
from marshmallow import ValidationError

def validate_request(input_request, input_schema):

    try:
        input_schema.load(input_request.json)

    except ValidationError as err:
        print('validation error', err.messages_dict)
        return make_response(jsonify(err.messages), 400)
    return True


def merge_request_with_model(model_entity, input_request, input_schema, id):

    input_object = input_schema.load(input_request.json)
    model_object = input_schema.dump(model_entity)

    for key, value in input_request.json.items():
        print(key, value)

    for key, value in model_object.items():
        print(key, value)



