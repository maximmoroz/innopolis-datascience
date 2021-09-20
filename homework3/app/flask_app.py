# Загружаем билиотеки
import flask
from flask import Flask, flash, request, redirect, url_for, send_from_directory
import pandas as pd
import requests
import json
import os
import numpy as np
from werkzeug.utils import secure_filename

# Задаем имя серверу
app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False
app.config['UPLOAD_FOLDER'] = '/content/'
ALLOWED_EXTENSIONS = {'png', 'jpeg'}


# Загрузка модели
def predict_model(x):
    return [1 if (i[1] / i[2]) > (i[3] / i[4]) - (i[5] ** 2) + (i[6] ** 2) else 0 for i in x]


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/uploads/<name>')
def download_file(name):
    return send_from_directory(app.config['UPLOAD_FOLDER'], name)


@app.route('/web', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('download_file', name=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''


# Задаем функцию Predict
@app.route("/predict", methods=["GET", "POST"])
def predict():
    data = {"success": False}
    params = None
    if flask.request.is_json:
        params = flask.request.get_json()

    if params is None:
        params = flask.request.args

    # Если параметры найдены, создаем из них Pandas DataFrame
    if params is not None:
        print(params)
        x = pd.DataFrame.from_dict(params, orient='index').transpose().astype('int').values
    else:
        return flask.jsonify(data)

    # Записываем значение prediction в data["prediction"]
    data["prediction"] = predict_model(x)
    # Записываем статус в data["success"]
    data["success"] = True

    # Возвращаем результат json format
    return flask.jsonify(data)


@app.route("/train", methods=["GET", "POST"])
def retraining():
    if flask.request.method == 'POST':

        x = json.loads(flask.request.json)['train_x']
        y = json.loads(flask.request.json)['train_y']
        return flask.jsonify({'x': x})  # "mnist_new.h5"
    else:
        return "Method should be POST"


# Запускаем Сервер
if __name__ == '__main__':
    app.run()
