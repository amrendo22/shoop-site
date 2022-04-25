from flask import Flask, render_template
from camera2.py from Main

app = Flask(__name__)
#GPIO.setmode(GPIO.BCM)
#GPIO.setwarning(False)
@app.route('/')

def hello():
    templateData = {
        'Title': 'Hello'}
    return render_template('index.html', **templateData)

#@app.route("/SHOOPS/camera2.py", methods = ['POST'])
@app.route("/results", methods=['POST', "GET"])
def run_app():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')
