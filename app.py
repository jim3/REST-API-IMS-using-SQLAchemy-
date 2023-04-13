from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import router
from Parts import db

app = Flask(__name__)

# Register the the routes from router.py
app.register_blueprint(router.part_routes)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///parts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

try:
    with app.app_context():
        db.create_all()
except Exception as e:
    print("Error creating database:", e)

if __name__ == '__main__':
    app.run(debug=True)  # run the app in debug mode
