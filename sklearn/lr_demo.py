#!/usr/bin/env python                                                                                                
# encoding: utf-8

from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.externals import joblib
import codecs
from sklearn.linear_model import LogisticRegression
import sys,os
from optparse import OptionParser 


def main(mod='lr.model',pre="result.txt"):
	data = load_iris()
	features = data['data']
	target = data['target']
	feature_names = data['feature_names']
	X = StandardScaler().fit_transform(features)
	clf_l2_LR = LogisticRegression(C=100, penalty='l2', tol=0.01)
	clf_l2_LR.fit(X, target)
	clf_l2_LR.predict(X)
	joblib.dump(clf_l2_LR, mod)
	result = " ".join(map(lambda x:str(x),clf_l2_LR.predict(X).tolist()))
	with codecs.open(pre,"w") as fp:
		fp.write(result)


if __name__ == '__main__':
	parser = OptionParser(usage="%prog [options]")
	parser.add_option("-m","--model",action="store",type="string",dest="model",help="the model name and location")
	parser.add_option("-p","--predict",action="store",type="string",dest="predict",help="the predict result location")
	(options,args)=parser.parse_args()
	
	if (options.model and options.predict):
		main(options.model,options.predict)
	else:
		main()
