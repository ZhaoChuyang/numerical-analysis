#!/usr/bin/env bash

# run experiment 2
python -m src.lab2 1 --a 0 --b 1 --tol 0.0005 --n 100
python -m src.lab2 2 --tol 0.00001 --n 50
python -m src.lab2 3 --a 0 --b 1 --tol 0.00001 --n 50 --p0 0.5 --p1 0.6