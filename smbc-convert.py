#!/usr/bin/env python
import sys, os, codecs

#Convert CSV files downloaded from Mitsui-Sumitomo credit card website
#for import into iBank because:
#1. it does not support the Shift-JIS encoding
#2. somehow it can't detect the 'YYYY/MM/DD' date format

#Based on script created by Liang Sun on March, 5, 2011
#http://liangsun.info/2011/03/11/python-script-to-transform-shift-jis-to-utf-8-encoding/

def main(argv):
	if len(argv) < 2:
		print "USAGE: %r infile [outfile]" % (argv[0],)
		print "If outfile is missing, output to stdout"
		return 0
	if not os.path.exists(sys.argv[1]):
		sys.stderr.write("ERROR: file %r was not found!" % (argv[1],))
		return 1
	
	# infile from SMBC website is always shift-jis crap
	infile = argv[1]
	fin = codecs.open(infile, "rb", "shift-jis")
	
	# if we did not specify an outfile, output to console
	if len(argv) == 2:
		# trick to get output to stdout in unicode even in pipe sequences
		fout = codecs.getwriter("utf8")(sys.stdout)
	else:
		outfile = argv[2]
		fout = codecs.open(outfile, "wb", "utf-8")
	
	try:
		for line in fin.readlines():
			line = line.split(",")
			line[0] = line[0].replace("/","-")
			fout.write(",".join(line))
	except UnicodeDecodeError:
		sys.stderr.write("ERROR: infile is not encoded with shift-jis")
	
	fin.close()
	fout.close()

if __name__ == "__main__":
    sys.exit(main(sys.argv))