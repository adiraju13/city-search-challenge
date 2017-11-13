from CityInformation import CityInformation
from flask import Flask
app = Flask(__name__)
c = CityInformation()

@app.route('/')
def home_page():
    return "This is the home page"

@app.route('/beta')
def beta():
    return "This is the beta version"

if __name__=='__main__':
    app.run(debug=True)