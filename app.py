from flask import Flask, request
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource
from swagger_ui import api_doc
from flask_migrate import Migrate
from config import Config

app = Flask(__name__)

app.config.from_object(Config)

db = SQLAlchemy(app)
ma = Marshmallow(app)
api = Api(app)
mi = Migrate(app, db)


api_doc(
    app,
    config_path='./specs/test.yaml',
    url_prefix='/api/doc',
    title='API doc'
)


def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    return app


class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    start_time = db.Column(db.String(200))
    end_time = db.Column(db.String(200))

    def __init__(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time


class BookingSchema(ma.Schema):
    class Meta:
        fields = ('id', 'date', 'start_time', 'end_time')


class BookingList(Resource):
    def get(self):
        bookings = Booking.query.all()

        return BookingSchema(many=True).dump(bookings)

    def post(self):
        data = request.json

        booking = Booking(data["start_time"], data["end_time"])
        bookings = Booking.query.filter(
            Booking.start_time >= data["start_time"],
            Booking.end_time <= data["end_time"]
        ).first()

        if bookings:
            return BookingSchema(many=False).dump(booking), 400

        db.session.add(booking)
        db.session.commit()

        return BookingSchema(many=False).dump(booking)


api.add_resource(BookingList, "/bookings")
