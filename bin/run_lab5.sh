#!/usr/bin/env bash

# 数值微分及数值积分上机实验

# 使用复合梯形公式计算
python -m src.lab5 --method ct

# 使用复合辛普森公式计算
python -m src.lab5 --method cs

# 取计算精度为1e-4时，使用两种方式需要的步长和子区间个数
python -m src.lab5 --method composite_simpson --tol 0.0001

