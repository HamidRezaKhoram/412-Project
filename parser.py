import matplotlib.pyplot as plt
import pandas as pd
data = pd.read_csv('dummy2.csv')
plt.plot(data['Data_value'], data['STATUS'])
plt.xlabel('X-axis label')
plt.ylabel('Y-axis label')
plt.title('Graph title')
plt.show()