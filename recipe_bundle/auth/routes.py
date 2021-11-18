from flask import (flash, render_template, redirect,
                   request, session, url_for, Blueprint)
from werkzeug.security import generate_password_hash, check_password_hash
from bson.objectid import ObjectId
from recipe_bundle import mongo

# Create blueprint for auth object
auth = Blueprint('auth', __name__)


@auth.route("/")
@auth.route("/register", methods=["GET", "POST"])
def register() -> object:
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

        # confirm email not already in DB
        existing_email = mongo.db.users.find_one(
            {"email": request.form.get("email")})
        # if email exists, notify user and reload register page
        if existing_email:
            flash("Email already exists, please sign in instea")
            return redirect(url_for("auth.register"))

        # if username and email don't exist, register user in Users collection
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
def signin() -> object:
    """
    Checks user exists, compares passwords and signs user in
    if correct. Lands on Collection page.
    If incorrect, user is taken back to sign in page.
    :return render_template of collection page
    """
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


@auth.route("/reset", methods=["GET", "POST"])
def reset() -> object:
    """
    Checks email address exists in database before resetting
    password on database with new input.
    :return: updates db password and redirects to sign in page
    """
    if request.method == "POST":
        # searches email address in db
        email_exists = mongo.db.users.find_one(
            {"email": request.form.get("r_email")})
        # find object id
        user_id = email_exists['_id']

        if email_exists:
            # New password
            updatedpw = {
                "password": generate_password_hash(
                    request.form.get("new_password"))
            }
        try:
            mongo.db.users.update({"_id": ObjectId(user_id)}, updatedpw)
        except Exception as e:
            flash("An error occurred when updating password: " +
                  getattr(e, 'message', repr(e)))
        else:
            # Message if username not found
            flash("Email not found, please try again")
            return redirect(url_for("auth.signin"))

    return render_template("auth/reset.html")


@auth.route("/signout")
def signout() -> object:
    """
    Signs out user from the site and returns sign in page
    :return render_template signin page
    """
    # Removes user from session cookies
    session.pop('user')
    flash("Signed out successful")
    return redirect(url_for("auth.signin"))
