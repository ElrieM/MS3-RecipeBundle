import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404


@app.route("/")
@app.route("/collection")
def collection():
    recipes = mongo.db.recipes.find()
    return render_template("collection.html", recipes=recipes)


@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/recipes/<recipe>")
def recipes(recipe):
    if recipe:
        return render_template("recipes.html", recipe=recipe)


@app.route("/search")
def search():
    return render_template("search.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # confirm username not already in DB
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username")})

        if existing_user:
            flash("Username already exists, please try again")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username"),
            "email": request.form.get("email"),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # store new user in 'session' cookie
        session["user"] = request.form.get("username")
        flash("Welcome, {}".format(request.form.get("username")))
        return redirect(url_for("collection", username=session["user"]))

    return render_template("register.html")


@app.route("/signin", methods=["GET", "POST"])
def signin():
    if request.method == "POST":
        # searches username in db
        user_exists = mongo.db.users.find_one(
            {"username": request.form.get("username")})

        if user_exists:
            # Checks password agrees to saved in db before allowing access
            if check_password_hash(
                    user_exists["password"], request.form.get("password")):
                session["user"] = request.form.get("username")
                flash("Welcome, {}".format(request.form.get("username")))
                return redirect(url_for("collection",
                                username=session["user"]))
            else:
                # Message if password incorrect
                flash("Credentials do not match, please try again")
                return redirect(url_for("signin"))

        else:
            # Message if username not found
            flash("Credentials do not match, please try again")
            return redirect(url_for("signin"))

    return render_template("signin.html")


@app.route("/signout")
def signout():
    session.pop('user')
    flash("Sign out successful")
    return redirect(url_for("signin"))


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
