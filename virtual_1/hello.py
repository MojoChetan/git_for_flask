from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    z='test'
    return z