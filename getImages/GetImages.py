import json
import os

mode = input("val/test?")
file_source = ""
if (mode=="val"):
	file_source = '../data/nocaps/annotations/nocaps_val_image_info.json'
else:
	file_source = '../data/nocaps/annotations/nocaps_test_image_info.json'

url=""
ID =""
with open(file_source) as json_file:
	data = json.load(json_file)
	for image in data['images']:
		url = image['coco_url']
		ID = image['id']
		command = 'wget -O '+mode+'/'+str(ID)+'.jpg '+url
		print(command)
		os.system(command)





