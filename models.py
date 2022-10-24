"""Models for Cupcake app."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DEFAULT_IMAGE_URL = 'https://tinyurl.com/demo-cupcake'


class Cupcake(db.Model):
    """Individual Cupcake"""

    __tablename__ = 'cupcakes'

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    flavor = db.Column(db.String(20),
                       nullable=False)
    size = db.Column(db.String(20),
                     nullable=False)
    rating = db.Column(db.Integer,
                       nullable=False)
    image = db.Column(db.Text,
                      nullable=False,
                      default=DEFAULT_IMAGE_URL)

    def serialize(self):
        return {
            "id": self.id,
            "flavor": self.flavor,
            "size": self.size,
            "rating": self.rating,
            "image": self.image
        }

# DO NOT MODIFY THIS FUNCTION


def connect_db(app):
    """Connect to database."""

    app.app_context().push()
    db.app = app
    db.init_app(app)
