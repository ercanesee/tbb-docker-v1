from flask import Flask
import os
app = Flask(__name__)


@app.route('/')

def hello_world():
    envtest = os.getenv('ortam')
    return '<h2> Hello,TBB Ortam : ' +  envtest + '</h2>'

if __name__ == '__main__':
    app.run()