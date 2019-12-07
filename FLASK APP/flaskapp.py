from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "<h1><marquee>HELLO WORLD</marquee></h1>"

@app.route('/home')
def home():
    return "<h1><marquee>HOME PAGE</marquee></h1>"

if __name__=='__main__':
    app.run(debug=True)
