from app import app, db
from datetime import datetime

class Link(db.Model):
    # To find all the datatypes can used for columns can find by printing below link 
    # print(dir(db.types))

    # Column args, autoincrement, default, nullable, primary_key, unique, quote (to force quote), comment
    id = db.Column(db.Integer, primary_key=True)
    link = db.Column(db.String(200), unique=True, nullable=False)
    title = db.Column(db.String(50), nullable=False)
    created = db.Column(db.DateTime(), default=datetime.now())
    updated = db.Column(db.DateTime())

    def create_db(self):
        with app.app_context():
            db.create_all()

    def add(self):
        self.create_db()
        db.session.add(self)
        db.session.commit()

    def update(self):
        self.create_db()
        self.updated = datetime.now()
        db.session.commit()

    def delete(self):
        self.create_db()
        db.session.delete(self)
        db.session.commit()
    
    def json(self):
        return {
            "id" : self.id,
            "title" : self.title,
            "link" : self.link,
        }

    def __repr__(self):
        return 'Link(id={}, link={}, title={})'.format(self.id, self.link, self.title)
