from flask import (render_template, Blueprint)

# Create blueprint for error object
err = Blueprint('err', __name__)


@err.errorhandler(404)
def error_404(e: object) -> object:
    """
    Displays 404 error page when page not found
    :return render_template of 404.html
    """
    return render_template('err/404.html'), 404
