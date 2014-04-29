# standard file import and export with known file names and delimiter is comma (default)

import csv
inputfile = raw_input("What's the file called?")
output = raw_input("What will we call the file?(include extension)")

def known():
	with open(inputfile, 'rb') as i:
		reader = csv.reader(i, delimiter = ' ', quoting = csv.QUOTE_MINIMAL)
		with open(output, 'wb') as o:
			writer = csv.writer(o, delimiter = ' ', quoting = csv.QUOTE_MINIMAL)
			for row in reader:
				writer.writerow(row)


known()