# REST API Markdown

##### URL : https://roshanvin4u.pythonanywhere.com 

### 1. URL/historical/

Returns json data of all the dates for which the weather data is available.

* Method : `GET`

* URL Params : `NONE`

* Data Params : `NONE`

* Success Response:
  * Code : `200`
    Content : `{"DATE" : "20130101",
               "DATE" : "20130102"}`
* Sample Call:
  * `requests.get(URL+'/historical/')`
  
### 2. URL/historical/

Inserts a new weather data.

* Method : `POST`

* URL Params : `NONE`

* Data Params : `'{"DATE":"20180601","TMIN":33,"TMAX":44}'`

* Success Response:
  * Code : `201`
  * Content : `{"DATE": "20180601"}`
  
* Sample Call:
  * `requests.post("URL/historical/", data='{"DATE":"20180601","TMIN":33,"TMAX":44}')`
  
### 3. URL/historical/

Gets the weather data for a specific date.

* METHOD : `GET`

* URL Params : `<dateYYYYMMDD> = '20180601'`

* Data Params : `NONE`

* Success Response:
  * Code : `200`
  * Content : `{"DATE": "20180601", "TMAX": 44, "TMIN": 33}`
  
* Error response:
  * Code : 404
  * Content : `<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
               <title>404 Not Found</title>
               <h1>Not Found</h1>
               <p>The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.</p>`
  
* Sample Call:
  * `requests.get("URL/historical/20180601")`
  
### 4. URL/historical/

Deletes a particular entry based on the date that has been passed.

* METHOD : `DELETE`

* URL Params : `<dateYYYYMMDD> = '20180601'`

* Data Params : `NONE`

* Success Response:
  * Code : `200`
  * Content : `Record for 20180601 deleted`
  
* Sample Call:
  * `requests.delete("URL/historical/20180601")`
  
### 5. URL/forecast/

Gets the forecast for the next 7 days.

* METHOD : `GET`

* URL Params : `<dateYYYYMMDD> = '20180601'`

* Data Params : `NONE`

* Success Response:
  * Code : `200`
  * Content : `{"DATE":"20180601","TMAX":34.0,"TMIN":20.0},
               {"DATE":"20180602","TMAX":34.2,"TMIN":20.2},
               {"DATE":"20180603","TMAX":34.4,"TMIN":20.4},
               {"DATE":"20180604","TMAX":34.6,"TMIN":20.6},
               {"DATE":"20180605","TMAX":34.8,"TMIN":20.8},
               {"DATE":"20180606","TMAX":35.0,"TMIN":21.0},
               {"DATE":"20180607","TMAX":35.2,"TMIN":21.2}`
  
* Sample Call:
  * `requests.delete("URL/forecast/20180601")`
