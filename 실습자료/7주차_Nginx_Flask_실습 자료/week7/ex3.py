from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def student():
   return render_template('input_info.html')  ## (1)

@app.route('/result', methods = ['POST', 'GET'])  ## (2) 
def result():
   if request.method == 'POST':  ## (3)
      result = dict()
      result['Name'] = request.form.get('Name')
      return render_template("result.html",result = result)

if __name__ == '__main__':
   app.run()