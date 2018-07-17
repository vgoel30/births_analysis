from pprint import pprint
import csv
import json

data = {}

def csv_dict_reader(file_obj):
	reader = csv.DictReader(file_obj, delimiter=',')
	#year,month,date_of_month,day_of_week,births
	for line in reader:
		year = int(line['year'])
		month = int(line['month'])
		date = int(line['date_of_month'])
		day = int(line['day_of_week'])
		births = int(line['births'])

		if year not in data:
			data[year] = {}
		if month not in data[year]:
			data[year][month] = {}
		data[year][month][date] = {}
		data[year][month][date]['day'] = day
		data[year][month][date]['births'] = births	


def csv_reader(file_obj):
	reader = csv.reader(file_obj)
	for row in reader:
		print(" ".join(row))

data_dir = '../data/'
file1 = '1994_2003.csv'
file2 = '2000_2014.csv'

filename = data_dir + file1

with open(filename) as file:
	csv_dict_reader(file)

filename = data_dir + file2

with open(filename) as file:
	csv_dict_reader(file)

pprint(data[2013][11])

out_file = data_dir + 'data.json'

with open(out_file, 'w') as outfile:
    json.dump(data, outfile,sort_keys = True, indent = 4,)