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
template = os.path.join(path, '*.out')


for fname in glob.glob(template):
  print fname
  f = open(fname, 'r')
  real_part = False

  for line in f:

        if line.startswith('  DISPERSION K POINT NUMBER'):
           print line

        if 'MODES         EIGV          FREQUENCIES     IRREP' in line:

            print line
            print f.next()

            while True:
               target = f.next()
               aux = target.split()

               if not aux:
                  break

               first_No = aux[0]
               second_No = aux[1]
               freq = aux[3]

               first_No = first_No.translate(None, '-')  # remove the '-'

               factor_freq = abs(int(second_No) - int(first_No)) + 1

               freqs = [freq] * factor_freq

#              FREQS_only_zero_or_negative = [x for x in freqs if x.startswith('0.0000') or x.startswith('-')]
               FREQS_only_zero_or_negative = [x for x in freqs if x.startswith('-')]
               print FREQS_only_zero_or_negative


