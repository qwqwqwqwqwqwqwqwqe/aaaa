import random

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
if __name__=='__main__':
    data=[]
    for i in range(1000):
        t=random.randint(0,100)
        data.append((t))
    data1=set(data)
    for i in data1:
        print("元素{0}出现的个数为{1}".format(i,data.count(i)))