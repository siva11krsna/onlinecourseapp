from flask import jsonify, make_response
from marshmallow import ValidationError

def validate_and_merge(input_request, input_schema, current_model, id):

    current_object = input_schema.dump(current_model)
    print(current_object)

    try:
        model_data = input_schema.load(input_request.json)

    except ValidationError as err:
        print('validation error', err.messages_dict)
        return make_response(jsonify(err.messages), 400)

