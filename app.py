from flask import Flask
import main

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, Azure!'

@app.route('/gw')
def game_week():
    return main.match_data

if __name__ == "__main__":
    app.run()
