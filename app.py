from flask import Flask, request, jsonify, render_template
from models import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)

app.config['SECRET_KEY'] = "mmmmmmmmcupCakes"
from flask_debugtoolbar import DebugToolbarExtension
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

# HTML ROUTE ****************************************

@app.route('/')
def show_blank_homepage():
    """Show a blank page"""

    return render_template('index.html')


# RESTful JSON API ROUTES ****************************************

def serialize_cupcake(cupcake):
    """Serialize a cupcake SQLAlchemy obj to dictionary."""

    return {
        "id": cupcake.id,
        "flavor": cupcake.flavor,
        "size": cupcake.size,
        "rating": cupcake.rating,
        "image": cupcake.image,
    }   


@app.route('/api/cupcakes')
def list_all_cupcakes():
    """Return JSON object for each cupcake in db.
    Show id, flavor, size, ratin, image."""

    cupcakes = Cupcake.query.all()
    serialized = [serialize_cupcake(c) for c in cupcakes]

    return jsonify(cupcakes=serialized)


@app.route('/api/cupcakes/<int:cupcake_id>')
def list_single_cupcake(cupcake_id):
    """Return JSON object for 1 cupcake"""

    cupcake = Cupcake.query.get_or_404(cupcake_id)
    serialized = serialize_cupcake(cupcake)

    return jsonify(cupcake=serialized)


@app.route('/api/cupcakes', methods = ['POST'])
def create_new_cupcake():
    """Create a new cupcake. Return new JSON object"""

    flavor  = request.json.get('flavor')
    size    = request.json.get('size')
    rating  = request.json.get('rating')
    image   = request.json.get('image')

    new_cupcake = Cupcake(flavor=flavor, size=size, rating=rating, image=image)

    db.session.add(new_cupcake)
    db.session.commit()

    serialized = serialize_cupcake(new_cupcake)

    return (jsonify(cupcake=serialized), 201)


@app.route('/api/cupcakes/<int:cupcake_id>', methods = ['PATCH'])
def update_cupcake(cupcake_id):

    cupcake = Cupcake.query.get_or_404(cupcake_id)

    cupcake.flavor  = request.json.get('flavor', cupcake.flavor)
    cupcake.size    = request.json.get('size', cupcake.size)
    cupcake.rating  = request.json.get('rating', cupcake.rating)
    cupcake.image   = request.json.get('image', cupcake.image)

    # import pdb
    # pdb.set_trace()

    db.session.commit()

    serialized = serialize_cupcake(cupcake)

    return jsonify(cupcake=serialized)


@app.route('/api/cupcakes/<int:cupcake_id>', methods = ['DELETE'])
def delete_cupcake(cupcake_id):

    cupcake = Cupcake.query.get_or_404(cupcake_id)

    db.session.delete(cupcake)
    db.session.commit()

    return jsonify(message="deleted")

