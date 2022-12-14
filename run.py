from flask import Flask
from flask import Response
from flask import request
#from flask_ngrok import run_with_ngrok
import json

main = Flask(__name__)
#run_with_ngrok(main)

fileAbout='./aboutProject.json'
fileKI='./ki_jateng.geojson'
fileRH='./rh_jateng.geojson'
fileMSLP='./mslp_jateng.geojson'
fileTP='./tp_jateng.geojson'

def openJSON(file):
  with open(file) as f:
    content=json.load(f)
  return content

@main.route("/")
def helloWorld():
  about=openJSON(fileAbout)
  return Response(response=json.dumps(about),
                    status=200,
                    mimetype="application/json")

@main.route("/ki")
def displayKI():
  ki=openJSON(fileKI)
  return Response(response=json.dumps(ki),
                    status=200,
                    mimetype="application/json")

@main.route("/rh")
def displayRH():
  rh=openJSON(fileRH)
  return Response(response=json.dumps(rh),
                    status=200,
                    mimetype="application/json")

@main.route("/mslp")
def displayMSLP():
  mslp=openJSON(fileMSLP)
  return Response(response=json.dumps(mslp),
                    status=200,
                    mimetype="application/json")

@main.route("/tp")
def displayTP():
  tp=openJSON(fileTP)
  return Response(response=json.dumps(tp),
                    status=200,
                    mimetype="application/json")

@main.route("/query")
def returnQuery():
  parameter = request.args.get('parameter')
  nilai = request.args.get('nilai')
  operator = request.args.get('operator')
  
  fileOpen=f"./{parameter}_jateng.geojson"
  variabel=openJSON(fileOpen)
  features=variabel["features"]
  
  if operator=='lebihdari':
    dataquery = [p for p in features if p["properties"]["value"] > int(nilai)]
  elif operator=='kurangdari':
    dataquery = [p for p in features if p["properties"]["value"] < int(nilai)]
  elif operator=='samadengan':
    dataquery = [p for p in features if p["properties"]["value"] == int(nilai)]

    
  return Response(response=json.dumps(dataquery),
                    status=200,
                    mimetype="application/json")
              

if __name__ == '__main__':
  main.run()