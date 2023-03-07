import datetime
from marshmallow import Schema, fields

class WeightSchema(Schema):
    mass_kg = fields.Int(required = True)
    last_measured = fields.DateTime(required=True)

