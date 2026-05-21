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

@app.route('/dataa' , methods= ['GET','POST'])
def data_anr():
    with open('anr_data.txt') as file:
        data = file.readlines()
        data = [s.replace('\n', ' ') for s in data]
        data = ''.join(data)
        print('a')
        return render_template('profile.html', name1="anr", name2="عبدالعزيز")
@app.route('/datah' , methods= ['GET','POST'])
def data_hanoosh():
    with open('hanoosh_data.txt') as file:
        data = file.readlines()
        data = [s.replace('\n', ' ') for s in data]
        data = ''.join(data)
        print('a')
        return data
@app.route('/datad' , methods= ['GET','POST'])
def data_dawood():
    with open('dawood_data.txt') as file:
        data = file.readlines()
        data = [s.replace('\n', ' ') for s in data]
        data = ''.join(data)
        print('a')
        return data
@app.route('/dataf' , methods= ['GET','POST'])
def data_fjr():
    with open('fjr_data.txt') as file:
        data = file.readlines()
        data = [s.replace('\n', ' ') for s in data]
        data = ''.join(data)
        print('a')
        return data







if __name__ == "__main__":
    app.run(port= 5001,debug=True)

