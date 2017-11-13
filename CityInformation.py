import pandas as pd
from math import sin, cos, sqrt, atan2, radians
import operator


class CityInformation:
	#read the data in from the file into a dataframe
	def __init__(self):
		self.data = pd.read_table('cities1000.txt')
		self.data.columns = ['geo_id', 'name', 'ascii_name', 'alternate_names', 
						'latitude', 'longitude', 'feature_class', 'feature_code', 
						'country_code', 'cc2', 'admin1code', 'admin2code',
						'admin3code', 'admin4code', 'population', 'elevation',
						'dem', 'timezone', 'mod_date']

		self.data.set_index('geo_id', inplace=True)

		#dictionary of geo_id to ordered list of areas by distance
		self.distance_between_locations = {}

	def search(self, search_query):
		search_query = search_query.encode('utf-8')
		resulting_string = "Here are your search results (although we search across alternate names as well, only master names are shown): <br><br>"
		for row in self.data.itertuples(index=True):
			#takes care of jagged edges
			if (isinstance(row.name, str) and row.name.find(search_query) != -1) or (isinstance(row.alternate_names, str) and row.alternate_names.find(search_query) != -1):
				resulting_string += "Geo_id: " + str(row.Index) + " Master Name: " + row.name + " Latitude: " + str(row.latitude) + " Longitude: " + str(row.longitude) + "<br>"
		return resulting_string


	def order_other_locations(self, index_of_interest, lat1, lon1):
		distances = []
		for row in self.data.itertuples(index=True):
			if row.Index != index_of_interest:
				distance = self.distance_between_points(lat1, lon1, row.latitude, row.longitude)
				distances.append([row.Index, distance])
		
		self.distance_between_locations[index_of_interest] = sorted(distances, key=operator.itemgetter(1))

	def get_closest_points(self, geo_id, k):
		resulting_string = ""
		if geo_id not in self.data.index:
			return "This geo_id is not valid! We do not have information on it"

		# add a caching layer so that things we do not recompute distances!
		if geo_id not in self.distance_between_locations.keys():
			self.order_other_locations(geo_id, self.data.loc[geo_id]["latitude"], self.data.loc[geo_id]["longitude"])

		resulting_string += "The " + str(k) + " closest places to geo_id " + str(geo_id) + " are:<br><br>" 
		#add the info we want to display to the output string
		for i in range(0, k):
			resulting_string += self.data.loc[self.distance_between_locations[geo_id][i][0]]["name"] + " " + str(self.distance_between_locations[geo_id][i][1]) + " km away<br>"

		return resulting_string
		
	#This equation determines the distance between two coordinates
	def distance_between_points(self, lat1, lon1, lat2, lon2):
		R = 6373.0

		#convert to radians
		lat1 = radians(lat1)
		lon1 = radians(lon1)
		lat2 = radians(lat2)
		lon2 = radians(lon2)

		dlon = lon2 - lon1
		dlat = lat2 - lat1

		a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
		c = 2 * atan2(sqrt(a), sqrt(1 - a))

		distance = R * c
		return distance