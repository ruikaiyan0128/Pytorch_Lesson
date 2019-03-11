import torch as t
import time
from torch import autograd
print(t.__version__)
print(t.cuda.is_available())

x = t.tensor(1.)
a = t.tensor(1., requires_grad=True)
b = t.tensor(2., requires_grad=True)
c = t.tensor(3., requires_grad=True)

y = a**2*x+b*x+c

print('before:', a.grad, b.grad, c.grad)
grads = autograd.grad(y, [a,b,c])
print('after:', grads[0], grads[1], grads[2])
