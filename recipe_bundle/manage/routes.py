from flask import (flash, render_template,
                   redirect, request, url_for, Blueprint)
from bson.objectid import ObjectId
from recipe_bundle import mongo
from recipe_bundle.util import util

# Create blueprint for manage object
manage = Blueprint('manage', __name__)


@manage.route("/admin")
def admin():
    cuisines = list(mongo.db.cuisines.find().sort("cuisine_name", 1))
    mealtypes = list(mongo.db.types.find().sort("mealtype_name", 1))
    diets = list(mongo.db.diets.find().sort("diet_name", 1))
    return render_template("manage/admin.html", cuisines=cuisines,
                           mealtypes=mealtypes, diets=diets)


@manage.route("/add_diet", methods=["GET", "POST"])
def add_diet():
    if request.method == "POST":
        new_diet = {
            "diet_name": request.form.get("diet_name")
        }
        mongo.db.diets.insert_one(new_diet)
        flash("New diet option added")
        return redirect(url_for("manage.admin"))

    return render_template("manage/add_diet.html")


@manage.route("/edit_diet/<diet_id>", methods=["GET", "POST"])
def edit_diet(diet_id):
    if request.method == "POST":
        submit = {
            "diet_name": request.form.get("diet_name")
        }
        mongo.db.diets.update({"_id": ObjectId(diet_id)}, submit)
        flash("Diets successfully updated")
        return redirect(url_for("manage.admin"))

    diet = mongo.db.diets.find_one({"_id": ObjectId(diet_id)})
    return render_template("manage/edit_diet.html", diet=diet)


@manage.route("/delete_diet/<diet_id>", methods=["GET", "POST"])
def delete_diet(diet_id):
    mongo.db.diets.remove({"_id": ObjectId(diet_id)})
    flash("Diets successfully removed")
    return redirect(url_for("manage.admin"))


@manage.route("/add_mealtype", methods=["GET", "POST"])
def add_mealtype():
    if request.method == "POST":
        new_mealtype = {
            "mealtype_name": request.form.get("mealtype_name")
        }
        mongo.db.types.insert_one(new_mealtype)
        flash("New meal type option added")
        return redirect(url_for("manage.admin"))

    return render_template("manage/add_mealtype.html")


@manage.route("/edit_mealtype/<mealtype_id>", methods=["GET", "POST"])
def edit_mealtype(mealtype_id):
    if request.method == "POST":
        submit = {
            "mealtype_name": request.form.get("mealtype_name")
        }
        mongo.db.types.update({"_id": ObjectId(mealtype_id)}, submit)
        flash("Meal type successfully updated")
        return redirect(url_for("manage.admin"))

    mealtype = mongo.db.types.find_one({"_id": ObjectId(mealtype_id)})
    return render_template("manage/edit_mealtype.html", mealtype=mealtype)


@manage.route("/delete_mealtype/<mealtype_id>", methods=["GET", "POST"])
def delete_mealtype(mealtype_id):
    mongo.db.types.remove({"_id": ObjectId(mealtype_id)})
    flash("Meal type successfully removed")
    return redirect(url_for("manage.admin"))


@manage.route("/add_cuisine", methods=["GET", "POST"])
def add_cuisine():
    if request.method == "POST":
        new_cuisine = {
            "cuisine_name": request.form.get("cuisine_name")
        }
        mongo.db.cuisines.insert_one(new_cuisine)
        flash("New cuisine option added")
        return redirect(url_for("manage.admin"))

    return render_template("manage/add_cuisine.html")


@manage.route("/edit_cuisine/<cuisine_id>", methods=["GET", "POST"])
def edit_cuisine(cuisine_id):
    if request.method == "POST":
        submit = {
            "cuisine_name": request.form.get("cuisine_name")
        }
        mongo.db.cuisines.update({"_id": ObjectId(cuisine_id)}, submit)
        flash("Cuisine successfully updated")
        return redirect(url_for("manage.admin"))

    cuisine = mongo.db.cuisines.find_one({"_id": ObjectId(cuisine_id)})
    return render_template("manage/edit_cuisine.html", cuisine=cuisine)


@manage.route("/delete_cuisine/<cuisine_id>", methods=["GET", "POST"])
def delete_cuisine(cuisine_id):
    mongo.db.cuisines.remove({"_id": ObjectId(cuisine_id)})
    flash("Cuisine successfully removed")
    return redirect(url_for("manage.admin"))
