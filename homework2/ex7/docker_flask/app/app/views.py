from flask import request
from app import app


@app.route('/', methods=['POST', 'GET'])
def home():
    default_name = 'world'
    if request.method == 'POST':
        name = request.form.get('name', default_name)
    else:
        name = request.args.get('name', default_name)
    return "hello {}!".format(name)
