#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#Kersten Doering 28.07.2015

cids = {}
infile = open("pubchem_smiles.smi","r")
for line in infile:
    temp = line.strip().split("\t")
    cids[temp[1]] = temp[0]
infile.close()

mols = {}
infile = open("mol_smiles.smi","r")
for line in infile:
    temp = line.strip().split("\t")
    mols[temp[1].replace(".mol","")] = temp[0]
infile.close()

infile = open("01_NA_Family_A_Smiles.csv","r")
outfile = open("01_NA_Family_A_Smiles-o.csv","w")
for line in infile:
    if "PubChem Non canonical SMILES" in line:
        outfile.write("\t\t\t\t" + line.strip() + "\t" + "PubChem canonical SMILES" + "\t" + "mol canonical SMILES" + "\n")
        continue
    temp = line.strip().split("\t")
    try:
        cid = str(int(temp[2]))
        if cid in cids:
            outfile.write(line.strip() + "\t" + cids[cid] + "\t")
    except:
        outfile.write(line.strip() + "\t\t\t\t\t" )
    if temp[0] in mols:
        outfile.write(mols[temp[0]] + "\n")
    else:
        outfile.write("\n")
outfile.close()
infile.close()
