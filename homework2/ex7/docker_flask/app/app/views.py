from flask import request
from app import app


@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        name = request.form.get('name', 'world')
    else:
        name = request.args.get('name', 'world')
    return "hello {}!".format(name)
