#!/usr/bin/env python
from pprint import pprint as pp
from flask import Flask, flash, redirect, render_template, request, url_for, Response
from weather import query_api
import sqlalchemy
import config
import json

app = Flask(__name__)
app.config.from_object(config)

cloud_sql_connection_name = "bookshelfproject-252519:northamerica-northeast1:mydb"

LOCALHOSTURL = "http://localhost:5500/"

# The SQLAlchemy engine will help manage interactions, including automatically
# managing a pool of connections to your database
db = sqlalchemy.create_engine(
    # Equivalent URL:
    # mysql+pymysql://<db_user>:<db_pass>@/<db_name>?unix_socket=/cloudsql/<cloud_sql_instance_name>
    sqlalchemy.engine.url.URL(
        drivername='mysql+pymysql',
        username='root',
        password='28',
        database='SeniorDesignMiniDB',
        query={
            'unix_socket': '/cloudsql/{}'.format(cloud_sql_connection_name)
        }
    ),
    # ... Specify additional properties here.
    # ...
)

@app.route('/', methods = ['POST', 'GET'])
def index():
    humidityArray = []
    temperatureArray = []
    with db.connect() as conn:
        myData = conn.execute(
            "SELECT * FROM mySensors;").fetchall()
        # Convert the results into a list of dicts representing votes
        for row in myData:
            humidityArray.append(row[0])
            temperatureArray.append(row[1])

    # for point in dataArray:
    #     print(point)
    # if request.method == 'POST':
    #   mylocation = request.form['mylocation']
    #   return redirect(url_for('result',locString = mylocation))
    # else:
    #   mylocation = request.args.get('mylocation')
    #   return redirect(url_for('result',locString = mylocation))
    return render_template('index.html', humidityData=humidityArray, tempData=temperatureArray)

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

    try:
        lat = locList[0]
        lon = locList[1]
    except IndexError:
        print("\nInvalid location. Defaulting coordinates.\n")
        lat = 42.3510312
        lon = -71.1087235

    resp = query_api(lat, lon)
    #print(coordTuple)
    pp(resp)
    if resp:
        data.append(resp)
    if len(data) != 2:
        error = 'Bad Response from Weather API'
    return render_template('result.html',data=data,error=error)

if __name__=='__main__':
    app.run(debug=True, port=5500)