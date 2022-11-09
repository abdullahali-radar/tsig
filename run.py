from flask import Flask
from flask import Response
from flask import request
#from flask_ngrok import run_with_ngrok
import json

main = Flask(__name__)
#run_with_ngrok(main)

fileAbout='./aboutProject.json'
fileKI='./ki_clip.geojson'
fileRH='./rh_clip_more70.geojson'
fileMSLP='./mslp_clip.geojson'
fileTP='./tp_clip_more0.geojson'

def openJSON(file):
  with open(fileAbout) as f:
    content=json.load(f)
  return content

@main.route("/")
def helloWorld():
  return Response(response=json.dumps(about),
                    status=200,
                    mimetype="application/json")

@main.route("/ki")
def displayKI():
  ki=openJSON(fileKI)
  return Response(response=json.dumps(ki),
                    status=200,
                    mimetype="application/json")

if __name__ == '__main__':
  main.run()