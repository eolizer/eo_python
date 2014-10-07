#!/usr/env python

import os
import sys
import collections
import getopt





def main(argv):
   
   # Script variables
   

   # Get and check script parameters
   help_message = """Usage: distRandom.py -d --distribcsv <distribution csv> -o --outpath <output path> -c --count <files count> --prefix <filename prefix>

   Script generates\n"""
   try:
      opts, args = getopt.getopt(argv, "hd:o:c:p:",["distribcsv=","outpath=","prefix="])
   except getopt.GetoptError:
      print help_message
      sys.exit(2)
   else:
   	  print help_message
   	  sys.exit(2)

   
   for opt, arg in opts:
       if opt == '-h':
           print help_message
           sys.exit()
       elif opt in ("-d", "--distribcsv"):
       	   input_file = arg
       elif opt in ("-o", "--outpath"):
       	   output_file = arg
       elif opt in ("-c", "--count"):
       	   output_file = arg
       elif opt in ("-p", "--prefix"):
       	   p_lines = int(arg)       




if __name__ == "__main__":
   main(sys.argv[1:])

