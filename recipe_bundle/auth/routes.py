from flask import (flash, render_template, redirect,
                   request, session, url_for, Blueprint)
from werkzeug.security import generate_password_hash, check_password_hash
from recipe_bundle import mongo

# Create blueprint for auth object
auth = Blueprint('auth', __name__)


@auth.route("/")
@auth.route("/register", methods=["GET", "POST"])
def register():
    """
    Creates new user, adds user information to MongoDB Users collection,
    creates login session and redirects to (recipe) collection page with
    a flash message welcoming the user.
    If the username already exists, registration page is reloaded and
    a flash message shown to notify user.
    Passwords are encrypted and stored.
    :return render_template of collection
    """
    if request.method == "POST":
        # confirm username not already in DB
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username")})
        # if username exists, notify user and reload register page
        if existing_user:
            flash("Username already exists, please try again")
            return redirect(url_for("auth.register"))
        # if username doesn't exist, registers user details in Users collection
        register = {
            "username": request.form.get("username"),
            "email": request.form.get("email"),
            "password": generate_password_hash(request.form.get("password"))
        }
        try:
            mongo.db.users.insert_one(register)
            # store new user in 'session' cookie
            session["user"] = request.form.get("username")
            flash("Welcome, {}".format(request.form.get("username")))
        except Exception as e:
            flash("An error occurred when adding new user: " +
                  getattr(e, 'message', repr(e)))
        return redirect(url_for("recipes.collection",
                                username=session["user"]))

    return render_template("auth/register.html")


@auth.route("/signin", methods=["GET", "POST"])
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
                return redirect(url_for("recipes.collection",
                                username=session["user"]))
            else:
                # Message if password incorrect
                flash("Credentials do not match, please try again")
                return redirect(url_for("auth.signin"))

        else:
            # Message if username not found
            flash("Credentials do not match, please try again")
            return redirect(url_for("auth.signin"))

    return render_template("auth/signin.html")


@auth.route("/signout")
def signout():
    session.pop('user')
    flash("Sign out successful")
    return redirect(url_for("auth.signin"))
