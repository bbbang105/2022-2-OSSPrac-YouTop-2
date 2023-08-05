from flask import Flask
app = Flask(__name__)

@app.route('/')  # default URL
def hello_world():
    return ('Hello World!')

# http://localhost:5000/
if __name__ == '__main__':
   app.run()
   