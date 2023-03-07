import logging
import sys
from os import path

sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))


from flask import Flask
from flask_restful import Api

from farm_api.constants import PROJECT_ROOT, INGRID_FARM_DATABASE
from farm_api.database import db
from farm_api.resources.cows_resource import CowsResource, COWS_ENDPOINT


# def create_app():
def create_app(db_location, *args):

    """
    Function that creates our Flask application.
    This function creates the Flask app, Flask-RESTful API,
    and Flask-SQLAlchemy connection

    :param db_location: Connection string to the database
    :return: Initialized Flask app
    """
    # This configures our logging, writing all logs to the file "cow_api.log"
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s %(name)-12s %(levelname)-8s %(message)s",
        datefmt="%m-%d %H:%M",
        handlers=[logging.FileHandler("cow_api.log"), logging.StreamHandler()],
    )

    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = db_location
    db.init_app(app)
    with app.app_context():
        db.create_all()
    api = Api(app)
    api.add_resource(CowsResource, COWS_ENDPOINT, f"{COWS_ENDPOINT}")
    return app


     

if __name__ == "__main__":
    app = create_app(f"sqlite:////{PROJECT_ROOT}/{INGRID_FARM_DATABASE}")
    app.run(debug=True)