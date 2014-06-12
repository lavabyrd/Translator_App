# standard file import and export with known file names and delimiter is comma (default)

import csv
inputfile = raw_input("What's the file called?") 


""" 
using this allows the file to be picked up 
from the same location as the script.py.
By introducting a full file location i can simply call from that location, 
(e.g. inputfile = ("c:\\test\\test.csv")) but I need to be sure to include the escape characters 
"""


output = raw_input("What will we call the file?(include extension)")

def known():
	with open(inputfile, 'rb') as i:
		reader = csv.reader(i, delimiter = ' ', quoting = csv.QUOTE_MINIMAL)
		with open(output, 'wb') as o:
			writer = csv.writer(o, delimiter = ' ', quoting = csv.QUOTE_MINIMAL)
			for row in reader:
				writer.writerow(row)


known()