
from flask import Flask
import mausam
import Market_price
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from flask import jsonify


app = Flask(__name__)


@app.route('/<name>')
def hello(name):
	return name

@app.route('/api/weather/<query>')
def Weather(query):
	res = mausam.result(query)
	return res

@app.route('/api/price/<query>')
def Price(query):
	res = Market_price.result(query)
	return res

 

if __name__ == '__main__':
	app.run(debug=True)