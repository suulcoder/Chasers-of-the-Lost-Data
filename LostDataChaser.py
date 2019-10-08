"""
-------------------------------------------------------------------------------
	

	Name: Chasers of the lost data
	Format: .py
	Autors: 
		-Saúl Contreras (SuulCoder)
		-Luis Quezada (Lfquezada)
		-Marco Fuentes
		-Justin Trigueros
		-Jonathan Pu

	Use: 

		This program is useful to recover the data that has been lost by
		some sensors of the Nasa. This is a proyect for the SpaceApp 
		Challege 2019. This algorithm uses a Machine Learning
		process, libraries from Python and statistics regressions. 


-------------------------------------------------------------------------------
"""
#Import all libraries
import csv
import numpy as np
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
#------------------------------------------------------------------------------


#FUNCTIONS:

# given a csv file, returns an array with each event/object in a dictionary with all it's elements named
def dataParser(fileName):
	data = []
	with open(fileName) as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		line = 0
		for row in csv_reader:
			objInfo = {}
			if line == 0:
				titles = row
			else:
				for i in range(len(row)):
					objInfo[titles[i]] = row[i]
				data.append(objInfo)
			line += 1
		print(f'{line} events processed.')
		return data

def printData(data):
	for event in data:
		for title,info in event.items():
			print(f'{title}: {info}')
		print('\n')

#------------------------------------------------------------------------------
imp = IterativeImputer(max_iter=10, random_state=0)
imp.fit([[1, 2], [3, 6], [4, 8], [np.nan, 3], [7, np.nan]])  
IterativeImputer(add_indicator=False, estimator=None,
                 imputation_order='ascending', initial_strategy='mean',
                 max_iter=10, max_value=None, min_value=None,
                 missing_values=nan, n_nearest_features=None,
                 random_state=0, sample_posterior=False, tol=0.001,
                 verbose=0)
X_test = [[np.nan, 2], [6, np.nan], [np.nan, 6]]
 # the model learns that the second feature is double the first
 print(np.round(imp.transform(X_test)))


# Parsed info of the csv's

fireballAndBolideReports = dataParser('Fireball_And_Bolide_Reports.csv')
printData(fireballAndBolideReports)

"""
meteorLandings = dataParser('Meteorite_Landings.csv')
printData(meteorLandings)

GLC03122015 = dataParser('GLC03122015.csv')
printData(GLC03122015)

NearEarthCometsOrbitalElements = dataParser('Near-Earth_Comets_-_Orbital_Elements.csv')
printData(NearEarthCometsOrbitalElements)

"""