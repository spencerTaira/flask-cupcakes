"""Flask app for Cupcakes"""
from flask import Flask, redirect, render_template, jsonify, request
from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, Cupcake, DEFAULT_IMAGE_URL


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)

app.config['SECRET_KEY'] = "I'LL NEVER TELL!!"

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)


@app.get('/')
def show_home():
    """ Renders homepage """

    return render_template('home.html')

@app.get('/api/cupcakes')
def cupcakes_info():
    """ Return JSON with all cupcakes info
    {cupcakes: [{id, flavor, size, rating, image}, ...]}
    """

    cupcakes = Cupcake.query.all()
    serialized = [c.serialize() for c in cupcakes]

    return jsonify(cupcakes=serialized)


@app.get('/api/cupcakes/<int:cupcake_id>')
def cupcake_info(cupcake_id):
    """ Return JSON with a single cupcake's info.
    {cupcake: {id, flavor, size, rating, image}}
    """

    cupcake = Cupcake.query.get_or_404(cupcake_id)
    serialized = cupcake.serialize()

    return jsonify(cupcake=serialized)


@app.post('/api/cupcakes')
def cupcake_add():
    """ Add a new cupcake to the databse. Takes in JSON with the
    necessary constructors:
    Example:
        {
        "flavor": "cherry",
        "size": "small",
        "rating": "5",
        "image": ""
        }

    On success, returns JSON with cupcake info, and
    status code 201.

    {cupcake: {id, flavor, size, rating, image}}

    """

    flavor = request.json['flavor']
    size = request.json['size']
    rating = request.json['rating']
    image = request.json['image']

    # set default image
    image = image or None

    new_cupcake = Cupcake(
        flavor=flavor,
        size=size,
        rating=rating,
        image=image
    )

    db.session.add(new_cupcake)
    db.session.commit()

    serialized = new_cupcake.serialize()
    return (jsonify(cupcake=serialized), 201)


@app.patch('/api/cupcakes/<int:cupcake_id>')
def cupcake_update(cupcake_id):
    """Updates a cupcake's information. Takes in cupcake_id in the URL
    and any updated information in the request body as JSON
    Example input:
      {
        "flavor": "cherry",
        "size": "small",
        "rating": "5",
        "image": ""
        }

    Returns JSON with newly-updated cupcake info. Status code
    200 on success, or 404 if cupcake cannot be found.:

    Returns JSON like:
        {cupcake: {id, flavor, size, rating, image}}

    """

    cupcake = Cupcake.query.get_or_404(cupcake_id)

    cupcake.image = request.json.get('image') or cupcake.image
    cupcake.rating = request.json.get('rating', cupcake.rating)
    cupcake.size = request.json.get('size', cupcake.size)
    cupcake.flavor = request.json.get('flavor', cupcake.flavor)

    db.session.commit()

    serialized = cupcake.serialize()

    return jsonify(cupcake=serialized)


@app.delete('/api/cupcakes/<int:cupcake_id>')
def cupcake_delete(cupcake_id):
    """ Deletes a cupcake record from cupcakes table in database

    Returns JSON like:
        {deleted: [cupcake-id]}

    and status code 200 on success, or 404 if cupcake cannot be found.
    """
    # Cupcake.query.filter(...).delete()
    cupcake = Cupcake.query.get_or_404(cupcake_id)

    db.session.delete(cupcake)
    db.session.commit()

    return jsonify(deleted=cupcake_id)
