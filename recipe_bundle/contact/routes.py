from flask import (render_template, Blueprint)

# Create blueprint for contact object
cont = Blueprint('cont', __name__)


@cont.route("/")
@cont.route("/contact")
def contact():
    """
    Loads contact page with contact form.
    Contact form sends email via EmailJS SDK
    :return render_template of contact.html
    """
    return render_template("cont/contact.html")
