# models.py
from flask_sqlalchemy import SQLAlchemy

# Initialize the database
db = SQLAlchemy()


class Parts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    partName = db.Column(db.String(80), nullable=False)
    partType = db.Column(db.String(80), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"<Part {self.partName}>"
