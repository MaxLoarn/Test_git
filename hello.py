import torch
import os
import pandas as pd

os.makedirs(os.path.join('C:\\Users\\13339\\Desktop\\Ai\\data'), exist_ok=True)
# exist_ok=True 只有在目录不存在时创建目录，目录已存在时不会抛出异常。
data_file = os.path.join('C:\\Users\\13339\\Desktop\\Ai\\data', 'house_tiny.csv')
with open(data_file, 'w') as f:
    f.write('NumRooms,Alley,Price\n')  # 列名
    f.write('NA,Pave,127500\n')  # 每行表示一个数据样本
    f.write('2,NA,106000\n')
    f.write('4,NA,178100\n')
    f.write('NA,NA,140000\n')
data = pd.read_csv(data_file)
print(data)

x = torch.arange(12)
print(x)
