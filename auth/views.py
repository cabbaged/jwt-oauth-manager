from flask import Blueprint, flash

from auth.validators import UserSchema, validate_schema
from auth.models import User
from auth.database import db_session
from auth.exceptions import InvalidUsage

from sqlalchemy.exc import IntegrityError

blueprint = Blueprint('auth', __name__)


@blueprint.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@blueprint.route("/auth")
def auth():
    return "Hi, want to auth?"

@blueprint.route("/token")
def token():
    return "your token"

@blueprint.route("/register", methods=['POST'])
@validate_schema(UserSchema())
def register(username, password, email):
    user = User(username=username,
                password=password,
                email=email)

    try:
        db_session.add(user)
        db_session.commit()
    except IntegrityError:
        raise InvalidUsage.user_already_registered()

    return user

@blueprint.route("/users")
def users():
    users = db_session.query(User).all()
    print(users)
    return str(users)
