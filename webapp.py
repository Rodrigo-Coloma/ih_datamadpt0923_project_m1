from subprocess import run
from flask import Flask
from flask import render_template
from flask import request
import os

print('webapp launched')
app = Flask(__name__)
@app.route('/',methods= ['POST','GET'])
def index(name=None):
    if request.method == 'POST':
        input = request.form
        if os.path.exists('./templates/route_map.html'):
            os.remove('./templates/route_map.html')
        run(['python','./main.py', '-r','-e', f"{input['email']}", '-s', f"{input['start']}", '-f', f"{input['finish']}", '-p', f"{input['monuments']}"],capture_output=True,text=True)
        try:
            return render_template('route_map.html',name=name)
        except:
            return render_template('map-error.html')
    else:
        return render_template('base.html',name=name)

app.run(host='0.0.0.0', port=8080,debug=True)