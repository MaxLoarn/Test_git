import torch

x = torch.tensor(3.0)
y = torch.tensor(2.0)

print(x + y, x * y, x / y, x**y)

z = torch.arange(50)
print(z)
print('****************************************************************************')
print(len(z))
print(z[10])
print('****************************************************************************')
a = torch.arange(50).reshape(5, 10)
print(a)
print(a.shape)  # 显示 variable a dimension
print(a.T)      # 转置 Transpose
print('****************************************************************************')
# symmetric matrix 对称矩阵
b = torch.tensor([[1, 2, 3], [2, 0, 4], [3, 4, 5]])
print(b)
print(b == b.T)
print(b.T)
