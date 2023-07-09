import json

def readJson():
	with open("../user/settings.json", "r") as settings:
		data = json.load(settings)

	expression = data["expression"]

	xmin = data["graphvalues"]["xmin"]
	xmax = data["graphvalues"]["xmax"]
	ymin = data["graphvalues"]["ymin"]
	ymax = data["graphvalues"]["ymax"]

	grid = data["appearance"]["grid"]

	return (expression, xmin, xmax, ymin, ymax, grid)

def writeJson(expression, xmin, xmax, ymin, ymax, grid):
	settings = {
		"expression" : expression,

		"graphvalues" : {
			"xmin" : xmin,
			"xmax" : xmax,
			"ymin" : ymin,
			"ymax" : ymax
		},

		"appearance" : {
			"grid" : grid
		}
	}

	with open("../user/settings.json", "w") as outfile:
		json.dump(settings, outfile)