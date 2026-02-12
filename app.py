from flask import Flask
from fetch_data import fetch_publications

app = Flask(__name__)

@app.route("/")
def home():
    publications = fetch_publications("0000-0002-1825-0097")
    return "<br>".join(publications)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
