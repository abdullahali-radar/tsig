from flask import Flask

main = Flask(__name__)

@main.route("/")
def helloWorld():
  return 'Hello World Flask!'

if __name__ == '__main__':
  main.run()