from flask import *
import os

app=Flask(__name__)


@app.route('/')
def home():
    return render_template('EXTN.html')
@app.route('/coorg')
def h():
    return render_template('coorg.html')
@app.route('/darjeeling')
def ho():
    return render_template('darjeeling.html')
@app.route('/kashmir')
def hom():
    return render_template('kashmir.html')
@app.route('/ladakh')
def homee():
    return render_template('ladakh.html')
@app.route('/munnar')
def homeee():
    return render_template('munnar.html')
@app.route('/nainital')
def hoemeee():
    return render_template('nainital.html')
@app.route('/ooty')
def ehome():
    return render_template('ooty.html')
@app.route('/udaipur')
def hoffme():
    return render_template('udaipur.html')
@app.route('/varanasi')
def homgge():
    return render_template('varanasi.html')

port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)
app.run(debug=True)
