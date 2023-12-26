from flask import Blueprint, redirect, render_template, request, url_for

bp = Blueprint("web", __name__)

@bp.route("/")
def home():
    return render_template('home.html')

@bp.app_errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@bp.app_errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500