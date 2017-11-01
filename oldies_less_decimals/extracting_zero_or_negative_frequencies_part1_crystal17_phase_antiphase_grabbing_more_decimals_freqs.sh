#

# Program to exctract zero or neg. freqs:

python extracting_zero_or_negative_frequencies_part1_crystal17_phase_antiphase_grabbing_more_decimals_freqs.py > zero_or_negatives_grabbing_more_decimals_freqs.txt

ex zero_or_negatives_grabbing_more_decimals_freqs.txt <<-EOF
  :g/\[\]/d    
  :g/^$/d     
  :%s/\.\//\r\.\//g 
  :g/MODES         EIGV          FREQUENCIES     IRREP/d
  :g/HARTREE/d
  wq " Update changes and quit.
EOF

# In order, these commands are:

# remove lines with "[]"
# remove emtpy lines
# search for "./"
# Add an empty line before "./"
# Update changes and quit.
