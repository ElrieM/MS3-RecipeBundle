import os
from flask import (Flask)
from flask_pymongo import PyMongo

if os.path.exists("env.py"):
    import env

# Create Flask App
app = Flask(__name__)

# Variables to connect to MongoDB
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)
mongo.init_app(app)


def create_app():
    """
    Import routes and assign blueprint to create app
    """
    # Route import
    from recipe_bundle.admin.routes import admin
    from recipe_bundle.auth.routes import auth
    from recipe_bundle.contact.routes import cont
    from recipe_bundle.err.routes import err
    from recipe_bundle.manage.routes import manage
    from recipe_bundle.recipes.routes import recipes
    # Blueprint routes
    app.register_blueprint(admin)
    app.register_blueprint(auth)
    app.register_blueprint(cont)
    app.register_blueprint(err)
    app.register_blueprint(manage)
    app.register_blueprint(recipes)
    # Return app
    return app
