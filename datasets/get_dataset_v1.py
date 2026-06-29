import math
from random import random, uniform

import numpy as np


def get_dataset_v1(N: int, K: float, u_bar: float, R: float):
    inputs = []
    outputs = []
    limit = 100
    for _ in range(N):
        x = uniform(-limit, limit)
        y = uniform(-limit, limit)
        theta = uniform(0, 2 * math.pi)
        input = [x, y, math.cos(theta), math.sin(theta)]
        output = [1, -1]
        inputs.append(input)
        outputs.append(output)
    return np.array(inputs), np.array(outputs)

if __name__ == '__main__':
    a, b = get_dataset_v1(10, 2, 2, 2)
    print(a.shape, a)
    print(b.shape, b)


