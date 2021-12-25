from flask import Flask
from auth.views import blueprint as auth_blueprint
from auth.database import db_session, init_db_command
from auth.exceptions import InvalidUsage

def errorhandler(error):
    response = error.to_json()
    response.status_code = error.status_code
    print('status: ' + str(response.status_code))
    return response


app = Flask(__name__)
app.register_blueprint(auth_blueprint)
app.cli.add_command(init_db_command)
app.errorhandler(InvalidUsage)(errorhandler)


@app.teardown_appcontext
def shutdown_session(exception=None):
    print('hi hello')
    db_session.remove()