import torch
from torch import

def error(b, w, points):
    totalError = 0
    for i in range(0,len(points)):
        x = points[i, 0]
        y = points[i, 1]
        totalError += (y-w*x-b)**2
    return totalError / len(points)