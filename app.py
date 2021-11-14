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
            "type": request.form.get("mealType"),
            "diet": request.form.get("diet"),
            "ingredients": request.form.getlist("ingredients[]"),
            "method": request.form.getlist("method[]"),
            "total_time": request.form.get("total_time"),
            "active_time": request.form.get("active_time")
        }
        mongo.db.recipes.insert_one(recipe)
        flash("Recipe added")
        return redirect(url_for("collection"))

    cuisines = mongo.db.cuisines.find().sort("cuisine_name", 1)
    mealtypes = mongo.db.types.find().sort("mealtype_name", 1)
    diets = mongo.db.diets.find().sort("diet_name", 1)
    return render_template("add_recipe.html", cuisines=cuisines,
                           mealtypes=mealtypes, diets=diets)


@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    if request.method == "POST":
        submit = {
            "recipe_name": request.form.get("recipe_name"),
            "cuisine": request.form.get("cuisine"),
            "type": request.form.get("type"),
            "diet": request.form.get("diet"),
            "ingredients": request.form.getlist("ingredients[]"),
            "method": request.form.getlist("method[]"),
            "total_time": request.form.get("total_time"),
            "active_time": request.form.get("active_time")
        }
        mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, submit)
        flash("Recipe changes saved")

    update_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    cuisines = mongo.db.cuisines.find().sort("cuisine_name", 1)
    mealtypes = mongo.db.types.find().sort("mealtype_name", 1)
    diets = mongo.db.diets.find().sort("diet_name", 1)
    return render_template("edit_recipe.html", cuisines=cuisines,
                           mealtypes=mealtypes, diets=diets,
                           recipe=update_recipe)


@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    flash("Recipe successfully deleted")
    return redirect(url_for("collection"))


@app.route("/select_recipe/<recipe_id>")
def select_recipe(recipe_id):
    sel_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template("recipes.html", recipe=sel_recipe)


@app.route("/search")
def search():
    return render_template("search.html")


@app.route("/add_diet", methods=["GET", "POST"])
def add_diet():
    if request.method == "POST":
        new_diet = {
            "diet_name": request.form.get("diet_name")
        }
        mongo.db.diets.insert_one(new_diet)
        flash("New diet option added")
        return redirect(url_for("admin"))

    return render_template("add_diet.html")


@app.route("/edit_diet/<diet_id>", methods=["GET", "POST"])
def edit_diet(diet_id):
    if request.method == "POST":
        submit = {
            "diet_name": request.form.get("diet_name")
        }
        mongo.db.diets.update({"_id": ObjectId(diet_id)}, submit)
        flash("Diets successfully updated")
        return redirect(url_for("admin"))

    diet = mongo.db.diets.find_one({"_id": ObjectId(diet_id)})
    return render_template("edit_diet.html", diet=diet)


@app.route("/delete_diet/<diet_id>", methods=["GET", "POST"])
def delete_diet(diet_id):
    mongo.db.diets.remove({"_id": ObjectId(diet_id)})
    flash("Diets successfully removed")


@app.route("/add_mealtype", methods=["GET", "POST"])
def add_mealtype():
    if request.method == "POST":
        new_mealtype = {
            "mealtype_name": request.form.get("mealtype_name")
        }
        mongo.db.types.insert_one(new_mealtype)
        flash("New meal type option added")
        return redirect(url_for("admin"))

    return render_template("add_mealtype.html")


@app.route("/edit_mealtype/<mealtype_id>", methods=["GET", "POST"])
def edit_mealtype(mealtype_id):
    if request.method == "POST":
        submit = {
            "mealtype_name": request.form.get("mealtype_name")
        }
        mongo.db.types.update({"_id": ObjectId(mealtype_id)}, submit)
        flash("Meal type successfully updated")

    mealtype = mongo.db.types.find_one({"_id": ObjectId(mealtype_id)})
    return render_template("edit_mealtype.html", mealtype=mealtype)


@app.route("/delete_mealtype/<mealtype_id>", methods=["GET", "POST"])
def delete_mealtype(mealtype_id):
    mongo.db.types.remove({"_id": ObjectId(mealtype_id)})
    flash("Meal type successfully removed")


@app.route("/add_cuisine", methods=["GET", "POST"])
def add_cuisine():
    if request.method == "POST":
        new_cuisine = {
            "cuisine_name": request.form.get("cuisine_name")
        }
        mongo.db.cuisines.insert_one(new_cuisine)
        flash("New cuisine option added")
        return redirect(url_for("admin"))

    return render_template("add_cuisine.html")


@app.route("/edit_cuisine/<cuisine_id>", methods=["GET", "POST"])
def edit_cuisine(cuisine_id):
    if request.method == "POST":
        submit = {
            "cuisine_name": request.form.get("cuisine_name")
        }
        mongo.db.cuisines.update({"_id": ObjectId(cuisine_id)}, submit)
        flash("Cuisine successfully updated")
        return redirect(url_for("admin"))

    cuisine = mongo.db.cuisines.find_one({"_id": ObjectId(cuisine_id)})
    return render_template("edit_cuisine.html", cuisine=cuisine)


@app.route("/delete_cuisine/<cuisine_id>", methods=["GET", "POST"])
def delete_cuisine(cuisine_id):
    mongo.db.cuisines.remove({"_id": ObjectId(cuisine_id)})
    flash("Cuisine successfully removed")


@app.route("/admin")
def admin():
    cuisines = list(mongo.db.cuisines.find().sort("cuisine_name", 1))
    mealtypes = list(mongo.db.types.find().sort("mealtype_name", 1))
    diets = list(mongo.db.diets.find().sort("diet_name", 1))
    return render_template("admin.html", cuisines=cuisines,
                           mealtypes=mealtypes, diets=diets)


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
