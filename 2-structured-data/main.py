#!/usr/bin/env python
from pprint import pprint as pp
from flask import Flask, flash, redirect, render_template, request, url_for, Response
from weather import query_api
from bs4 import BeautifulSoup
import json

app = Flask(__name__)

LOCALHOSTURL = "http://localhost:5000/"

@app.route('/', methods = ['POST', 'GET'])
def index():
    # if request.method == 'POST':
    #   mylocation = request.form['mylocation']
    #   return redirect(url_for('result',locString = mylocation))
    # else:
    #   mylocation = request.args.get('mylocation')
    #   return redirect(url_for('result',locString = mylocation))
    return render_template('weather.html',
        data=[{"coord": {"lon": 42.351318, "lat": -71.1090176}}])

@app.route("/result" , methods=['GET', 'POST'])
def result():
    data = []
    error = None
    location = str(request.form.get('finalLocation'))

    print("\nLOCATION IS: " + str(location) + "\n")

    locList = location.split(" ")

    # if request.method == 'POST':
    #     mylocation = request.form('mylocation')
    #     print("MY LOCATION STRING IS: " + str(mylocation))
    #webpage = requests.get(LOCALHOSTURL)

    #soup = BeautifulSoup(htmlString, 'html.parser')

    #method3 = soup.find("div", {"name":"mylocation text-body"})

    #print("HERE IS METHOD 3: " + str(method3) + "\n")

    lat = locList[0]
    lon = locList[1]

    #TESTING LATITUDE AND LONGITUDE
    #lat = 30.234
    #lon = -90.245651

    resp = query_api(lat, lon)
    #print(coordTuple)
    pp(resp)
    if resp:
        data.append(resp)
    if len(data) != 2:
        error = 'Bad Response from Weather API'
    return render_template('result.html',data=data,error=error)

if __name__=='__main__':
    app.run(debug=True)