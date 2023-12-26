from app.blueprints import user, web
from flask import Flask, request
from app.extensions import db


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
db.init_app(app)

app.register_blueprint(web.bp)
app.register_blueprint(user.bp)

with app.app_context():
    db.create_all()