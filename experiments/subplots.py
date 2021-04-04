import matplotlib.pyplot as plt 

# trying to learn how to use matplotlib subplots

fig, (ax1,ax2) = plt.subplots(1,2)

x = [i for i in range(100)]
y = x
z = [8 for i in range(100)]
ax1.plot(x,y)
ax2.plot(x,z)
plt.show()