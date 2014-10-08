#!/usr/env python

import os
import sys
import collections
import getopt
import csv



def main(argv):
  """ Main function """
   
  # Script variables
  inp_csv =''
  out_path = ''
  file_count = 0   

  help_message = """Usage: distRandom.py -d --distribcsv <distribution csv> -o --outpath <output path> -c --count <files count> --prefix <filename prefix>

Script generates\n"""

  # Get and check script parameters
  if not argv:
    print help_message
    sys.exit(2)
  
  try:
    opts, args = getopt.getopt(argv, "hd:o:c:p:",["distribcsv=","outpath=","prefix="])
  except getopt.GetoptError:
    print help_message
    sys.exit(2)
    
  for opt, arg in opts:
    if opt == '-h':
      print help_message
      sys.exit()
    elif opt in ("-d", "--distribcsv"):
      inp_csv = arg
    elif opt in ("-o", "--outpath"):
      out_path = arg
    elif opt in ("-c", "--count"):
      file_count = int(arg)
    elif opt in ("-p", "--prefix"):
      file_prefix = arg

  """ Open CSV size distribution file and read it to distRecords variable"""
  try:
    finp = open(inp_csv,'rb')
    dist_records = csv.reader(finp, delimiter=',')
  except IOError, e:
    print "I/O Error ({0}): {1}". format(e.errno, e.strerror)
    sys.exit(2)
  percentile_list = []
  for row in dist_records:
   percentile_list.append({"perc":row[0], "settings":{"minsize":row[1], "maxsize":row[2]}})

  print percentile_list

  """ Calculate number of files for each percentile """
  for perc_row in percentile_list:
    pfiles = (file_count * int(perc_row["perc"]))/100
    perc_row["settings"]["files"] = pfiles
  
  



  print percentile_list
  
# Run point
if __name__ == "__main__":
   main(sys.argv[1:])

