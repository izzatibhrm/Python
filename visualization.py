"""

Description: Data visualization using python
Dataset: Developer.csv @ Python Session 2.1

"""
#import module-numpy
#used to visualize data or 
#to perform a wide variety of mathematical operations on array
import numpy as np
#import module to work with dataset
import pandas as pd
#import module - matplotlib
#creating static, animated and interactive visualizations
from matplotlib import pyplot as plt

#the data set
filename = r"C:\Users\izzat\Downloads\ACDSP\PYTHON-SESSION-2-1\DEVELOPER.csv"

#display the data type for the variables
print(type(filename))

#red file and print the output
df = pd.read_csv(filename)
print(df)
 
plt.style.use("fivethirtyeight")
ages_x = df['age']
x_indexes = np.arange(len(ages_x))

#specify the width
width = 0.25
python_y = df['python_dev']
java_y = df['java_dev']
cplus_y = df['cpplus_dev']

plt.title("Age vs Developer's salary in USD")

plt.xlabel('Age')
plt.ylabel("Developers")

#plot bar
plt.bar(x_indexes - width,python_y,width=width,color='red',label="Python Developers")
plt.bar(x_indexes,java_y,width=width,color='blue',label="Java Developers")
plt.bar(x_indexes + width,cplus_y,width=width,color='green',label="C++ Developers")

#for indication or label of data
plt.legend()
plt.xticks(ticks=x_indexes,label=ages_x)
plt.tight_layout()
plt.show()
