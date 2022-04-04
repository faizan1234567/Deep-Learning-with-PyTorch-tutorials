import torch

a = torch.arange(16, dtype = torch.float)
b = a.reshape(4,4)
print(b)

x = torch.ones(4, 4)
print(f'oness tensor: {x}')

y = torch.randn(5, 5)
print(f'random number: {y}')