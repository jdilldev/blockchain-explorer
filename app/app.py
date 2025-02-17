from flask import Flask

app = Flask(__name__)

@app.route("/balance/<address>")
def hello_world(address):
    print('do it')
    return address