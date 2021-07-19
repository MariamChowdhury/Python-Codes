import numpy as np # importing numpy for mathematical operations
import matplotlib.pyplot as plt #for showing plots
x=np.arange(1,10,2) # taking values from 1 to 10 with a interval of 2 with the form of an array
print(x) #will print [1 3 5 7 9]
y=np.sqrt(x) # root of the values of x
print(y)
plt.plot(x,y) # making a plot
plt.show() #show plot
plt.close('all') #closing plots
plt.plot(x,x, 'r') #straight line plot with x and x of red color
plt.show()
plt.plot(x,y,'r',x,x,'g',y,x,'b', lw=3) #plotting multiple eqn together, lw=line width
plt.title('title of the plot')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.show()
