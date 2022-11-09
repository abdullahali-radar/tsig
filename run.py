from flask import Flask
from flask import Response
from flask import request
#from flask_ngrok import run_with_ngrok
import json

main = Flask(__name__)
#run_with_ngrok(main)

fileAbout='/aboutProject.json'
f=open(fileAbout)
about=json.load(f)
f.close()

@main.route("/")
def helloWorld():
  return Response(response=json.dumps(about),
                    status=200,
                    mimetype="application/json")

if __name__ == '__main__':
  main.run()