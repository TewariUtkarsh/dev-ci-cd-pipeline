from flask import Flask, render_template, Request, jsonify
from flask_cors import CORS, cross_origin
# from wsgiref import simple_server


app = Flask(__name__)
CORS(app)


@app.route("/", methods=['POST', 'GET'])
@cross_origin()
def index():

    return "Just a Development Environment!!!"


if __name__ == '__main__':

    app.run(debug=True)