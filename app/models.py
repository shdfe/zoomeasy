from app import db
from datetime import datetime

class Zoom(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    class_link = db.Column(db.String(50))
    class_name = db.Column(db.String(50))
    start_time = db.Column(db.DateTime, default=datetime.utcnow())
    done = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'Zoom {self.class_name}'



#for now, make one zoom class schema, then deveop user schema and user class and make one to many relationship with db.relationship()