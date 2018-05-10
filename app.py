from flask import Flask

app = Flast(__name__)

@app.route('/')
def hello():
    return 'Hello World!'
