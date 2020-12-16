from flask import (
    Flask,
    jsonify,
    request
)

app = Flask(__name__)

@app.route("/")
def index():
    # titleがxxのやつを見つけてくる
    return "{'title': 'this is a title', 'content': 'this is content'}"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")