from flask import Flask
app = Flask(__name__)

@app.route('/')
def home_page():
    return "This is the home page"

@app.route('/beta')
def beta():
    return "This is the beta version"

if __name__=='__main__':
    app.run(debug=True)