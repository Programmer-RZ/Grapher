import json

def readJson():
	with open("user/settings.json", "r") as settings:
		data = json.load(settings)

	expression = data["expression"]

	xmin = data["graphvalues"]["xmin"]
	xmax = data["graphvalues"]["xmax"]
	ymin = data["graphvalues"]["ymin"]
	ymax = data["graphvalues"]["ymax"]

	theme = data["appearance"]["theme"]
	grid = data["appearance"]["grid"]

	return (expression, xmin, xmax, ymin, ymax, theme, grid)

def writeJson(expression, xmin, xmax, ymin, ymax, theme, grid):
	settings = {
		"expression" : expression,

		"graphvalues" : {
			"xmin" : xmin,
			"xmax" : xmax,
			"ymin" : ymin,
			"ymax" : ymax
		},

		"appearance" : {
			"theme" : theme,
			"grid" : grid
		}
	}

	with open("user/settings.json", "w") as outfile:
		json.dump(settings, outfile)