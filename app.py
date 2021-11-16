import os
from recipe_bundle import create_app

# Create app
app = create_app()

# Run app
if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
