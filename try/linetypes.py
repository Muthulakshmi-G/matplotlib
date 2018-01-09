import matplotlib.pyplot as plt
x1=[10,20,30]
y1=[20,40,10]

plt.plot(x1,y1,linestyle='--',color='blue',linewidth=3)

x2=[10,20,30]
y2=[40,10,30]

plt.plot(x2,y2,linestyle='solid',color='red',linewidth=5)

x3=[10,20,40]
y3=[20,40,10]

plt.plot(x3,y3,linestyle='solid',color='black',linewidth=6)
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('Two or more lines with different widths and colors with suitable legends ')
plt.legend()
plt.show()
