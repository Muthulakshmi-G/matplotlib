#two or more lines display
import matplotlib.pyplot as plt

#line one points
x1=[10,20,30]
y1=[20,30,40]

#plottiong the line one points
plt.plot(x1,y1,label="line 1")

#line 2 points
x2=[10,20,30]
y2=[40,10,30]

#plotting the line 2 points

plt.plot(x2,y2,label="line 2")

plt.xlabel('x-axis')

plt.ylabel('yaxis')

plt.title("tow or more lines")

#show the legend on  the plot
plt.legend()

#Displays a figure
plt.show()
