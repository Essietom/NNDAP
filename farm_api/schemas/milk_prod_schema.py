from farm_api.helper import validate_cron
from marshmallow import Schema, fields

class MilkProductionSchema(Schema):
    last_milk = fields.DateTime()
    cron_schedule = fields.String(required=True, validate = validate_cron)    
    amount_l = fields.Int()



