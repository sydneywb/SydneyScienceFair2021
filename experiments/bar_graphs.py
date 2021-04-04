import matplotlib.pyplot as plt 

# Can you plot multiple bars on top of each other in a matplotlib bar graph?

plt.bar(0,2, color='b')
plt.bar(1,2, color='g')

plt.bar(0,1, color='r')

y = [1.5, 0.5]
for i in y:
	plt.bar(1,i, color='b' if i == 1.5 else 'r')


plt.show()