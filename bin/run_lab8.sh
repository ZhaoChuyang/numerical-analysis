#!/usr/bin/env bash

# 运行程序1, 分别使用幂法、对称幂法、反幂法求最大特征值及特征向量
python -m src.lab8 --prob 1 --method power --iter-num 20 --tol 0.00001
python -m src.lab8 --prob 1 --method inverse --iter-num 20 --tol 0.00001
python -m src.lab8 --prob 1 --method symmetric --iter-num 20 --tol 0.00001

# 运行程序2, 求householder变换中使用到到H1, H2, H3
python -m src.lab8 --prob 2
