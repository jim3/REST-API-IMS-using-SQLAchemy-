from flask import Blueprint, request, jsonify
from Parts import Parts, db

part_routes = Blueprint('part_routes', __name__)


@part_routes.route('/api/parts', methods=['GET'])
def parts():
    all_parts = Parts.query.all()
    parts_list = []
    for part in all_parts:
        part_dict = {
            'id': part.id,
            'partName': part.partName,
            'partType': part.partType,
            'quantity': part.quantity,
            'price': part.price
        }
        parts_list.append(part_dict)
    return jsonify(parts_list)


@part_routes.route('/api/parts', methods=['POST'])
def add_part():
    print('Adding a new part')
    part = Parts(    # creates a new Parts object
        partName=request.json['partName'],
        partType=request.json['partType'],
        quantity=request.json['quantity'],
        price=request.json['price']
    )
    db.session.add(part)  # adds Parts objects to the database session
    db.session.commit()  # commits the transaction
    return jsonify({'message': 'Part added successfully'})

