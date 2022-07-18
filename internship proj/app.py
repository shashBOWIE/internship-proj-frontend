@@ -0,0 +1,75 @@
from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

import json

from data import neighborhoods
from data import data

neighboRet = []
holdingInfo = []


@app.route('/', methods=['GET', 'POST'])
def home():
   if request.method == 'POST':
       if request.form['submit_button'] == 'secOpiAdd':
           open('sample.json', 'w').close()
           holdingInfo.clear()
           pythonTran = []
           neighboRet.clear()
           pythonTran.clear()
           pythonTran = request.form.getlist('myCheckbox')
           pythonTran.append(request.form.get('thirdForm'))
           pythonTran.append(request.form.get('secForm'))
           pythonTran.append(request.form.get('exampleForm'))
           pythonTran = list(map(int, pythonTran))
           exec(open("webscraper.py").read())
           print(pythonTran)
           
        #Create Recommendations ===========================
           for key, values in neighborhoods.items():
                if pythonTran[-1] == 1 and values[0] == 1:
                    stoVal1 = len(set(pythonTran).intersection(values))
                    if stoVal1 >= 2:
                        neighboRet.append(key)
                if pythonTran[-1] == 2 and values[0] == 2:
                    stoVal1 = len(set(pythonTran).intersection(values))
                    if stoVal1 >= 2:
                        neighboRet.append(key)
                if pythonTran[-1] == 3 and values[0] == 3:
                    stoVal1 = len(set(pythonTran).intersection(values))
                    if stoVal1 >= 2 :
                        neighboRet.append(key)

           for community in neighboRet:
                raw_data = data[community][0]
                json_str = json.dumps(raw_data, indent=4, sort_keys=True)
                resp = json.loads(json_str)
                holdingInfo.append(resp)
                with open("sample.json", "a") as outfile:
                    outfile.write(json_str)

           outfile.close()
           #datan = [json.loads(line) for line in open('sample.json', 'r')]
           #print(datan)
           return redirect(url_for('second'))

   return render_template('index.html', holdingInfo = holdingInfo)

@app.route('/finale')
def second():
    return render_template('other.html', finalList = holdingInfo)

@app.route('/map')
def third():
    return render_template('my_map1.html', finalList = holdingInfo)
@app.route('/about')
def aboutt():
    return render_template('aboutus.html', finalList = holdingInfo)



if __name__ == '__main__':
   app.debug = True
   app.run()
