#!/bin/bash

# This script runs the MMD-based generative network for multivariate data, and
# then computes data weights based on either support points or their nearest
# neighbors in the data (thus, a coreset).
#   SNAP is {0, 1}, and defines whether to use the simulations vs coreset.
#   M is the size of the support set or coreset.
#   DATA_FILE is the name of the file containing original data to be modeled.

SNAP=1
M=200
DATA_FILE='gp_data.txt'

python multivariate_mmd_gan.py --data_file=$DATA_FILE --gen_num=$M --max_step=100000;
python weighting.py --data_file=$DATA_FILE --snap=0;
python weighting.py --data_file=$DATA_FILE --snap=1;
