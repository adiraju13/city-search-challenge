# city-search-challenge

The public facing website can be found here: https://citysearchapp.herokuapp.com/

**Accepts post requests to the following routes:**

/closest-neightbors 

>> Format: {'geo_id': 'id', 'neighbors':'num_of_neighbors'}

/search

>> Format: {'search': 'query'}


**Approach**

For search of the k nearest neighbors to a geo-id, I implemented a method that computes distance from a location to all other locations, and then orders these locations in a list by the distance away they are. I then store this list in a HashMap of geo-id to the location distances. I save this information, so if there is a query again for the same geo-id, I can skip the computation of the distances.


For search query handling, I search each row of the dataframe to see if the search query exists as a substring under the field of name or alternate_names.



NOTE: Because of time limitations, I cut some corners on the API. Basically, I return a string representation of the results directly to the front end. If I were to have more time, I would have had the functions return lists of locations/lists of search results, and have another function take those lists and convert them into the front end facing representations. 

