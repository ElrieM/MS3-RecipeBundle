from flask import (render_template, Blueprint)

# Create blueprint for error object
from recipe_bundle import app
errors = Blueprint('errors', __name__)


@app.errorhandler(404)
def error_404(error: object) -> object:
    """
    Displays 404 error page when page not found
    :return render_template of 404.html
    """
    return render_template('errors/404.html', error=error), 404


@app.errorhandler(400)
def error_400(error: object) -> object:
    """
    Displays 400 error page server cannot or will not process the
    request due to an apparent client error
    :return render_template of 400.html
    """
    return render_template('errors/400.html', error=error), 400


@app.errorhandler(500)
def error_500(error: object) -> object:
    """
    Displays 500 error page when unexpected condition
    was encountered and no more specific message
    :return render_template of 500.html
    """
    return render_template('errors/500.html', error=error), 500
