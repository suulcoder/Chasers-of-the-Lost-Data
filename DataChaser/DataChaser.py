"""
-------------------------------------------------------------------------------
  
  Name: DataChaser
  Format: .py
  Autors: 
    -Saúl Contreras (SuulCoder)
    -Luis Quezada (Lfquezada)
    -Marco Fuentes
'Fireball_And_Bolide_Reports.csv'
  Use: 

    This program is useful to recover the data that has been lost by
    some sensors of the Nasa. This is a proyect for the SpaceApp 
    Challege 2019. This algorithm uses a Machine Learning
    process, libraries from Python and statistics regressions. 

-------------------------------------------------------------------------------
"""
#Import all libraries

import pandas as pd #import the pandas module
import numpy as np
import csv
from sklearn.linear_model import LinearRegression

#------------------------------------------------------------------------------

class Value(object):
  """This class represents a value that has uncertainty. 
    The objective for this class is to reduce the 
    uncertainty based on differnt models given by the
    user. Based on posible values with an uncertainty to 
    get a value with no uncertainty.

    atributes:
      
      -value: float type, has the current value
      -bottom: float type that has the low limit of the uncertainty
      -top: float type that has the top value of the uncertaintly

    methods:

      -add
      -getBottom
      -getTop
      -getValue

  """

  def __init__(self, value,bottom,top):
    super(Value, self).__init__()
    self.value = value
    self.bottom = bottom
    self.top = top
  
  def add(self,value,bottom,top):
    """add: This method recevies the following parameters: 

        value: float type with a possible value
        bottom: its low uncertainty
        top: its up uncertainty
        
        This method is useful to add a new possible value and uncertainty
        to the Value class and update the information
    """
    if(self.bottom!=self.top):
      if(self.bottom<=bottom and self.top>=top):
        self.bottom=bottom
        self.top=top
      elif((self.bottom>bottom and self.top>=top and top>self.bottom) or (self.bottom<=bottom and self.top<top and bottom>self.top)):
        self.top=top
      elif((self.bottom<=bottom and self.top<top and bottom<self.top) or (self.bottom>bottom and self.top>=top and top<self.bottom)):
        self.bottom=bottom
      elif(self.bottom>bottom and self.top>=top):
        self.bottom=bottom
      self.value=((self.bottom+self.top)/2)

  def getValue(self):
    return self.value

  def getBottom(self):
    return self.bottom

  def getTop(self):
    return self.top

#------------------------------------------------------------------------------

class Chaser(_PackageBoundObject):
  """This class represents the chase that will do all the logic for an 
    specific incomplete data stored in a .csv document. 

    atributes:
      -Filename: It contains the path of the .csv file
      -trainData: Data to train
      -currentData: Is the data that will be filled
      -titles: titles of floating point information
      -alltitles: titles no matter the type

    methods:

      -trainDataBuilder
      -LinearRegression
      -Transposed
      -getDataToChase
      -store

  """
  def __init__(self, filename,saveFile):
    super(Chaser, self).__init__()
    self.filename = filename
    self.trainData = []
    self.saveFile = saveFile
    self.currentData = []
    self.titles = []
    self.allTitles = []
    self.indexes = []
    self.index = []
    self.realData = []

  def trainDataBuilder(self):
    """
      This function get all the data that is useful as reference to get 
      points for do the different types of regressions.  It returns a 
      list of strings with the names of the categories. 
    """
    data = []
    allTitles = []
    titles = []
    index = []
    with open(self.filename) as csv_file:
      csv_reader = csv.reader(csv_file, delimiter=',')
      line = 0
      for row in csv_reader:
        if(line==0):
          allTitles=row
        else:
          control = True
          for element in row:
            if(element==''):
              control = False
          if(control):
            count = 0
            currentRow = []
            for element in row:
              try:
                currentRow.append(float(element))
                if(index.count(count)==0):
                  index.append(count)
                if(titles.count(allTitles[count])==0):
                  titles.append(allTitles[count])
              except:
                pass
              count+=1
            data.append(currentRow)
        line+=1
    with open('trainData.csv', mode='w') as data_file:
      data_file = csv.writer(data_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
      data_file.writerow(titles)
      for currentData in data:
        data_file.writerow(currentData)
    self.trainData = self.Transposed(data) 
    self.titles = titles
    self.allTitles = allTitles
    self.index = index
    return titles

  def Transposed(self,matrix):
    try:
      return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]  
    except Exception as e:
      print("""Please check that the data is correct or:
           -eliminate the category that contains floats and strings at the same time.
           -eliminate the category that has strings and empty spaces at the same time""")

  def dataParser(self,fileName):
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


  def printData(self,data):
    """
      print all parsed data
    """
    for event in data:
      for title,info in event.items():
        print(f'{title}: {info}')
      print('\n')
      

  def getDataToChase(self):
    """
      Get data to chase, the data to complete
    """
    realData = []
    data = self.dataParser(self.filename)
    Parsedlist = []                                             #Getting all the information in lists
    for event in data:
      trainList = []
      realList = []
      for title,info in event.items():
        realList.append(info)
        try:
          trainList.append(Value(float(info),float(info),float(info)))
        except:
          if(info==''):
            trainList.append('')
      Parsedlist.append(trainList)
      realData.append(realList)
    self.realData = realData
    self.currentData = self.Transposed(Parsedlist)

  def LinearRegression(self):
    """
      This function will get all possible values for the empty spaces 
      based on liner regression. It receives a list of strings with 
      the name of the parameters and it will return a list of possible
      Value type (Class)
    """
    file = pd.read_csv ('trainData.csv', sep=',')
    model = LinearRegression()
    result = []
    for i in range(0,len(self.titles)):
      indexes = []
      for j in range(0,len(self.titles)):
        if(i!=j):
          X = file.iloc[:, i].values.reshape(-1, 1)  # values converts it into a numpy array
          Y = file.iloc[:, j].values.reshape(-1, 1)  # -1 means that calculate the dimension of rows, but have 1 column
          model.fit(X, Y)  # perform linear regression
          unc = 1-model.score(X, Y)
          if(j==0):
            count = 0
            for element in self.currentData[i]:
                if(element==''):
                  indexes.append(count)
                  try:
                    t = (model.coef_)*(self.currentData[j][count].getValue())+model.intercept_
                    t = t[0][0]
                    element = Value(t,t-(unc*t),t+(unc*t))
                  except:
                    pass
                count+=1
          else:
            self.indexes = indexes
            for index in indexes:
              if(self.currentData[j][index]!=''):
                t = (model.coef_)*(self.currentData[j][index].getValue())+model.intercept_
                t = t[0][0]
                try:
                  self.currentData[i][index].add(t,t-(unc*t),t+(unc*t))
                except:
                  self.currentData[i][index] = Value(t,t-(unc*t),t+(unc*t))

  def store(self):
    """
      Store all the data in a csv name
    """
    name = self.saveFile
    with open(name, mode='w') as data_file:
      data_file = csv.writer(data_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
      data_file.writerow(self.allTitles)
      matrix = self.Transposed(self.currentData)
      firstCount=0
      for row in matrix:
        values = []
        count = 0
        for element in row:
          if(element!=''):
            values.append(element.getValue())
          else:
            values.append('') 
          if(self.index.count(count)==0):
            values.insert(count,self.realData[firstCount][count])  
          count+=1
        index_count = 0
        for val in values:
          print(self.allTitles[index_count] + ": " + str(val))
          index_count+=1
        print("\n")
        data_file.writerow(values)
        firstCount+=1
      print("Data stored in " + name)

#------------------------------------------------------------------------------