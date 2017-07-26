#

# Program to exctract zero or neg. freqs:

python extracting_zero_or_negative_frequencies_part1.py > zero_or_negatives.txt

ex zero_or_negatives.txt <<-EOF
  :g/\[\]/d    
  :g/^$/d      
  :%s/\.\//\r\.\//g
  wq " Update changes and quit.
EOF

# In order, these commands are:

# remove lines with "[]"
# remove emtpy lines
# search for "./"
# Add an empty line before "./"
# Update changes and quit.
