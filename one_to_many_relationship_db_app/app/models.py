from app import app, db
from datetime import datetime

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    links = db.relationship('Link', backref='category')

class Link(db.Model):
    # To find all the datatypes can used for columns can find by printing below link 
    # print(dir(db.types))

    # Column args, autoincrement, default, nullable, primary_key, unique, quote (to force quote), comment
    id = db.Column(db.Integer, primary_key=True)
    link = db.Column(db.String(200), unique=True, nullable=False)
    title = db.Column(db.String(50), nullable=False)
    created = db.Column(db.DateTime(), default=datetime.now())
    updated = db.Column(db.DateTime())
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))

    # To create db if not exsist
    def create_db(self):
        with app.app_context():
            db.create_all()

    # Add current obj of link to db
    def add(self):
        db.session.add(self)
        db.session.commit()

    # Update current obj of link to db
    def update(self):
        self.updated = datetime.now()
        db.session.commit()

    # Delete current obj of link from db
    def delete(self):
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
