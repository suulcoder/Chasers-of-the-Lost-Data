#import DataChaser
from DataChaser import *
DataChaser = Chaser('Fireball_And_Bolide_Reports.csv','TestFireball_And_Bolide_Reports.csv')
DataChaser.trainDataBuilder()
DataChaser.getDataToChase()
DataChaser.LinearRegression()
DataChaser.cubicRegression()
DataChaser.quadraticRegression()
DataChaser.store()