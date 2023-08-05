from flask import Flask
app = Flask(__name__)

@app.route('/')  # default URL
def hello_world():
    return ('Hello World!')

# http://localhost:8000/
# 으로 접속해보세요.
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)