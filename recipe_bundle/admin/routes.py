from flask import (render_template, Blueprint)

# Create blueprint for admin object
admin = Blueprint('admin', __name__)


@admin.route("/")
@admin.route("/home")
def home() -> object:
    """
    Loads landing / home page
    :return render_template of admin.html
    """
    return render_template("admin/index.html")


@admin.route("/terms")
def terms() -> object:
    """
    Loads terms from register page
    :return render_template of terms.html
    """
    return render_template("admin/terms.html")
