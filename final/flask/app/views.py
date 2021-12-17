from flask import request, jsonify
from app import app
from app.model import get_emoji


@app.route('/', methods=['POST', 'GET'])
def home():
    default_text = ''
    if request.method == 'POST':
        text = request.form.get('text', default_text)
    else:
        text = request.args.get('text', default_text)

    return jsonify({'emoji': get_emoji(text)})
