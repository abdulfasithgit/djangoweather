from django.shortcuts import render

def home(request):
	import json
	import requests

	if request.method == 'POST':
		zipcode = request.POST['zipcode']
		print(zipcode)
		api_request = requests.get("http://www.airnowapi.org/aq/forecast/zipCode/?format=application/json&zipCode="+ zipcode +"&date=2020-03-12&distance=5&API_KEY=4B4BC65A-4394-45A1-8AB4-BC77A069E7E3");
		try:
			api = json.loads(api_request.content);
		except Exception as e:
			api ="error"
		
		if  api[0]["Category"]["Name"] == 'Good':
			category_description = "Air quality is considered satisfactory, and air pollution poses little or no risk."
			category_color = "good";
		elif api[0]["Category"]["Name"] == 'Moderate':
			category_description = "Air quality is acceptable; however, for some pollutants there may be a moderate health concern for a very small number of people who are unusually sensitive to air pollution."
			category_color = "moderate";
		elif api[0]["Category"]["Name"] == 'Unhealthy for Sensitive Groups':
			category_description = "Although general public is not likely to be affected at this AQI range, people with lung disease, older adults and children are at a greater risk from exposure to ozone, whereas persons with heart and lung disease, older adults and children are at greater risk from the presence of particles in the air."
			category_color = "usg";
		elif api[0]["Category"]["Name"] == 'Very Unhealthy':
			category_description = "Health alert: everyone may experience more serious health effects."
			category_color = "unhealthy";
		elif api[0]["Category"]["Name"] == 'Hazardous':
			category_description = "Health warnings of emergency conditions. The entire population is more likely to be affected."
			category_color = "hazardous";
		
		return render(request, "home.html", {
			"api": api, 
			'category_description': category_description,
			'category_color': category_color
			})
	else:
		api_request = requests.get("http://www.airnowapi.org/aq/forecast/zipCode/?format=application/json&zipCode=90001&date=2020-03-12&distance=5&API_KEY=4B4BC65A-4394-45A1-8AB4-BC77A069E7E3");
		try:
			api = json.loads(api_request.content);
		except Exception as e:
			api ="error"
		
		if  api[0]["Category"]["Name"] == 'Good':
			category_description = "Air quality is considered satisfactory, and air pollution poses little or no risk."
			category_color = "good";
		elif api[0]["Category"]["Name"] == 'Moderate':
			category_description = "Air quality is acceptable; however, for some pollutants there may be a moderate health concern for a very small number of people who are unusually sensitive to air pollution."
			category_color = "moderate";
		elif api[0]["Category"]["Name"] == 'Unhealthy for Sensitive Groups':
			category_description = "Although general public is not likely to be affected at this AQI range, people with lung disease, older adults and children are at a greater risk from exposure to ozone, whereas persons with heart and lung disease, older adults and children are at greater risk from the presence of particles in the air."
			category_color = "usg";
		elif api[0]["Category"]["Name"] == 'Very Unhealthy':
			category_description = "Health alert: everyone may experience more serious health effects."
			category_color = "unhealthy";
		elif api[0]["Category"]["Name"] == 'Hazardous':
			category_description = "Health warnings of emergency conditions. The entire population is more likely to be affected."
			category_color = "hazardous";
		
		return render(request, "home.html", {
			"api": api, 
			'category_description': category_description,
			'category_color': category_color
			})

def about(request):
	return render(request, "about.html", {})
