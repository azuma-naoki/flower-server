from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np
import sqlite3

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
CORS(app)

@app.route("/")
def hello_world():
    return "<p> Welcome FlowerServer!</p>"

# @app.route("/emotion/<int:emotion_id>", methods=['GET'])
# def emorion(emotion_id):

#     emotion = emotion_id

#     connection = sqlite3.connect('flower.db')

#     result = connection.execute(f'''
#     select name.name, genus_label.name, mean.mean
#     from name, mean, genus_label
#     where name.par_id=mean.par_id and name.chi_id=mean.chi_id and genus_label.id=mean.par_id and lab_id = {emotion};
#     ''')


#     flower = [
#         {'name':row[0], 'par_name':row[1], 'mean':row[2]}
#         for row in result
#     ]

#     return jsonify(flower)

# @app.route("/flower/<string:flower>", methods=['GET'])
# def flower(flower):

#     f_name = flower
#     print(f_name)

#     connection = sqlite3.connect('flower.db')

#     result = connection.execute(f'''
#     select name.chi_id, name.chi_name,  mean.mean
#     from name, mean, genus_label
#     where name.par_id=mean.par_id and name.chi_id=mean.chi_id and genus_label.id=mean.par_id and genus_label.name="{f_name}";
#     ''')

#     flower = {}
#     for row in result:
#         if(row[1] not in flower):
#             flower[row[1]] = []
#         flower[row[1]].append(row[2])

#     return jsonify(flower)