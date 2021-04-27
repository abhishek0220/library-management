from flask_restful import Resource, reqparse, request
from flask import Response
from Library import db
from Library.Models.allModels import *

import os

class Publisher(Resource):
    def get(self):
        return PublisherModel.all_publisher()

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('p_id', required = False)
        parser.add_argument('name', help = 'This field cannot be blank', required = True)
        parser.add_argument('address', help = 'This field cannot be blank', required = True)
        parser.add_argument('phone', help = 'This field cannot be blank', required = True)
        data = parser.parse_args()
        if(data['p_id'] == None):
            publisherObject = PublisherModel(data['name'], data['address'], data['phone'])
        else:
            publisherObject = db.session.query(PublisherModel).filter(PublisherModel.p_id == data['p_id']).first()
            if(publisherObject == None):
                return Response("{'message': '404 Not Found', 'status' : 404}", status=404, mimetype='application/json')
            publisherObject.p_name = data['name']
            publisherObject.address = data['address']
            publisherObject.phone = data['phone']
        try:
            publisherObject.save_to_db()
        except Exception as e:
            print(e)
            return Response("{'message': 'Internal Server Error', 'status' : 503}", status=503, mimetype='application/json')
        else:
            return Response("{'message': 'added Successfully', 'status' : 200}", status=200, mimetype='application/json')

    def delete(self):
        p_id = request.args.get('id', -1)
        if(p_id == -1):
            return Response("{'message': 'Please pass valid id to be deleted', 'status' : 200}", status=200, mimetype='application/json')
        db.session.query(PublisherModel).filter(PublisherModel.p_id == p_id).delete()
        db.session.commit()
        return Response("{'message': 'Deleted Successfully', 'status' : 200}", status=200, mimetype='application/json')


class Rental(Resource):
    def get(self):
        return RentalModel.all_rentals()

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('rentalId', required = False)
        parser.add_argument('price', help = 'This field cannot be blank', required = True)
        parser.add_argument('fine', help = 'This field cannot be blank', required = True)
        parser.add_argument('limit', help = 'This field cannot be blank', required = True)
        data = parser.parse_args()

        if(data['rentalId'] == None):
            rentalObject = RentalModel(data['price'], data['fine'], data['limit'])
        else:
            rentalObject = db.session.query(RentalModel).filter(RentalModel.rental_id == data['rentalId']).first()

            if(rentalObject == None):
                return Response("{'message': '404 Not Found', 'status' : 404}", status=404, mimetype='application/json')

            rentalObject.price_day = data['price']
            rentalObject.fine_day = data['fine']
            rentalObject.limit_day = data['limit']

        # commiting changes to database
        try:
            rentalObject.save_to_db()
        except Exception as e:
            print(e)
            return Response("{'message': 'Internal Server Error', 'status' : 503}", status=503, mimetype='application/json')
        else:
            return Response("{'message': 'added Successfully', 'status' : 200}", status=200, mimetype='application/json')


    def delete(self):
        rental_id = request.args.get('id', -1)

        if(rental_id == -1):
            return Response("{'message': 'Please pass valid id to be deleted', 'status' : 200}", status=200, mimetype='application/json')

        # commiting changes to database
        db.session.query(RentalModel).filter(RentalModel.rental_id == rental_id).delete()
        db.session.commit()

        # returning the successful response of deletion
        return Response("{'message': 'Deleted Successfully', 'status' : 200}", status=200, mimetype='application/json')

class Reader(Resource):
    def get(self):
        return ReaderModel.all_readers()

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('reader_id', required = False)
        parser.add_argument('name', help = 'This field cannot be blank', required = True)
        parser.add_argument('email', help = 'This field cannot be blank', required = True)
        parser.add_argument('charges', help = 'This field cannot be blank', required = True)
        data = parser.parse_args()

        if(data['reader_id'] == None):
            readerObject = ReaderModel(data['name'], data['email'], data['charges'])
        else:
            readerObject = db.session.query(ReaderModel).filter(ReaderModel.reader_id == data['reader_id']).first()

            if(readerObject == None):
                return Response("{'message': '404 Not Found', 'status' : 404}", status=404, mimetype='application/json')

            readerObject.name = data['name']
            readerObject.email = data['email']
            readerObject.charges = data['charges']

        # commiting changes to database
        try:
            readerObject.save_to_db()
        except Exception as e:
            print(e)
            return Response("{'message': 'Internal Server Error', 'status' : 503}", status=503, mimetype='application/json')
        else:
            return Response("{'message': 'added Successfully', 'status' : 200}", status=200, mimetype='application/json')


    def delete(self):
        reader_id = request.args.get('id', -1)

        if(reader_id == -1):
            return Response("{'message': 'Please pass valid id to be deleted', 'status' : 200}", status=200, mimetype='application/json')

        # commiting changes to database
        db.session.query(ReaderModel).filter(ReaderModel.reader_id == reader_id).delete()
        db.session.commit()

        # returning the successful response of deletion
        return Response("{'message': 'Deleted Successfully', 'status' : 200}", status=200, mimetype='application/json')

class TestClass(Resource):
    def get(self):
        #pm = PublisherModel("Manning Publications Company", "NONE", "+919879879876")
        #pm.save_to_db()
        #rm = RentalModel(5,3,7)
        #rm.save_to_db()
        '''
        bm = BooksModel(
            name = 'Unlocking Android',
            isbn = 1933988673,
            total_copies = 5,
            available_copies = 5,
            #authors = db.Column(db.ARRAY(db.String(50))),
            pages = 416,
            thumbnail_url = 'https://s3.amazonaws.com…thumb-images/ableson.jpg',
            #categories = db.Column(db.ARRAY(db.String(50))),
            short_desc = "Unlocking Android: A Developer's Guide provides concise, hands-on instruction for the Android operating system and development tools. This book teaches important architectural concepts in a straightforward writing style and builds on this with practical and useful examples throughout.",
            #long_desc = db.Column(db.String(120), nullable=True),
            p_id = 1,
            rental_id = 1,
        )
        bm.save_to_db()
        '''
        b : BooksModel = db.session.query(BooksModel).first()
        print(b.publishers)
        return "hii"