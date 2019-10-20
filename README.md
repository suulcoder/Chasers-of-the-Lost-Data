# Data Chaser
Data Chaser is a library that autocompletes empty fields in a csv file. Data Chaser uses Artifitial Intelignece based 
on multiple regressions, updating the values based un the uncertanty of the regressions to get the new updated values and
ranges.In order to fill the empty fields we noticed that regressions have uncertainty, and base on the uncertainty of differents regressions of the different categories of the csv we made a neural network to get the information

```
  Name: DataChaser
  Format: .py
  Autors: 
    -Saúl Contreras (SuulCoder)
    -Luis Quezada (Lfquezada)
    -Marco Fuentes
    
  Use: 

    This program is useful to recover the data that has been lost by
    some sensors of the Nasa. This is a proyect for the SpaceApp 
    Challege 2019. This algorithm uses a Machine Learning
    process, libraries from Python and statistics regressions. 
```


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
pip3 install --user -i https://test.pypi.org/simple/ DataChaser
```


## Running ⚙️

Import Library and run it.
```
import DataChaser
```


## Build With 🛠️

Sublime Text and LINUX MINT

## Documentation

	
To start with DataChaser you must instantiate a class after import the library
	
		Import DataChaser
		DataChaser = Chaser({Path of the input File} ,{Path of the output File})
	
Then run the following methods of the class:

```
 	#You must run this methods if you want the chaser to work
	DataChaser.trainDataBuilder()
    	DataChaser.getDataToChase()
    	
	#Here starts the regressions you are able to delete all
    	#those that does not work with your data
   	DataChaser.LinearRegression()
    	DataChaser.cubicRegression()
    	DataChaser.quadraticRegression()
    
    	#This methods will write a new document in the output file
    	DataChaser.store()
```

Check your output file, and remember that while more information your input file has, the library is better. 

## Background

CSV files have multiple categories. Each category depends on the other ones (sometimes they doesn't). With this we can determine a regression that satisfies both categories. For example if in our data we have distance x and time t, the returned regression must be a linear one with the velocity as scope. But sometimes the regressions aren't linear. Furthermore we can say that each regression has uncertainty

With this concept we can develop a model for a neural network where each neuron receives three entries:

            Value:The current possible value of the empty field.

            Low limit: The difference between the value and the uncertainty, its the lowest number that the value can have in the empty field.

            Up limit: The sum between the value and the uncertainty, its the highest number that the value can have in the empty field

Each time that you add a new possible value and a new possible uncertainty, the model merge between the current possible value and current uncertainty to get an accurate one.


How it works?


When you have two possible values and uncertainties based on different regressions. You will have two possible situations:

There is an interception between both uncertainties:

The uncertainty becomes smaller so it will be reduce, and the new possible value will be in the middle of both limits.

There is no interception between the uncertainties:

If there is no interception the new uncertainty will become the union of both uncertainties, so it becomes bigger.


how to improve the algorithm?


Each time the uncertainty become smaller it starts reaching zero. When the uncertainty becomes zero the returned data is 100% correct, but when the uncertainty becomes greater the given value is getting even lost.

To overcome this error, you must leave in the CSV all the categories that you are sure that have a relation. Then the uncertainty starts getting smaller and smaller each time.

Other way to improve the algorithm is to add more regression models, or if you know how the categories are related you must just chose that regression

