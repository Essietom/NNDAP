from farm_api.database import db


class Cow(db.Model):
    """
    Cow Flask-SQLAlchemy Model

    Represents objects contained in the cows table
    """

    __tablename__ = "cows"

    cow_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(), nullable=False)
    sex = db.Column(db.String(), nullable=False)
    birthdate = db.Column(db.String(), nullable=False)
    condition = db.Column(db.String(), nullable=False)
    weight_mass_kg = db.Column(db.Integer, nullable=False)
    weight_last_measured = db.Column(db.String(), nullable=False)
    feeding_amount_kg = db.Column(db.Integer, nullable=False)
    feeding_cron_schedule = db.Column(db.String(), nullable=False)
    feeding_last_measured = db.Column(db.String(), nullable=False)
    milk_prod_last_milk = db.Column(db.String(), nullable=False)
    milk_prod_cron_schedule = db.Column(db.String(), nullable=False)
    milk_prod_amount_l = db.Column(db.Integer, nullable=False)
    has_calves = db.Column(db.Boolean, nullable=False)

    # @property
    # def weight(self):
    #     return {'mass_kg': self.weight_mass_kg, 'last_measured': self.weight_last_measured}

    # @property
    # def feeding(self):
    #     return {'amount_kg': self.feeding_amount_kg, 'cron_schedule': self.feeding_cron_schedule, 'last_measured' : self.feeding_last_measured}

    # @property
    # def milk_production(self):
    #     return {'last_milk': self.milk_prod_last_milk, 'last_milk': self.milk_prod_last_milk, 'amount_l': self.milk_prod_amount_l}


    def __repr__(self):
        return (
            f"**Cow** "
            f"cow_id: {self.cow_id} "
            f"name: {self.name} "
            f"sex: {self.sex}"
            f"birthdate: {self.birthdate} "
            f"condition: {self.condition} "
            f"has_calves: {self.has_calves}"
            f"**Cow** "
            f"**Weight** "
            f"mass_kg: {self.weight_mass_kg}"
            f"last_measured: {self.weight_last_measured} "
            f"**Weight** "
            f"**Feeding** "
            f"amount_kg: {self.feeding_amount_kg} "
            f"cron_schedule: {self.feeding_cron_schedule}"
            f"last_measured: {self.feeding_last_measured} "
            f"**Feeding** "
            f"**MilkProduction** "
            f"last_milk: {self.milk_prod_last_milk} "
            f"cron_schedule: {self.milk_prod_cron_schedule}"
            f"prod_amount_l: {self.milk_prod_amount_l} "
            f"**MilkProduction** "
        )

