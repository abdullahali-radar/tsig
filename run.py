from flask import Flask
from flask import Response
from flask import request
import json

main = Flask(__name__)

fileAbout='/content/tsig/aboutProject.json'
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