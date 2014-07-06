#!/usr/bin/env python

import sys
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt;
import matplotlib.mlab as mlab
from jmlog2csv import jmlog2csv



def main(argv):
	jml = jmlog2csv(argv)
	csv_file = jml.convert()


	try:
		inp_csv_data = mlab.csv2rec(csv_file, delimiter=',')
	except IOError, e:
		print "I/O Error ({0}): {1}". format(e.errno, e.strerror)
		sys.exit(2)

	
	# Graphs by threads	
	inp_data = np.sort(inp_csv_data, order="step_active_threads")
	xval = [ x for x in inp_data.step_active_threads if x != -1]
	
	# Threads-Rate dependency graph
	sys.stdout.write("Building Threads-Rate dependency graph...")
	fig, ax = plt.subplots()
	fig.set_size_inches((9, 3))
	yval = [ y for y in inp_data.step_avg_rate if str(y) != "nan"]
	ax.plot(xval, yval, lw=1, color='green', label="Request rate")
	ax.set_title('Threads - Request rate')
	ax.set_ylabel('Rate (req/s)')
	ax.set_xlabel('Threads count')
	ax.grid()
	plt.legend()	
	plt.savefig('threads_rate.png', dpi=100, bbox_inches="tight")
	sys.stdout.write(" Done\n")

	# Thread - Average reply time graph
	sys.stdout.write("Building Threads-Average reply time dependency graph...")
	fig, ax = plt.subplots()
	fig.set_size_inches((9, 3))
	yval = [ y for y in inp_data.step_avg_reply_time if y != -1]
	ax.plot(xval, yval, lw=1, label="Average reply time")
	ax.set_title('Threads - Reply time')
	ax.set_ylabel('Reply time (ms)')
	ax.set_xlabel('Threads count')
	ax.grid()
	plt.legend()	
	plt.savefig('threads_avgrepltime.png', dpi=100, bbox_inches="tight")
	sys.stdout.write(" Done\n")
	
	sys.stdout.write("Building Threads-Errors dependency graph...")
	# Thread - Errors time graph
	fig, ax1 = plt.subplots()
	ax2 = ax1.twinx()

	fig.set_size_inches((9, 3))
	yval = [ y for y in inp_data.step_errors if y != -1]
	errcnt = ax1.plot(xval, yval, lw=1, label="Errors count", color="orange")
	yval = [ y for y in inp_data.step_errors_percentage if str(y) != "nan"]
	errprcnt = ax2.plot(xval, yval, lw=2, label="Errors percentage", color="red")
	ax1.set_title('Threads - Errors')
	ax1.set_ylabel('Errors (#)')
	ax2.set_ylabel('Errors (%)')
	ax1.set_xlabel('Threads count')
	ax1.grid()
	lns = errcnt+errprcnt
	lbls = [l.get_label() for l in lns]
	ax1.legend(lns, lbls, loc=0)	
	
	plt.savefig('threads_errors.png', dpi=100, bbox_inches="tight")
	sys.stdout.write(" Done\n")

	###############
	# Time graphs #
	###############    
	xval = [ x for x in inp_csv_data.total_time if x != -1]
	
	# Average Rate graph
	sys.stdout.write("Building Time-Rate dependency graph...")
	fig, ax = plt.subplots()
	fig.set_size_inches((9, 5))
	ax.set_xlabel('Seconds elapsed (s)')
	yval = [ y for y in inp_csv_data.total_avg_rate if str(y) != "nan"]
	rate = ax.plot(xval, yval, lw=1, label="Rate", color="green")
	ax.set_title('Average request rate')
	ax.set_ylabel('Request rate (req/s)')
	ax.set_xlabel('Time elapsed (s)')
	ax.grid()
	ax1 = ax.twinx()
	yval = [ y for y in inp_csv_data.step_active_threads[1:] if y != -1]
	thrcnt = ax1.plot(xval, yval, lw=1, label="Threads", color="blue")
	ax1.set_ylabel('Active threads')
	lns = rate + thrcnt
	lbls = [l.get_label() for l in lns]
	ax1.legend(lns, lbls, loc=0)	
	plt.savefig('time_avgrate.png', dpi=100, bbox_inches="tight")
	sys.stdout.write(" Done\n")

	# Average reply time graph
	sys.stdout.write("Building Time-Reply time dependency graph...")
	fig, ax = plt.subplots()
	fig.set_size_inches((9, 5))
	ax.set_xlabel('Seconds elapsed (s)')
	yval = [ y for y in inp_csv_data.total_avg_reply_time if y != -1]
	rate = ax.plot(xval, yval, lw=1, label="Reply time", color="magenta")
	ax.set_title('Average reply time')
	ax.set_ylabel('Reply time (ms)')
	ax.set_xlabel('Time elapsed (s)')
	ax.grid()
	ax1 = ax.twinx()
	yval = [ y for y in inp_csv_data.step_active_threads[1:] if y != -1]
	thrcnt = ax1.plot(xval, yval, lw=1, label="Threads", color="blue")
	ax1.set_ylabel('Active threads')
	lns = rate + thrcnt
	lbls = [l.get_label() for l in lns]
	ax1.legend(lns, lbls, loc=0)	
	plt.savefig('time_avgrepltime.png', dpi=100, bbox_inches="tight")
	sys.stdout.write(" Done\n")

	# Maximum reply time graph
	sys.stdout.write("Building Time-Maximum Reply time dependency graph...")
	fig, ax = plt.subplots()
	fig.set_size_inches((9, 5))
	ax.set_xlabel('Seconds elapsed (s)')
	yval = [ y for y in inp_csv_data.step_max_reply_time[1:] if y != -1]
	rate = ax.plot(xval, yval, lw=1, label="Nax. Reply time", color="magenta")
	ax.set_title('Max reply time')
	ax.set_ylabel('Max Reply time (ms)')
	ax.set_xlabel('Time elapsed (s)')
	ax.grid()
	ax1 = ax.twinx()
	yval = [ y for y in inp_csv_data.step_active_threads[1:] if y != -1]
	thrcnt = ax1.plot(xval, yval, lw=1, label="Threads", color="blue")
	ax1.set_ylabel('Active threads')
	lns = rate + thrcnt
	lbls = [l.get_label() for l in lns]
	ax1.legend(lns, lbls, loc=0)	
	plt.savefig('time_maxrepltime.png', dpi=100, bbox_inches="tight")
	sys.stdout.write(" Done\n")

	# Average errors graph
	sys.stdout.write("Building Time-Errors time dependency graph...")
	fig, ax = plt.subplots()
	fig.set_size_inches((9, 5))
	ax.set_xlabel('Seconds elapsed (s)')
	yval = [ y for y in inp_csv_data.step_errors_percentage[1:] if str(y) != "nan"]
	err_prcnt = ax.plot(xval, yval, lw=2, label="Errors (%)", color="red")
	ax.set_title('Errors')
	ax.set_ylabel('Errors (%)')
	ax.set_xlabel('Time elapsed (s)')
	ax.grid()
	ax1 = ax.twinx()
	yval = [ y for y in inp_csv_data.step_active_threads[1:] if y != -1]
	thrcnt = ax1.plot(xval, yval, lw=1, label="Threads", color="blue")
	ax1.set_ylabel('Active threads')
	lns = err_prcnt + thrcnt
	lbls = [l.get_label() for l in lns]
	ax1.legend(lns, lbls, loc=0)	
	plt.savefig('time_errors.png', dpi=100, bbox_inches="tight")
	sys.stdout.write(" Done\n")

if __name__ == "__main__":
	main(sys.argv[1:])