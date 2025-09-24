cities = {
"Tokyo": {
    "country": "Japan",
    "population": 37400068,  # Approximate metro population
    "fact": "Tokyo is the largest metropolitan area in the world."
},
"Paris": {
    "country": "France",
    "population": 2148000,  # Approximate city proper population
    "fact": "Paris is known as 'The City of Light' because it was one of the "
    "first cities to have street lighting."
}, 
"Cairo": {
    "country": "Egypt",
    "population": 20484965,  # Approximate metro population
    "fact": "Cairo is home to the Great Pyramid of Giza, the only one of "
    "the Seven Wonders of the Ancient World still standing."}}

for city, info in cities.items():
    print(f"{city}\nCountry: {info["country"]}\nPopulation: {info["population"]}\n{info["fact"]}\n")