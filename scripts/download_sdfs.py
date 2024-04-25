#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#Kersten Doering 06.07.2015, 27.07.2015

# generate shell script for downloading SDF files
# example: wget -O 5311498_later.sdf https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/5311498/record/SDF/ -a wget.log
c1 = "wget -O ../sdfs/"
c2 = ".sdf https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/"
c3 = "/record/SDF/ -a wget.log"

infile = open("../data/01_NA_Family_A_Smiles.csv","r")
outfile = open("download.sh","w")
for line in infile:
	try:
		cid = str(int(line.strip().split(",")[-4]))
	except:
		#print line
		continue
	outfile.write(c1+cid+c2+cid+c3+"\n")
outfile.close()



"""
import sys
import pandas as pd

infile = sys.argv[1]
outfile = open("download.sh","w")

c1 = "wget -O sdfs/"
c2 = ".sdf https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/"
c3 = "/record/SDF/ -a wget.log"

df = pd.read_csv(infile)
cids = df["PubChemID"].tolist() #column must be literal
for cid in cids:
	if cid is not None:
		outfile.write(c1+cid+c2+cid+c3+"\n")
outfile.close()
"""
