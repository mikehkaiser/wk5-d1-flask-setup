from flask import Blueprint, request, jsonify
from bikes_inventory.helpers import token_required
from bikes_inventory.models import db, User, Bike, bike_schema, bikes_schema


api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/get')
def get():
    return {'surly':42069, 'black mountain cycles': 'MCD'}

@api.route('/bikes', methods = ['POST'])
@token_required
def create_bike(current_user_token):
    model_name = request.json['model_name']
    manufacturer = request.json['manufacturer']
    size = request.json['size']
    msrp = request.json['msrp']
    frame_material = request.json['frame_material']
    category = request.json['category']
    speeds = request.json['speeds']
    stock_weight = request.json['stock_weight']
    user_token = current_user_token.token

    print(f'TESTER: {current_user_token.token}')

    bike = Bike(model_name, manufacturer, size, msrp, frame_material,
    category, speeds, stock_weight, user_token = user_token)

    db.session.add(bike)
    db.session.commit()

    response = bike_schema.dump(bike)
    return jsonify(response)

# retrieve all bikes
@api.route('/bikes', methods = ['GET'])
@token_required
def get_bikes(current_user_token):
    owner = current_user_token.token
    bikes = Bike.query.filter_by(user_token=owner).all()
    response = bikes_schema.dump(bikes)
    return jsonify(response)

#retrieve single bike endpoint
@api.route('/bikes/<id>')
@token_required
def get_bike(current_user_token, id):
    bike = Bike.query.get(id)
    response = bike_schema.dump(bike)
    return jsonify(response)

#Update and Delete
@api.route('/bikes/<id>', methods = ['POST'])
@token_required
def update_bike(current_user_token, id):
    bike = Bike.query.get(id)
    print(bike)
    if bike:
        bike.model_name = request.json['model_name']
        bike.manufacturer = request.json['manufacturer']
        bike.size = request.json['size']
        bike.msrp = request.json['msrp']
        bike.frame_material = request.json['frame_material']
        bike.category = request.json['category']
        bike.speeds = request.json['speeds']
        bike.stock_weight = request.json['stock_weight']
        bike.user_token = current_user_token.token

        db.session.commit()

        response = bike_schema.dump(bike)
        return jsonify(response)
    else:
        return jsonify({'Error':"That bike doesn't exist yet."})

@api.route('/bikes/<id>', methods = ['DELETE'])
@token_required
def delete_bike(current_user_token, id):
    bike = Bike.query.get(id)
    if bike:
        db.session.delete(bike)
        db.session.commit()

        response = bike_schema.dump(bike)
        return jsonify(response)
    else:
        return jsonify({'Error': 'That bike does not exist.'})