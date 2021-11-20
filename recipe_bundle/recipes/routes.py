from flask import (flash, render_template, redirect,
                   request, url_for, Blueprint, session)
from bson.objectid import ObjectId
from recipe_bundle import mongo
from recipe_bundle.util import util

# Create blueprint for recipes object
recipes = Blueprint('recipes', __name__)


@recipes.route("/")
@recipes.route("/collection")
def collection():
    """
    Creates recipe collection page, displaying recipes in DB
    :return: rendertemplate of collection.html
    """
    # Check if user is logged in
    if "user" not in session:
        return redirect(url_for("auth/signin"))
    # collects all recipes in collection
    recipes = list(mongo.db.recipes.find())
    # renders template
    return render_template("recipes/collection.html", recipes=recipes)


@recipes.route("/view_recipe/<recipe_id>")
def view_recipe(recipe_id):
    sel_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template("recipes/view_recipe.html", recipe=sel_recipe)


@recipes.route("/add_recipe", methods=["GET", "POST"])
def add_recipe() -> object:
    """
    Adds recipe to MongoDB with add_recipe form information
    :return redirect to (recipe) collection page
    """
    # Check if a user is signed in
    if 'user' not in session:
        return redirect(url_for("auth.signin"))

    if request.method == "POST":
        try:
            # Store the recipe image file in AWS S3
            img_url = util.upload_img('recipe_img')
        except Exception:
            img_url = "https://ms3recipebundle.s3.eu-central-1.amazonaws.com/placeholder.png"

    if request.method == "POST":
        try:
            ingr_list = request.form.getlist("ingr-list")
            method_list = request.form.getlist("method-list")
            # Create recipe object from form
            recipe = {
                "recipe_name": request.form.get("recipe_name"),
                "cuisine": request.form.get("cuisine"),
                "type": request.form.get("mealType"),
                "diet": request.form.get("diet"),
                "ingredients": ingr_list,
                "method": method_list,
                "total_time": request.form.get("total_time"),
                "active_time": request.form.get("active_time"),
                "recipe_img": img_url,
                "creator": session["user"]
            }
            # Add recipe to MongoDB
            mongo.db.recipes.insert_one(recipe)
            flash("Recipe successfully added")
        except Exception as e:
            flash("An error has occurred while adding recipe - " +
                  getattr(e, 'message', repr(e)))
        # Redirect to view recipe page
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


@recipes.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("search-col")
    recipes = list(mongo.db.recipes.find({"$text": {"$search": query}}))
    return render_template("recipes/collection.html", recipes=recipes)
