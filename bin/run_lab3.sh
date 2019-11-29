#!/usr/bin/env bash

# run experiment 3

# use LU factorization to solve this LES
python -m src.lab3 --method LU

# use Jacobi method to solve this LES. default norm is euclidean norm
python -m src.lab3 --method Jacobi --norm euclidean

# use Gauss-Seidel method to solve this LES. use maximum norm
python -m src.lab3 --method Gauss-Seidel --norm maximum