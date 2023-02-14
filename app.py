import os
from typing import Union, Tuple

from flask import request, jsonify, Response
from flask import Flask
from marshmallow import ValidationError

from make_query import build_query
from model import PackageRequestSchema

app = Flask(__name__)

# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# DATA_DIR = os.path.join(BASE_DIR, "data")
file_name = "data/apache_logs.txt"


@app.route("/perform_query", methods=['POST'])
def perform_query() -> Union[Response, Tuple[Response, int]]:
    query_data = request.json
    try:
        validated_data = PackageRequestSchema().load(query_data)

    except ValidationError as error:
        return jsonify(error.messages), 400

    result = None
    for query in validated_data['queries']:
        result = build_query(
            cmd=query['cmd'],
            value=query['value'],
            file_name=validated_data['file_name'],
            data=result
        )

    return jsonify(result)


if __name__ == '__main__':
    app.run(host="localhost", port=10001, debug=True)