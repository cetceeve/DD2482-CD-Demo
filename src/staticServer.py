from flask import Flask, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/health')
def health():
  return "OK"

@app.route('/get_url', methods=['GET'])
def get_url():
    google_url = "https://www.google.com"
    return jsonify({"url": google_url})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
