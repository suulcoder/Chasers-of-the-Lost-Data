"""
-------------------------------------------------------------------------------
	

	Name: TensorFlowTest
	Format: .py
	Autors: 
		-Saúl Contreras (SuulCoder)
		-Luis Quezada (Lfquezada)
		-Marco Fuentes

	Use: 

		This program is useful to learn how does TensorFlow works

-------------------------------------------------------------------------------
"""
#Import all libraries
from __future__ import absolute_import, division, print_function, unicode_literals
import functools
import numpy as np
import tensorflow as tf

"""
This function is to get all the data that is useful to train the model 
"""
def trainDataBuilder(filename,name):
	data = []
	titles = []
	with open(fileName) as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		line = 0
		for row in csv_reader:
			if(line==0):
				titles = row
			else:
				data.append(row)
			line+=1
	with open(name, mode='w') as data_file:
		data_file = csv.writer(data_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		data_file.writerow(titles)
		for currentData in data:
			data_file.writerow(currentData)
	return "Check " + name + " for the train data"

trainData = 'trainData.csv'    #You must write the name of the doc you want. 
print(trainDataBuilder('Fireball_And_Bolide_Reports.csv',trainData))
train_file_path = tf.keras.utils.get_file(trainData, TRAIN_DATA_URL)
