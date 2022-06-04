from flask import Flask, request
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource
from flask_migrate import Migrate, upgrade

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://dev:dev@db/test'

app.config.update(
    TESTING=True,
    DEBUG=True,
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
    SECRET_KEY='192b9bdd22ab9ed4d12e236c78afcb9a393ec15f71bbf5dc987d54727823bcbf'
)

db = SQLAlchemy(app)
ma = Marshmallow(app)
api = Api(app)
mi = Migrate(app, db)


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