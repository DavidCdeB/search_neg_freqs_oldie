# 
# Extracting zero or negative freq's from a set of *T.out

import re
import os
import glob
from itertools import islice
import numpy as np
import subprocess
import itertools
import sys


ALL_FREQ = []
path='./'
template = os.path.join(path, '*T.out')


for fname in glob.glob(template):
  print fname
  f = open(fname, 'r')
  real_part = False

  for line in f:

#       If the *.out are in crystal14, uncomment REAL PART and IMAGINARY PART and comment the others:
        if line.startswith('  DISPERSION K POINT NUMBER'):
           print line
#       elif line.startswith(' REAL PART'):
        if line.startswith(' MODES IN PHASE'):
            real_part = True
        elif line.startswith(' NORMAL MODES NORMALIZED TO CLASSICAL AMPLITUDES'):
            real_part = True
        elif line.startswith(' MODES IN ANTI-PHASE'):
#       elif line.startswith(' IMAGINARY PART'):
            real_part = False
        elif line.startswith(' FREQ(') and real_part:
             FREQS = line.split()
             FREQS_only_zero_or_negative = [x for x in FREQS if x.startswith('0.00') or x.startswith('-')]
             print FREQS_only_zero_or_negative
