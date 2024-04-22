from flask import Flask, render_template
from sqlalchemy import table, text

app = Flask(__name__)

@app.route('/')

def index():
    return render_template('base.html')


if __name__ == '__main__':
    app.run(debug=True)