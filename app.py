import sqlite3

from flask import Flask, jsonify
import main

app = Flask(__name__)



@app.route('/')
def get_funds():
    # main.main()
    return jsonify({"Hello": "world"})


if __name__ == "__main__":
    app.run()

