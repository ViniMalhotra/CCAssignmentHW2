from __future__ import print_function

import pandas as pd
from flask import Flask, request
import json
from flask import abort
from datetime import datetime
import datetime as dt

app = Flask(__name__)

@app.route('/historical/', methods=["GET","POST"])
def get_alldates():
    global dataset
    dataset = pd.read_csv("daily.csv")
    #Returns all the dates for which weather information is available
    if request.method == "GET":
        weather_list = []
        for i in range(dataset.shape[0]):
            entry = {'DATE':str(dataset['DATE'][i])}
            weather_list.append(entry)
            
        print("Returning %s results" % str(dataset.shape[0]))
        return json.dumps(weather_list)
    
    #Adds a new date, tmax and tmin entry to the dataset
    if request.method == "POST":
        recvData = str(request.get_data(), 'utf-8')
        data = json.loads(recvData)
        d = {'DATE' : int(data["DATE"]), 'TMAX' : data["TMAX"], 'TMIN' : data["TMIN"]}
        print("IN POST INSERT")
        print(d)
        new_df = pd.DataFrame(data=d, columns=['DATE','TMAX','TMIN'], index=[dataset.shape[0]])
        dataset = dataset.append(new_df)
        entry = {'DATE':data["DATE"]}
        print(entry)
        return json.dumps(entry), 201
    return "ERROR"

@app.route('/forecast/<dateYYYYMMDD>', methods=["GET"])
def get_forecast(dateYYYYMMDD):
    global dataset 
    #Get forecast for next seven days
    todaysDate = datetime.strptime(dateYYYYMMDD,'%Y%m%d')
    forecast_df = pd.DataFrame(columns=['DATE','TMAX','TMIN'])
    d = {'DATE' : dateYYYYMMDD, 'TMAX' : 34.0, 'TMIN' : 20.0}
    print(d)
    forecast_df = forecast_df.append(d,ignore_index=True)
    for i in range(1,7):
        nextDay = todaysDate + dt.timedelta(days = i)
        print(nextDay)
        dateStr = datetime.strftime(nextDay, '%Y%m%d')
        print(dateStr)
        d = {'DATE' : dateStr, 'TMAX' : ((34.0 * 5) + i)/5  , 'TMIN' : ((20.0 * 5) + i)/5}
        print(d)
        forecast_df = forecast_df.append(d,ignore_index=True)
    
    print(forecast_df)
    return forecast_df.to_json(orient = "records")

@app.route('/historical/<dateYYYYMMDD>', methods=["GET","DELETE"])
def get_details_per_date(dateYYYYMMDD):
    global dataset
    #Get details of a particular date
    print(dateYYYYMMDD)
    param = int(dateYYYYMMDD)
    if request.method == "GET":
        new_result = dataset[dataset["DATE"] == param]
        print(new_result)
        if new_result.empty:
            return abort(404)
        formatted_result = {"DATE":str(int(new_result["DATE"])),"TMAX":int(new_result["TMAX"]),"TMIN":int(new_result["TMIN"])}
        print(formatted_result)
        return json.dumps(formatted_result)
    #Delete Entry for a particular date
    elif request.method == "DELETE":
        print("In Delete")
        dataset = dataset[dataset["DATE"] != param]
        return "Record for %s deleted" % dateYYYYMMDD
    return "Failure"
    
if __name__ == '__main__':   
    app.run()
        




