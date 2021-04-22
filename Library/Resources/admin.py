from flask_restful import Resource, reqparse, request
from flask import Response
from Library import db
from Library.Models.publisher import PublisherModel
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
            publisherObject = PublisherModel(data['name'],data['address'], data['phone'])
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