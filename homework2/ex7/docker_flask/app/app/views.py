from flask import request
from app import app


@app.route('/')
def home():
    name = request.args.get('name', 'world')
    return "hello {}!".format(name)
