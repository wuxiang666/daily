#!/usr/bin/env python                                                                                                
# encoding: utf-8

from optparse import OptionParser 

parser = OptionParser(usage="%prog [options]")
parser.add_option("-m","--machine",action="store",type="string",dest="machine",help="the machine to be check")
# parser.add_option("-f", "--file", dest="filename",help="write report to FILE", metavar="FILE")
# parser.add_option("-q", "--quiet",action="store_false", dest="quiet", default=True,
# 	help="don't print status messages to stdout")
# args=['-m','file.txt','-m','good luck to you', 'arg2', 'arge']
(options,args)=parser.parse_args()
print options.machine
# if options.machine:        
#     print options.machine.split(",")



