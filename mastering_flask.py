from flask import Flask
from config import DevelopConfig

app = Flask(__name__)
app.config.from_object(DevelopConfig)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
