"""
-------------------------------------------------------------------------------
  
  Name: regression
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

class Chaser(object):
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
  def __init__(self, filename):
    super(Chaser, self).__init__()
    self.filename = filename
    self.trainData = []
    self.currentData = []
    self.titles = []
    self.allTitles = []

  def trainDataBuilder(self):
    """
      This function get all the data that is useful as reference to get 
      points for do the different types of regressions.  It returns a 
      list of strings with the names of the categories. 
    """
    data = []
    allTitles = []
    titles = []
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
    return titles

  def Transposed(self,matrix):
    result = []
    row = 0 
    for i in matrix:
      column = 0 
      newRow = []
      for j in i:
        try:
          newRow.append(matrix[column][row])
        except:
          pass
        column+=1
      row+=1
      result.append(newRow)
    return result

  def getDataToChase(self):
    indexes=[]
    matrix=[]
    with open(self.filename) as csv_file:
      csv_reader = csv.reader(csv_file, delimiter=',')
      line = 0
      for currentRow in csv_reader:
        row = []
        if(line!=0):
          if(line==1):
            index_count = 0
            for element in currentRow:
              try:
                float(element)
                indexes.append(index_count)
                index_count+=1
              except:
                index_count+=1
          for index in indexes:
            if(currentRow[index]!=''):
              row.append(Value(float(currentRow[index]),float(currentRow[index]),float(currentRow[index])))
            else:
              row.append('')
          matrix.append(row)
        line+=1
      self.currentData = self.Transposed(matrix)

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
          X, y = self.trainData[j], self.trainData[i]
          model.fit(X, y)
          unc = model.score(X, y)
          if(j==0):
            count = 0
            for element in self.currentData[i]:
                if(element==''):
                  indexes.append(count)
                  try:
                    t = model.predict(currentData[j][count].getValue())
                    element = Value(t,t-unc,t+unc)
                  except:
                    pass
                count+=1
          else:
            for index in indexes:
              t = model.predict(currentData[j][index].getValue())
              currentData[i][index].add(t,t-unc,t+unc)


  def store(self):
    name = "Test_" + self.filename
    with open(name, mode='w') as data_file:
      data_file = csv.writer(data_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
      data_file.writerow(self.allTitles)
      matrix = self.Transposed(self.currentData)
      for row in matrix:
        for element in row:
          element = element.getValue()
        data_file.writerow(row)
      print("Data stored in " + name)

#------------------------------------------------------------------------------
DataChaser = Chaser('Fireball_And_Bolide_Reports.csv')
DataChaser.trainDataBuilder()
DataChaser.getDataToChase()
DataChaser.LinearRegression()
DataChaser.store()