from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    html="""
    <html>
    <head>
        <style>
        
            div{
                width: 320px;
                background-color: rgba(173, 216, 230, 0.3);
                padding: 25px 30px;
                border-radius: 12px;
                box-shadow: 0 4px 10px rgba(0,0,0,0.9);
                margin: 80px auto 120px auto;
            }
            h1{
                text-align: center;
                margin-top: 30px;
                text-decoration: underline;
                font-weight: bold;
                color: #000000; 
                text-shadow:
                0 0 5px #ff005d,
                0 0 10px #ff005d,
                0 0 20px #ff005d,
                0 0 40px rgba(232,54,86,1);
            }
            leora{
                display: block;
                margin-bottom: 8px;
                font-weight: 600;
                font-size: 18px;
                color: #590B31; 
                text-shadow:
                0 0 5px #118DBF,
                0 0 10px #118DBF,
                0 0 20px #118DBF,
                0 0 40px rgba(232,54,86,1);
            }
        </style>
    </head>
    <body bgcolor='black'>
        <img src="https://www.dgicommunications.com/wp-content/uploads/2023/01/college-classroom-design-ideas.jpg"width="100%" height="100%" style="position: fixed; top: 0; left: 0; z-index: -1;">
        <div><h1>Name of our teachers</h1></div>
        <div><leora>
        """
    with open('teacher_names.txt','r') as f:
        while True:
            line = f.readline()
            if not line:
                break
            html += f"<li>{line}</li>"
    html +="""
    </leora></div>
    </body>
    </html>"""
    return html
if __name__ == '__main__':
    app.run(port=5050, debug=True)
        