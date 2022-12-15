import pandas as pd
import matplotlib.pyplot as plt

csv_path = r'python_tool/suuji.csv'
csv_df = pd.read_csv(csv_path)

data_x = csv_df[csv_df.columns[0]]
data_y = csv_df[csv_df.columns[1]]

plt.xlabel(csv_df.columns[0])
plt.ylabel(csv_df.columns[1])

plt.plot(data_x, data_y, linestyle='solid', marker='o')
plt.show()