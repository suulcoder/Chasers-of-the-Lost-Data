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

import csv

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

# Parsed info of the csv's
meteorLandings = dataParser('Meteorite_Landings.csv')
printData(meteorLandings)

fireballAndBolideReports = dataParser('FireBall_And_Bolide_Reports.csv')
printData(fireballAndBolideReports)

GLC03122015 = dataParser('GLC03122015.csv')
printData(GLC03122015)

NearEarthCometsOrbitalElements = dataParser('Near-Earth_Comets_-_Orbital_Elements.csv')
printData(NearEarthCometsOrbitalElements)

