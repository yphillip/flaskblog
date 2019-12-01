import os
from flaskblog import create_app

DEBUG_VALUE = (os.environ.get('DEBUG_VALUE') == "True")

app = create_app()
if __name__ == "__main__":
    app.run(debug=DEBUG_VALUE)

