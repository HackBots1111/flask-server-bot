from weather import Weather, Unit

def result(query):
	weather = Weather(unit= Unit.CELSIUS)
	location = weather.lookup_by_location(query)
	condition = location.condition
	return condition.text















