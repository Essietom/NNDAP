from cron_validator import CronValidator
from marshmallow import ValidationError


def validate_cron(cron: str):
    try:
        CronValidator.parse(cron)
        return 'cron schedule is incorrect, should follow this format'
    except ValueError as e:
        print(f"Could not parse cron `{cron}`")
        raise ValidationError(f"{cron} is not a valid cron expression")

