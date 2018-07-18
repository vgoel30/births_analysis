import json
import csv
from pprint import pprint
import pandas as pd
import math
import numpy as np; np.random.seed(0)
import matplotlib.pyplot as plt
import os
from math import log as ln

def get_year_distribution(datafile, year):
	year = str(year)
	with open(datafile) as f:
		data = json.load(f)
		data_year = data[year]

		if plot:
			births = {month:0 for month in data_year}
			for month in data_year:
				month_births = 0
				month_data = data_year[month]
				for date in month_data:
					month_births += month_data[date]['births']
				births[month] = month_births
			
			births = {int(month): births[month]/100000 for month in births}
			lists = sorted(births.items()) # sorted by key, return a list of tuples
			x, y = zip(*lists) # unpack a list of pairs into two tuples
			plt.plot(x, y,marker='o')
			plt.xlabel('Year')
			plt.ylabel('Births in hundred thousand')
			plt.title('Monthly births in the year ' + str(year))
			plt.ylim([2.5,4])
			plt.show()			

def get_yearly_births(datafile, plot=False):
	births = {str(i):0 for i in range(1994, 2015)}

	with open(datafile) as f:
		data = json.load(f)
		
		for year in data:
			year_births = 0
			year_data = data[year]
			for month in year_data:
				month_data = year_data[month]
				for day in month_data:
					year_births += int(month_data[day]['births'])

			births[year] = year_births

	if plot:
		sum = 1000000
		births = {year:births[year]/sum for year in births}

		lists = sorted(births.items()) # sorted by key, return a list of tuples
		x, y = zip(*lists) # unpack a list of pairs into two tuples
		plt.plot(x, y,marker='o')
		plt.xlabel('Year')
		plt.ylabel('Births in million')
		plt.title('Yearly births in USA')
		plt.ylim([3.1,5])
		plt.show()
	
	return births

def get_combined_monthly_births(datafile):
	births = {str(i):0 for i in range(1, 13)}

	with open(datafile) as f:
		data = json.load(f)

		for year in data:
			year_data = data[year]
			for month in year_data:
				month_births = 0
				month_data = year_data[month]
				for date in month_data:
					month_births += month_data[date]['births']
				births[month] += month_births
	pprint(births)

	births = {int(month): births[month]/1000000 for month in births}
	lists = sorted(births.items()) # sorted by key, return a list of tuples
	x, y = zip(*lists) # unpack a list of pairs into two tuples
	plt.plot(x, y,marker='o')
	plt.xlabel('Month')
	plt.ylabel('Births in million')
	plt.title('Total births in a month across 1994-2014')
	plt.ylim([6,8])
	plt.show()

def get_combined_day_births(datafile):
	births = {i:0 for i in range(1, 367)}
	births = {month:{} for month in range(1, 13)}

	with open(datafile) as f:
		data = json.load(f)

		for year in data:
			year_data = data[year]
			for month in year_data:
				month_data = year_data[month]
				for date in month_data:
					if int(date) not in births[int(month)]:
						births[int(month)][int(date)] = 0
					births[int(month)][int(date)] += month_data[date]['births']
	pprint(births)

	# births = {month: births[month]/100000 for month in births}
	# lists = births.items() # sorted by key, return a list of tuples
	# x, y = zip(*lists) # unpack a list of pairs into two tuples
	# plt.plot(x, y)
	# plt.xlabel('Day')
	# plt.ylabel('Births in hundred thousand')
	# plt.title('Total births on a day across 1994-2014')
	# #plt.ylim([6,8])
	# plt.show()

plot = True

data_dir = '../data/'
datafile = data_dir + 'data.json'
# year_births = get_yearly_births(datafile, plot=plot)
# pprint(year_births)
#get_yearly_births(datafile, plot)
#get_year_distribution(datafile, 2009)
get_combined_day_births(datafile)
