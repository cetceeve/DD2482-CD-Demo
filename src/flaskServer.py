from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/get_url', methods=['GET'])
def get_url():
    url = request.args.get('url')
    if not url:
        return jsonify({"error": "Missing url"}), 400

    return jsonify({"url": url})


if __name__ == "__main__":
    app.run(host='localhost', port=8080)
