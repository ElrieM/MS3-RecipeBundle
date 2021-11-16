from flask import (render_template, Blueprint)

# Create blueprint for admin object
admin = Blueprint('admin', __name__)


@admin.route("/")
@admin.route("/home")
def home() -> object:
    """
    Loads landing / Home page
    :return render_template of index.html
    """
    return render_template("admin/index.html")
