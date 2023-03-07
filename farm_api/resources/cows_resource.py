from datetime import datetime
import logging

from flask import request
from flask_restful import Resource, abort
from sqlalchemy.exc import IntegrityError
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound
from marshmallow import ValidationError

from farm_api.database import db
from farm_api.models.cow import Cow
from farm_api.schemas.cow_schema import CowSchema
from farm_api.schemas.feeding_schema import FeedingSchema
from farm_api.schemas.milk_prod_schema import MilkProductionSchema
from farm_api.schemas.weight_schema import WeightSchema


COWS_ENDPOINT = "/api/cow"
logger = logging.getLogger(__name__)


class CowsResource(Resource):
    def get(self):
        """
        CowsResource GET method. Retrieves all cows found in the Farm

        :param cow_id: Cow ID to retrieve, this request parameter is optional
        can also filter by name or sex
        :return: Cow, 200 HTTP status code
        """
        try:
            sex = request.args.get('sex')
            name = request.args.get('name')
            cow_id = request.args.get('cow_id')
            cows = Cow.query.filter_by(**request.args).all()

            cows_json = [ CowSchema().dump(self.cow_to_schema(cow)) for cow in cows]
            logger.info("Cows successfully retrieved.", cows_json)
            return cows_json
        except InvalidRequestError as e:
            logger.warning(
                f"You have passed an invalid query value. Error: {e}"
            )

            abort(400, message="You queried by an invalid query parameter, you can query with name, sex or cow_id!")


    def delete(self):
        id = request.args.get('id')
        cow = Cow.query.get_or_404(id, "the cow you try to delete doesnt exist")
        db.session.delete(cow)
        db.session.commit()
        return '', 204

    def post(self):
        """
        CowsResource POST method. Adds a new Cow to the database.

        :return: Cow.cow, 201 HTTP status code.
        """

        data = request.get_json()

        try:
            cow = self.schema_to_cow(data)
        except ValidationError as e:
            return {
                "error" : e.messages
            }, 400


        try:
            db.session.add(cow)
            db.session.commit()
            cow_json = CowSchema().dump(self.cow_to_schema(cow))
        except IntegrityError as e:
            logger.warning(
                f"Duplicate Error, this cow is already in the database. Error: {e}"
            )

            abort(500, message="Unexpected Error!")
        else:
            return cow_json, 201

    def patch(self):
        id = request.args.get('id')
        cow = Cow.query.get_or_404(id, "the cow you try to edit doesnt exist")

        if 'name' in request.json:
            cow.name = request.json['name']
        if 'sex' in request.json:
            cow.sex = request.json['sex']

        cow_json = CowSchema().dump(self.cow_to_schema(cow))

        db.session.commit()
        return cow_json

    def cow_to_schema(self, cow:Cow) -> CowSchema:
        new_cow = CowSchema()
        new_cow.cow_id = cow.cow_id
        new_cow.birthdate = datetime.strptime(cow.birthdate, '%Y-%m-%d %H:%M:%S')  #change format to '%Y-%m-%d %H:%M:%S'
        new_cow.name = cow.name
        new_cow.has_calves = cow.has_calves
        new_cow.condition = cow.condition
        new_cow.sex = cow.sex


        weight = WeightSchema()
        weight.cron_schedule = cow.milk_prod_cron_schedule
        weight.last_measured = datetime.strptime(cow.weight_last_measured, '%Y-%m-%d %H:%M:%S') #change format to '%Y-%m-%d %H:%M:%S'

        feeding = FeedingSchema()
        feeding.cron_schedule = cow.feeding_cron_schedule
        feeding.last_measured = datetime.strptime(cow.feeding_last_measured, '%Y-%m-%d %H:%M:%S') #change format to '%Y-%m-%d %H:%M:%S'
        feeding.amount_kg = cow.feeding_amount_kg

        milk_production = MilkProductionSchema()
        milk_production.amount_l = cow.milk_prod_amount_l
        milk_production.last_milk = datetime.strptime(cow.milk_prod_last_milk, '%Y-%m-%d %H:%M:%S') #change format to '%Y-%m-%d %H:%M:%S'
        milk_production.cron_schedule = cow.milk_prod_cron_schedule

        new_cow.feeding = feeding
        new_cow.milk_production = milk_production
        new_cow.weight = weight

        return new_cow
    
    def validate(self, data: dict) -> None:
        CowSchema().load(data)

    def schema_to_cow(self, data: dict) -> Cow:
        self.validate(data)

        new_cow = Cow()
        new_cow.birthdate = data['birthdate']
        new_cow.name = data['name']
        new_cow.has_calves = data['has_calves']
        new_cow.condition = data['condition']
        new_cow.sex = data['sex']
        new_cow.milk_prod_amount_l = data['milk_production']['amount_l']
        new_cow.milk_prod_last_milk = data['milk_production']['last_milk']
        new_cow.milk_prod_cron_schedule = data['milk_production']['cron_schedule']
        new_cow.weight_last_measured = data['weight']['last_measured']
        new_cow.weight_mass_kg = data['weight']['mass_kg']
        new_cow.feeding_cron_schedule = data['feeding']['cron_schedule']
        new_cow.feeding_last_measured = data['feeding']['last_measured']
        new_cow.feeding_amount_kg = data['feeding']['amount_kg']
        return new_cow