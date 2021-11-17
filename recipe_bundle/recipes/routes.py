from flask import (flash, render_template, redirect,
                   request, url_for, Blueprint)
from bson.objectid import ObjectId
from recipe_bundle import mongo

# Create blueprint for recipes object
recipes = Blueprint('recipes', __name__)


@recipes.route("/")
@recipes.route("/collection")
def collection():
    recipes = list(mongo.db.recipes.find())
    return render_template("recipes/collection.html", recipes=recipes)


@recipes.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("search-col")
    recipes = list(mongo.db.recipes.find({"$text": {"$search": query}}))
    return render_template("recipes/collection.html", recipes=recipes)


@recipes.route("/select_recipe/<recipe_id>")
def select_recipe(recipe_id):
    sel_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template("recipes/view_recipe.html", recipe=sel_recipe)


@recipes.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    ingr_list = request.form.getlist("ingr-list")
    method_list = request.form.getlist("method-list")

    if request.method == "POST":
        recipe = {
            "recipe_name": request.form.get("recipe_name"),
            "cuisine": request.form.get("cuisine"),
            "type": request.form.get("mealType"),
            "diet": request.form.get("diet"),
            "ingredients": ingr_list,
            "method": method_list,
            "total_time": request.form.get("total_time"),
            "active_time": request.form.get("active_time")
        }
        mongo.db.recipes.insert_one(recipe)
        flash("Recipe added")
        return redirect(url_for("recipes.collection"))

    cuisines = mongo.db.cuisines.find().sort("cuisine_name", 1)
    mealtypes = mongo.db.types.find().sort("mealtype_name", 1)
    diets = mongo.db.diets.find().sort("diet_name", 1)
    return render_template("recipes/add_recipe.html", cuisines=cuisines,
                           mealtypes=mealtypes, diets=diets)


@recipes.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    if request.method == "POST":
        submit = {
            "recipe_name": request.form.get("recipe_name"),
            "cuisine": request.form.get("cuisine"),
            "type": request.form.get("mealType"),
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
    return render_template("recipes/edit_recipe.html", cuisines=cuisines,
                           mealtypes=mealtypes, diets=diets,
                           recipe=update_recipe)


@recipes.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    flash("Recipe successfully deleted")
    return redirect(url_for("recipes.collection"))
