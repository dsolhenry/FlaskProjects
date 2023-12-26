from app.extensions import db
from app.models.user import User as UserModel
from flask import Blueprint, redirect, render_template, request, url_for

bp = Blueprint("user", __name__)

@bp.route('/user/')
def index():
    users = UserModel.query.all()
    return render_template("user/index.html", users=users)

# Add user to the storage database
@bp.route("/user/", methods=["POST"])
def store():
    new_user = UserModel(
        username= request.form['username'],
        email= request.form['email']
    )
    # store user in db
    db.session.add(new_user)
    db.session.commit()
    return redirect(url_for("user.index"))
    

@bp.route("/user/create")
def create():
    return render_template("user/create.html")


@bp.route("/user/delete/<int:id>", methods=["GET", "POST"])
def user_delete(id):
    user = db.get_or_404(UserModel, id)
    if request.method == "POST":
        db.session.delete(user)
        db.session.commit()
        return render_template("user/index.html", user=user)
    return redirect(url_for("user.index"))


@bp.route("/user/<int:id>")
def user_detail(id):
    user = db.get_or_404(UserModel, id)
    return render_template("user/detail.html", user=user)