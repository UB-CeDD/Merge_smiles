#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#Kersten Doering 06.07.2015, 27.07.2015

# generate shell script for downloading SDF files
# example: wget -O 5311498_later.sdf https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/5311498/record/SDF/ -a wget.log
c1 = "wget -O sdfs/"
c2 = ".sdf https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/"
c3 = "/record/SDF/ -a wget.log"

infile = open("01_NA_Family_A_Smiles.csv","r")
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
# use the file mol-files.rar from Fidele and extract the files into a folder mol-files
python download_sdfs.py 
chmod +x download.sh 
mkdir sdfs
./download.sh 
cat sdfs/* > structures.sdf
mkdir smiles # removed sdf lines in ACA_00017.mol, ACA_00042.mol, and ACA_00017.mol
python get_smiles.py 
#...
babel -isdf structures.sdf -ocan pubchem_smiles.smi -b
#205 molecules converted
#3692 audit log messages 9 debugging messages 
cat smiles/* > mol_smiles.smi
python merge_smiles.py 
python compare_smiles.py
"""
