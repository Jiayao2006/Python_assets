from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello NYP SIT DBFT"

if __name__ == "__main__":
    app.run() # method of flask class