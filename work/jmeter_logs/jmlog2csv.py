#!/usr/bin/env python

import os
import sys
import getopt

class jmlog2csv:

	def __init__(self, argv):
		self.argv = ""
		
		try:
			opts, args = getopt.getopt(argv, "i:", ["input_file="])
		except getopt.GetoptError:
			print os.path.basename(__file__)+" -i[--input_file] <input file>"
			sys.exit(2)
	
		for opt, arg in opts:
			if opt in ("-i", "--input_file"):
				self.input_file_name = arg

		self.output_file_name = os.path.splitext(os.path.basename(self.input_file_name))[0]+".csv"


	def convert(self):
				
		try:
			inpf = open(self.input_file_name,"r")
			output_csv = open(self.output_file_name,"w")
		except IOError, e:
			print "I/O Error ({0}): {1}". format(e.errno, e.strerror)
			sys.exit(2)



		output_csv_hdr = "step_requests,total_requests,step_time,total_time,\
step_avg_rate,total_avg_rate,step_avg_reply_time,\
total_avg_reply_time,step_max_reply_time,\
total_max_reply_time,step_errors,total_errors,\
step_errors_percentage,total_error_percentage,\
step_active_threads\n"
	

		output_csv.write(output_csv_hdr)

		print "Processing file: "

		i = 0
		for line in inpf:
			line_list = line.split()
		
			if line_list[0] == "summary":
				if line_list[1] == "+":
					valsToWrite = [line_list[2], "", line_list[4][:-1], "",\
								 line_list[6][:-2], "", line_list[8], "",\
								 line_list[12], "", line_list[14], "",\
								 line_list[15].strip("(")[:-2], "", line_list[17]]
				
				elif line_list[1] == "=":
					valsToWrite = ["", line_list[2], "", line_list[4][:-1], "",\
								 line_list[6][:-2], "", line_list[8], "",\
								 line_list[12], "", line_list[14], "",\
								 line_list[15].strip("(")[:-2]]

				i += 1 	
				output_csv.write(",".join(valsToWrite)+"\n")
				sys.stdout.write("#")
		print "\nTotal lines processed: %d" % (i)
		
		return self.output_file_name




if __name__ == "__main__":
	jml = jmlog2csv(sys.argv[1:])
	jml.convert()
