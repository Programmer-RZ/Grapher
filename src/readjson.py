import json

with open("user/settings.json", "r") as settings:
	data = json.load(settings.read())