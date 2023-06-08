import json

def readJson(data):
	expression = data["expression"]

	xmin = data["graphvalues"]["xmin"]
	xmax = data["graphvalues"]["xmax"]
	ymin = data["graphvalues"]["ymin"]
	ymax = data["graphvalues"]["ymax"]

	theme = data["appearance"]["theme"]
	grid = data["appearance"]["grid"]

	return (expression, xmin, xmax, ymin, ymax, theme, grid)

def openJson():
	with open("user/settings.json", "r") as settings:
		data = json.load(settings)
	
	return data