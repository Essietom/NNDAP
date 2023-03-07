import datetime
from marshmallow import Schema, fields, validate, ValidationError
from farm_api.helper import validate_cron

class FeedingSchema(Schema):
    amount_kg = fields.Int(required=True)
    cron_schedule = fields.String(required=True, validate = validate_cron)    # cron_schedule: fields.String(required=True, validate = validate.Regexp('^$|https://facebook.com/[a-zA-Z][a-zA-Z 0-9._]{0,50}$', 0,'Feeding cron schedule is incorrect, should follow this format'))
    last_measured = fields.DateTime(required=True)
