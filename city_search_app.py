from CityInformation import CityInformation
from flask import Flask, request
app = Flask(__name__)
c = CityInformation()

@app.route('/')
def home_page():
    return """
    <form action="/closest-neighbors" method="post">
    Use this form to search for closest neighbors to a certain geo_id: <br>
    Enter the geo_id: <input type="number" name="geo_id"><br>
    Enter the number of closest points: <input type="number" name="neighbors"><br>
    <input type="submit" value="Submit">
	</form> <br><br><br>
	<form action="/search" method="post">
    Use this form to seach our dataset for city information: <br>
    Enter a single word to search: <input type="text" name="search"><br>
    <input type="submit" value="Submit">
	</form>
	"""

@app.route('/closest-neighbors',  methods=['POST'])
def closest_neighbors():
	return c.get_closest_points(int(request.form['geo_id']), int(request.form['neighbors']))

@app.route('/search',  methods=['POST'])
def search():
	return c.search(request.form['search'])

if __name__=='__main__':
    app.run(debug=False)