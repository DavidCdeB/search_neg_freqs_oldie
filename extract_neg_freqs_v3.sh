#

# Program to exctract zero or neg. freqs:

#grep "WITH SHRINKING FACTORS" *.out > neg_freqs_grabbing_more_decimals.txt 
python extract_neg_freqs_v3.py > neg_freqs_grabbing_more_decimals.txt

ex neg_freqs_grabbing_more_decimals.txt <<-EOF
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
