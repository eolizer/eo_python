#!/usr/bin/python

import sys
import random
import getopt

def main(argv):
# Get script parameters
   input_file = ''
   output_file = ''
   p_lines = ''

   try:
      opts, args = getopt.getopt(argv, "hi:o:p:",["ifile=","ofile=","plines="])
   except getopt.GetoptError:
      print 'random_urls.py -i <input_file> -o <output_file> -p <number_of_lines_percent>' 
      sys.exit(2)
   for opt, arg in opts:
       if opt == '-h':
           print 'random_urls.py -i <input_file> -o <output_file> -n <number_of_lines>' 	
           sys.exit()
       elif opt in ("-i", "--ifile"):
       	   input_file = arg
       elif opt in ("-o", "--ofile"):
       	   output_file = arg
       elif opt in ("-p", "--plines"):
       	   p_lines = int(arg)

   """
    Open input file, read file content to memory variable and calculate number
    of lines in input file
   """
   with open(input_file, "r") as inpf:
      inplist = inpf.readlines()
      number_of_inplines = len(inplist)

# Calculate number of lines in output file based on --plines 
   number_of_outlines = number_of_inplines * p_lines // 100

# Get number_of_outlines of random lines from input file 
   lines_num_to_out = random.sample(xrange(number_of_inplines), number_of_outlines)

# Write randomly selected lines from input file to output file
   with open(output_file, "w") as outf:
      for l in lines_num_to_out:
   	     outf.write(inplist[l])



if __name__ == "__main__":
   main(sys.argv[1:])

