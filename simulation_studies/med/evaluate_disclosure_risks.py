import argparse
import numpy as np
import pdb

"""Evaluate disclosure risk for data set generated by multivariate_mmd_gan.py.

  Flags:
    tag: Defines which experiment's directory to read from, e.g logs_TAG. 
    temp: Boolean, to load temp files from fixed model.
"""

parser = argparse.ArgumentParser()
parser.add_argument('--tag', type=str, default='test')
parser.add_argument('--temp', action='store_true', default=False, dest='temp')
args = parser.parse_args()
tag = args.tag
temp = args.temp

if temp:
    filenames = [
        'logs_{}/presence_risk_temp.txt'.format(tag),
        'logs_{}/attribute_risk_temp.txt'.format(tag)]
else:
    filenames = [
        'logs_{}/presence_risk.txt'.format(tag),
        'logs_{}/attribute_risk.txt'.format(tag)]

for f in filenames:
    risk = np.loadtxt(open(f, 'rb'), delimiter=',')
    risk = risk[-10:]
    # Risk has two columns: Sensitivity and Precision.
    mean_sensitivity, mean_precision = np.mean(risk, axis=0)
    std_sensitivity, std_precision = np.std(risk, axis=0)
    print('\nEvaluated file: {}'.format(f))
    print('  Sensitivity (mean, +- 2 * std) = {:.4f}, [{:.4f}, {:.4f}]'.format(
        mean_sensitivity, mean_sensitivity - 2 * std_sensitivity,
        mean_sensitivity + 2 * std_sensitivity))
    print('  Precision (mean, +- 2 * std) = {:.4f}, [{:.4f}, {:.4f}]'.format(
        mean_precision, mean_precision - 2 * std_precision,
        mean_precision + 2 * std_precision))
