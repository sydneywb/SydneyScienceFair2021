import numpy as np 
import pandas as pd 

df = pd.DataFrame(
	[['Jan', 58, 42, 74, 22, 2.95],
	['Feb', 61, 45, 78, 26, 3.02],
	['Mar', 65, 48, 84, 25, 2.34]],
	index = [0, 1, 2],
	columns = ['month', 'avg_high', 'avg_low', 'record_high', 'record_low', 'avg_precipitation'])
print(df)

a = np.array([[1, 2, 3], [4, 5, 6]])
new_a = np.append(a, [[7, 8, 9]], axis=0)
print(new_a)

import os
directory = '/Users/sydneybadescu/Desktop/python_work/science_fair2021/cover_images'
for file in os.listdir(directory):
	print(file)
