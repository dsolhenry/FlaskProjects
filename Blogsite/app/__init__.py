from flask import Flask, render_template, redirect, url_for, request
from app.blueprints import web


app = Flask(__name__)

app.register_blueprint(web.bp)



