# models.py
# Defines your database models (e.g., SQLAlchemy models):
# StoreData class (structure to be defined later)
# Report class (structure to be defined later)


from storestate.database import db


class StoreData(db.Model):
    __tablename__ = "storedatab"
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(120))
    created_at = db.Column(db.DateTime(timezone=True), server_default=db.func.current_timestamp())

