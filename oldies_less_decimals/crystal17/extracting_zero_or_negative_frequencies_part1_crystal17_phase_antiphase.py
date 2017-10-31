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

        if line.startswith('  DISPERSION K POINT NUMBER'):
           print line

#       elif line.startswith(' REAL PART'):
        elif line.startswith(' MODES IN PHASE'):
            real_part = True
#           print line
        elif line.startswith(' NORMAL MODES NORMALIZED TO CLASSICAL AMPLITUDES'):
            real_part = True
#            print line
#       elif line.startswith(' IMAGINARY PART'):
        elif line.startswith(' MODES IN ANTI-PHASE'):
            real_part = False
        elif line.startswith(' FREQ(') and real_part:
             FREQS = line.split()
             FREQS_only_zero_or_negative = [x for x in FREQS if x.startswith('0.00') or x.startswith('-')]
             print FREQS_only_zero_or_negative
