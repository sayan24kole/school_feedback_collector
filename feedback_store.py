#suppose i have teacher's name and feedback.
from flask import Flask, request, render_template, redirect, url_for
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('main_page.htm')
@app.route('/process_feedback', methods = ['POST'])
def process_feedback():
    name = request.form['teach']
    feedback = request.form['feedback']
    with open('teacher_names.txt','r') as f:
        while True:
            each_line = f.readline()
            if not each_line:
                break
            if(name == each_line.strip()):
                with open(f'C:\Users\sayan\OneDrive\Desktop\feedback collector\teacher\{each_line}_teach.txt','a') as k:
                    k.write(f'{feedback}\n')
                    return render_template('main_page.htm')
            
@app.route('/main_page')
def main_page1():
    return render_template('main_page.htm')
   
@app.route('/go')
def go():
    return redirect(url_for('main_page1'))


if __name__ == '__main__':
    app.run(debug=True)
        