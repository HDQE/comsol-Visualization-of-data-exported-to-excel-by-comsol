import pandas as pd
import matplotlib.pyplot as plt
import os
from matplotlib import rcParams

rcParams['font.sans-serif'] = ['SimHei']
rcParams['axes.unicode_minus'] = False  

desktop = os.path.join(os.path.expanduser("~"), "Desktop")
file_path = os.path.join(desktop, "temp.xlsx")

df = pd.read_excel(file_path, usecols=[0], header=None)

split_data = df[0].str.split(expand=True)

split_data = split_data.dropna()

split_data.columns = ['x', 'y']

split_data['x'] = pd.to_numeric(split_data['x'], errors='coerce')
split_data['y'] = pd.to_numeric(split_data['y'], errors='coerce')

# 进行数据采样，假设每10个点显示一个点
sampled_data = split_data.iloc[::10, :]

# 绘制图形，减少关键点数量，保留细线
plt.plot(split_data['x'], split_data['y'], linewidth=1, label='线条')  # 线条

# 在采样数据上显示较少的关键点
plt.plot(sampled_data['x'], sampled_data['y'], marker='o', linestyle='None', label='关键点')

plt.title("位移图")
plt.xlabel("X轴")
plt.ylabel("Y轴")

plt.legend()

plt.show()
