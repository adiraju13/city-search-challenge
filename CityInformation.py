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
		#precompute the distances before the server starts up so that 
		#querying for the closest neighbors is quick
		self.setup_distances()

	def setup_distances(self):
		for row in self.data.itertuples():
			self.order_other_locations(row.Index, row.latitude, row.longitude)


	def order_other_locations(self, index_of_interest, lat1, lon1):
		distances = []
		for row in self.data.itertuples(index=True):
			if row.Index != index_of_interest:
				distance = self.distance_between_points(lat1, lon1, row.latitude, row.longitude)
				distances.append([row.Index, distance])
		
		self.distance_between_locations[index_of_interest] = sorted(distances, key=operator.itemgetter(1))

	def get_closest_points(self, geo_id, k):
		resulting_string = ""
		for i in range(0, k):
			resulting_string += self[self.distance_between_locations[geo_id][i][0]]["name"] + " " + self.distance_between_locations[geo_id][i][1] + " km away\n"

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