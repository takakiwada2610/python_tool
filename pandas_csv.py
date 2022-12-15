import pandas as pd
import os

dir_path = r'python_tool'
file_name = 'fruitlist.csv'

file_path = os.path.join(dir_path, file_name)

df = pd.read_csv(file_path)
print(df)