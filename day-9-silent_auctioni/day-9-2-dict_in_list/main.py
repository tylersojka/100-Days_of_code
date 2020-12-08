travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇

def add_new_country(country_name, num_visits, city_names):
    travel_dict = {}

    travel_dict["country"] = country_name
    travel_dict["visits"] = num_visits
    travel_dict["cities"] = city_names
    travel_log.append(travel_dict)


#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
