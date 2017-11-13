from CityInformation import CityInformation
from flask import Flask, request
app = Flask(__name__)
c = CityInformation()

@app.route('/')
def home_page():
    return """
    <form action="/beta" method="post">
    Enter the geo_id: <input type="number" name="geo_id"><br>
    Enter the number of closest points: <input type="number" name="neighbors"><br>
    <input type="submit" value="Submit">
	</form>
	"""

@app.route('/beta',  methods=['POST'])
def beta():
	return c.get_closest_points(int(request.form['geo_id']), int(request.form['neighbors']))

if __name__=='__main__':
    app.run(debug=False)