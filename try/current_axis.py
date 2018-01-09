import matplotlib.pyplot as plt
x=range(1,50)
y=[value*3 for value in x]

plt.plot(x,y)
plt.xlabel('x-axis')
plt.ylabel('y-axis')

plt.title('draw line')

#shows the current axis limits values
print(plt.axis())
#set the new axes limits
plt.axis([0,100,0,200])

plt.show()
