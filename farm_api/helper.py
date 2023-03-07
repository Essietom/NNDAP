from cron_validator import CronValidator
from marshmallow import ValidationError


def validate_cron(cron: str):
    try:
        CronValidator.parse(cron)
        return 'cron schedule is incorrect, should follow this format'
    except ValueError as e:
        print(f"Could not parse cron `{cron}`")
        raise ValidationError(f"{cron} is not a valid cron expression")


# def cow_to_schema(self, cow:Cow) -> CowSchema:
#     new_cow = CowSchema()
#     new_cow.cow_id = cow.cow_id
#     new_cow.birthdate = cow.birthdate
#     new_cow.name = cow.name
#     new_cow.has_calves = cow.has_calves
#     new_cow.condition = cow.condition
#     new_cow.sex = cow.sex


#     weight = WeightSchema()
#     weight.cron_schedule = cow.weight_last_measured
#     weight.last_measured = cow.weight_mass_kg

#     feeding = FeedingSchema()
#     feeding.cron_schedule = cow.feeding_cron_schedule
#     feeding.last_measured = cow.feeding_last_measured
#     feeding.amount_kg = cow.feeding_amount_kg

#     milk_production = MilkProductionSchema()
#     milk_production.amount_l = cow.milk_prod_amount_l
#     milk_production.last_milk = cow.milk_prod_last_milk
#     milk_production.cron_schedule = cow.milk_prod_cron_schedule

#     new_cow.feeding = feeding
#     new_cow.milk_production = milk_production
#     new_cow.weight = weight

#     return new_cow

# def schema_to_cow(self, data: dict) -> Cow:
#     self.validate(data)
    
#     new_cow = Cow()
#     new_cow.birthdate = schema. data['birthdate']
#     new_cow.name = data['name']
#     new_cow.has_calves = data['has_calves']
#     new_cow.condition = data['condition']
#     new_cow.sex = data['sex']
#     new_cow.milk_prod_amount_l = data['milk_production']['amount_l']
#     new_cow.milk_prod_last_milk = data['milk_production']['last_milk']
#     new_cow.milk_prod_cron_schedule = data['milk_production']['cron_schedule']
#     new_cow.weight_last_measured = data['weight']['last_measured']
#     new_cow.weight_mass_kg = data['weight']['mass_kg']
#     new_cow.feeding_cron_schedule = data['feeding']['cron_schedule']
#     new_cow.feeding_last_measured = data['feeding']['last_measured']
#     new_cow.feeding_amount_kg = data['feeding']['amount_kg']
#     return new_cow