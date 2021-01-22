from database.db_setup import db


class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    street_name = db.Column(db.VARCHAR(length=100), nullable=False)
    house_number = db.Column(db.VARCHAR(length=15), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=db.func.now(), onupdate=db.func.now())
    updated_at = db.Column(db.DateTime(timezone=True),
                           server_default=db.func.now(), onupdate=db.func.now())
