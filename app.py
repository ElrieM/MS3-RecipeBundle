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
    recipes = list(mongo.db.recipes.find())
    return render_template("collection.html", recipes=recipes)


@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    if request.method == "POST":
        recipe = {
            "recipe_name": request.form.get("recipe_name"),
            "cuisine": request.form.get("cuisine"),
            "type": request.form.get("type"),
            "diet": request.form.get("diet"),
            "ingredients": request.form.get("ingredients"),
            "method": request.form.get("method"),
            "total_time": request.form.get("total_time"),
            "active_time": request.form.get("active_time")
        }
        mongo.db.recipes.insert_one(recipe)
        flash("Recipe added")
        return redirect(url_for("collection"))

    return render_template("add_recipe.html")


@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    if request.method == "POST":
        submit = {
            "recipe_name": request.form.get("recipe_name"),
            "cuisine": request.form.get("cuisine"),
            "type": request.form.get("type"),
            "diet": request.form.get("diet"),
            "ingredients": request.form.get("ingredients"),
            "method": request.form.get("method"),
            "total_time": request.form.get("total_time"),
            "active_time": request.form.get("active_time")
        }

        mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, submit)
        flash("Recipe changes saved")

    update_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template("edit_recipe.html", recipe=update_recipe)


@app.route("/select_recipe/<recipe_id>")
def select_recipe(recipe_id):
    sel_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template("recipes.html", recipe=sel_recipe)


@app.route("/search")
def search():
    return render_template("search.html")


@app.route("/admin")
def admin():
    cuisines = list(mongo.db.recipes.find())
    return render_template("admin.html", cuisines = cuisines)


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
