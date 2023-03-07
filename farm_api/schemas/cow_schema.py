from farm_api.models.cow import Cow
import json
import datetime
from marshmallow import Schema, fields, validate, ValidationError
from farm_api.schemas.feeding_schema import FeedingSchema
from farm_api.schemas.milk_prod_schema import MilkProductionSchema
from farm_api.schemas.weight_schema import WeightSchema
import typing


class CowSchema(Schema):
    """
    Schema used for loading/dumping Cows
    """
    cow_id = fields.Int(strict=True)
    name = fields.Str(required=True)
    sex = fields.Str(required=True, validate=validate.OneOf(("male","female","MALE", "FEMALE"), error="sex can either be: male or female"))
    birthdate = fields.DateTime()
    condition = fields.Str(required=True, validate=validate.OneOf(("healthy","unhealthy","HEALTHY", "UNHEALTHY"), error="condition can either be: healthy or unhealthy"))
    weight  = fields.Nested(WeightSchema)
    feeding = fields.Nested(FeedingSchema)
    milk_production = fields.Nested(MilkProductionSchema)
    has_calves = fields.Boolean()
