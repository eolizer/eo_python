#!/usr/bin/env python

import os
import sys
import getopt

def main(argv):
	input_file = ""
	output_iter = ""
	output_summ = ""

	try:
		opts, args = getopt.getopt(argv, "i:", ["input_file="])
	except getopt.GetoptError:
		print os.path.basename(__file__)+" -i[--input_file] <input file>"
		sys.exit(2)
	
	for opt, arg in opts:
		if opt in ("-i", "--input_file"):
			input_file = arg

	output_iter = os.path.splitext(os.path.basename(input_file))[0]+"_iter.csv"
	output_summ = os.path.splitext(os.path.basename(input_file))[0]+"_summ.csv"
	

	try:
		inpf = open(input_file,"r")
		outiterf = open(output_iter,"w")
		outsummf = open(output_summ,"w")
	except IOError, e:
		print "I/O Error ({0}): {1}". format(e.errno, e.strerror)
		sys.exit(2)

	output_iter_hdr = "\"Phase requests\",\"Phase time\",\"Phase rate\",\"Phase avg. repl. time\",\"Phase max. repl. time\",\"Phase errors\",\"Phase error percentage\"\n"
	output_summ_hdr = "\"Total requests\",\"Total time\",\"Total avg. rate\",\"Total avg. repl. time\",\"Total max. repl. time\",\"Total errors\",\"Total avg. error percentage\"\n"

	outiterf.write(output_iter_hdr)
	outsummf.write(output_summ_hdr)

	for line in inpf:
		line_list = line.split()
		print line_list
		if line_list[0] == "summary":
			valsToWrite = [line_list[2], line_list[4][:-1], line_list[6][:-2], line_list[8], line_list[12], line_list[14], line_list[15].strip("(")[:-2]]
			if line_list[1] == "+":
				outiterf.write(",".join(valsToWrite)+"\n")
			elif line_list[1] == "=":
				outsummf.write(",".join(valsToWrite)+"\n")
				

if __name__ == "__main__":
	main(sys.argv[1:])