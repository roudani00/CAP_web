from flask import Flask, render_template, request, redirect, url_for



app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


#'oejwf

@app.route('/members', methods=['GET','POST'])
def mem():
    if request.method == 'POST':
        return render_template('member.html')
    return render_template('member.html')

@app.route('/Why', methods=['GET','POST'])
def why():
    if request.method == 'POST':
        return render_template('why.html')
    return render_template('why.html')

@app.route('/data' , methods= ['GET','POST'])
def data():
    if request.form.get('action') == 'anr':
        with open('anr_data.txt') as anr:
            data = anr.readlines()
            data = [s.replace('\n', ' ') for s in data]
            data = ''.join(data)
            print(data)
            return data




@app.route('/test')
def test():
    return render_template('test.html')

if __name__ == "__main__":
    app.run(port= 5001,debug=True)

