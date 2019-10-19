# Data Chaser
Data Chaser is a library that autocompletes empty fields in a csv file. Data Chaser uses Artifitial Intelignece based 
on multiple regressions, updating the values based un the uncertanty of the regressions to get the new updated values and
ranges. 

## Getting Started 🚀

This script was develop in Python and uses Pandas, Numpy, Sklearn and CSV python libraries there are three important files:
  	'''
	Install Python 3.6 or a newer version
	Intall Pip
	'''

### Prerequisites 📋

You´ll need to install using pip3 install command: 
```
pip3 install pandas
pip3 install pandas
pip3 install numpy
pip install -i https://test.pypi.org/simple/ DataChaser
```

## Running ⚙️

Import Library and run it.


## Build With 🛠️

Sublime Text and LINUX MINT

## Documentation

	
To start with DataChaser you must instantiate a class after import the library
	
	DataChaser = Chaser({Path of the input File} ,{Path of the output File})
	
Then run the following methods of the class:

		DataChaser.trainDataBuilder()
		DataChaser.getDataToChase()
		DataChaser.LinearRegression()
		DataChaser.store()

Check your output file, and remember that while more information your input file has, the library is better. 
