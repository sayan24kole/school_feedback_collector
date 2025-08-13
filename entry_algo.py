#suppose I have name and code
from flask import Flask, request, render_template, redirect, url_for
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('stdlogin.htm')
@app.route('/process_login', methods = ['POST'])
def process_login():
    name = request.form['name']
    code = request.form['code']
    k = 0
    with open('student_names.txt','r') as f:
        while True:
            each_line = f.readline()
            if not each_line:
                break
            std_name = each_line.split(',')[0]
            std_id = each_line.split(',')[1]
            if(std_name.strip() == name and std_id.strip() == code):
                k = 1
                break
            else:
                k = 0
    if(k == 1):
        return redirect(url_for('main_page1'))
    elif(k == 0):
        return f"Invalid"
@app.route('/main_page')
def main_page1():
    return render_template('main_page.htm')
   
@app.route('/go')
def go():
    return redirect(url_for('main_page1'))


if __name__ == '__main__':
    app.run(debug=True)
    
