from app import app
from flask import Flask, jsonify
import requests
import urllib
import json
from urllib.request import urlopen

@app.route('/')
@app.route('/index')
def index():
    return 'Welcome'

@app.route('/pokemon/<variable>', methods = ['GET']) 

def pokemon(variable):
 	r = requests.get("http://pokeapi.co/api/v2/pokemon/" + variable)
 	if(variable.isdigit()):
 		return  "The pokemon with id " + variable +" is " +json.dumps(r.json()['forms'][0]['name']).strip('\"')
 	else:
 		return variable + " has id " + json.dumps(r.json()['forms'][0]['url'][-2]).strip('\"')

if __name__ == '__main__':
	app.run(debug=True)

