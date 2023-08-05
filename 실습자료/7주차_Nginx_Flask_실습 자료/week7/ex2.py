from flask import Flask
app = Flask(__name__)

@app.route('/')  # default URL
def hello_world():
   return ('Hello World!')

@app.route('/page')  # page URL
def print_page():
    return ('This is page')

if __name__ == '__main__':
   app.run()
