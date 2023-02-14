from marshmallow import Schema, fields, validate, validates_schema

valid_commands = ("filter", "map", "unique", "sort", "limit", "regex")


class RequestSchema(Schema):

    cmd = fields.Str(required=True, validate=validate.OneOf(valid_commands))
    value = fields.Str(required=True)


class PackageRequestSchema(Schema):
    queries = fields.Nested(RequestSchema, many=True)
    file_name = fields.Str(required=True)
