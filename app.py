from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "20227 Balamurugan Welocome To  ROSA Application!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
