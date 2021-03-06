import matplotlib.pyplot as plt
import numpy as np

#In this file i try to use numpy array in the place of native python list's

years = np.array( [1950, 1960, 1970, 1980, 1990, 2000, 2010] )
gdp = np.array( [300.2,543.3,1075.9, 2962.5, 5979.6,10289.7,14958.3] )

#create a linechart, years in axis x and gdp in axis y
plt.plot(years,gdp, color='green',marker='o',linestyle='solid')

plt.title('GdP Nominal')

plt.ylabel('USD Bi')
plt.xlabel('years')

plt.show()
