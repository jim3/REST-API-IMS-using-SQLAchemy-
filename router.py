from flask import Blueprint, request, jsonify
from Parts import Parts, db

part_routes = Blueprint('part_routes', __name__)


# Get all parts
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


# Add a part
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


# Update a part
@part_routes.route('/api/parts/<int:id>', methods=['PUT'])
def update_part(id):
    print('Updating a part')
    part = Parts.query.get(id)
    part.partName = request.json['partName']
    part.partType = request.json['partType']
    part.quantity = request.json['quantity']
    part.price = request.json['price']
    db.session.commit()
    return jsonify({'message': 'Part updated successfully'})


# Delete a part
@part_routes.route('/api/parts/<int:id>', methods=['DELETE'])
def delete_part(id):
    print('Deleting a part')
    part = Parts.query.get(id)
    db.session.delete(part)
    db.session.commit()
    return jsonify({'message': 'Part deleted successfully'})


# Get a part
@part_routes.route('/api/parts/<int:id>', methods=['GET'])
def get_part(id):
    print('Getting a part')
    part = Parts.query.get(id)
    part_dict = {
        'id': part.id,
        'partName': part.partName,
        'partType': part.partType,
        'quantity': part.quantity,
        'price': part.price
    }
    return jsonify(part_dict)
