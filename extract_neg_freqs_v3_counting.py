# Counting the number of negative freq's 

import re
import os
import glob
from itertools import islice
import numpy as np
import subprocess
import itertools
import sys

f = open('neg_freqs_grabbing_more_decimals.txt', 'r')
print f
for line in f:
        if re.match(r"^.", line):
         print line
         All_aux = []
         while True:
               target = f.next()
               target2 = target.translate(None, "[]'',")

               aux = target2.split()
               All_aux.append(aux)
 
               flat_list = [item for sublist in All_aux for item in sublist]
               if not aux:
                 break
         print 'len(negatives) = ' , len(flat_list)

