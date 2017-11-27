#! /usr/bin/env python
# -* - coding:utf8 -*-

import codecs
import re
import sys

def main(inputFile,outputFile):
	with codecs.open(inputFile,"r") as f:
		result =  "".join(f.readlines())
		temp = [re.sub("TBLPROPERTIES (.*)","",i,flags=re.S).strip()+";" for i in result.split(";")]
    with codecs.open(outputFile,"w") as f:
    	f.write("\n\n".join(final))


if __name__ == '__main__':
	main(sys.argv[1],sys.argv(2))