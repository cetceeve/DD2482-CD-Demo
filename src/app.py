import os
from flask import Flask, jsonify, render_template
from flask_cors import CORS

template_directory = os.path.abspath('src/templates')
static_directory = os.path.abspath('src/static')

app = Flask(__name__, template_folder=template_directory,
            static_folder=static_directory)
CORS(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_url', methods=['GET'])
def get_url():
    # hardcoded_url = "https://github.com/cetceeve/DD2482-CD-Demo/tree/main"
    hardcoded_url = "https://duckduckgo.com/"
    return jsonify({"url": hardcoded_url})


HOST = '0.0.0.0'
# Testing IP

# 192.168.0.106
# 130.229.178.24

if __name__ == '__main__':
    app.run(host=HOST, port=5000)
