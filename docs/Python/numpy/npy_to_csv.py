#!/bin/env python3
import numpy as np
import sys

# 读取npy文件并转换成csv
def npy_to_csv(i,o):
    data = np.load(i)
    np.savetxt(o,data,delimiter=',')
    
if __name__=='__main__':
    if(len(sys.argv)!=3):
        print('usage:\n\tnpy_to_csv.py xxx.npy xxx.csv')
        exit(1)
    else:
        npy_to_csv(sys.argv[1],sys.argv[2])
