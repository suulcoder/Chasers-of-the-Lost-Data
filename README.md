#Data Chaser
Data Chaser is a library that autocompletes the empty fields in a csv file. Data Chaser use Artifitial Intelignece based 
on multiple regressions, updating the values based un the uncertanty of the regressions to get the new updated values and
uncertainties. 

## Getting Started 🚀

This script was develop in Python and uses Pandas, Numpy, Sklearn and CSV python libraries there are three important files:
  
	```
	Install Python 3.6 or a newer version
	Intall Pip
	```

### Prerequisites 📋

You´ll need to install using pip install command: 


```
pip install pandas
pip install pandas
pip install numpy
pip install DataChaser
```

You must use pip3 instead of pip. 

## Running⚙️

Import Library and run it.


## Build With 🛠️

Sublime Text and LINUX MINT

## Documentation

	
To start with DataChaser you must instantiate a class after import the library
	
	'''
	DataChaser = Chaser({Path of the input File} ,{Path of the output File})
	'''
	
Then run the following methods of the class:

	'''
		DataChaser.trainDataBuilder()
		DataChaser.getDataToChase()
		DataChaser.LinearRegression()
		DataChaser.store()
	'''


