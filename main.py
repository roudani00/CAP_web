from flask import Flask, render_template, request, redirect, url_for



app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')



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
        intrest = ["Robotics","Mechatronics","Control Systems","Aerodynamics"]
        projects = ["Dielectric Barrier Discharge (DBD) active flow control","Inverted pendulum control using AI"]
        head = " ذلِكَ فَضْلُ اللَّهِ يُؤْتِيهِ مَنْ يَشاءُ وَاللَّهُ واسِعٌ عَلِيمٌ"
        print('a')
        return render_template('profile.html', name1="Abdulaziz Al Roudan", name2="عبدالعزيز الروضان",
                               intrest=intrest, projects=projects, slogen=head, img="static/assets/anr.png")
@app.route('/datah' , methods= ['GET','POST'])
def data_hanoosh():
    with open('hanoosh_data.txt') as file:
        data = file.readlines()
        data = [s.replace('\n', ' ') for s in data]
        data = ''.join(data)
        print('a')
        return render_template('profile.html', name1="hanoosh", name2="عبدالعزيز")
@app.route('/datad' , methods= ['GET','POST'])
def data_dawood():
    with open('dawood_data.txt') as file:
        data = file.readlines()
        data = [s.replace('\n', ' ') for s in data]
        data = ''.join(data)
        print('a')
        return render_template('profile.html', name1="dawod", name2="عبدالعزيز")
@app.route('/dataf' , methods= ['GET','POST'])
def data_fjr():
    with open('fjr_data.txt') as file:
        data = file.readlines()
        data = [s.replace('\n', ' ') for s in data]
        data = ''.join(data)
        print('a')
        return render_template('profile.html', name1="fjr", name2="عبدالعزيز")







if __name__ == "__main__":
    app.run(port= 5001,debug=True)

