#!/usr/bin/env bash

# run experiment 3

# use LU factorization to solve this LES
python -m src.exp3 --method LU

# use Jacobi method to solve this LES. default norm is euclidean
python -m src.exp3 --method Jacobi --norm euclidean

# use Gauss-Seidel method to solve this LES. use maximum norm
python -m src.exp3 --method Gauss-Seidel --norm maximum