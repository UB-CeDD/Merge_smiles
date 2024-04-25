#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#Kersten Doering 28.07.2015
import csv

# Get CIDS from PUBCHEM 
cids = {}
infile = open("data/pubchem_smiles.smi","r")
for line in infile:
    temp = line.strip().split("\t")
    cids[temp[1]] = temp[0]
infile.close()

mols = {}
infile = open("data/mol_smiles.smi","r")
for line in infile:
    temp = line.strip().split("\t")
    mols[temp[1].replace(".mol","")] = temp[0]
infile.close()

infile = 'data/01_NA_Family_A_Smiles.csv'
outfile = "data/01_NA_Family_A_Smiles-o.csv"

with open(infile, 'r', newline='') as in_file:
    reader = csv.reader(in_file)
    header = next(reader) # we skip the header of the file
    lines = []
    for line in reader:
        if line[0] == "": #we are only keeping the lines that have a molecule code
            continue
        else:
            cid = line[1]
            print(cid)
            if cid in cids.keys():
                smi = cids[cid]
                line[2] = smi #add the smiles in position 3 of the line, PubChem smiles
            cc = line[0]
            if cc in mols.keys():
                smi = mols[cc]
                line[3] = smi
        lines += [line]

with open(outfile, 'w', newline='') as out_file:
    writer = csv.writer(out_file)
    writer.writerow(header)  # Write the header
    writer.writerows(lines)  # Write the rest of the data



"""

infile = open("01_NA_Family_A_Smiles.csv","r") #change with name from input file
outfile = open("01_NA_Family_A_Smiles-o.csv","w")



with open('inp_smi.csv', 'r', newline='') as in_file:
    reader = csv.reader(in_file)
    # skip header
    next(reader)
    for line in reader:
        print(line)
        if "PubChem Non canonical SMILES" in line:
            outfile.write("\t\t\t\t" + line.strip() + "\t" + "PubChem canonical SMILES" + "\t" + "mol canonical SMILES" + "\n")
            continue
        #temp = line.strip().split(",")
        cid = line[1]
        if cid != "":
            cid = int(float(cid))
        if str(cid) in cids.keys():
            smi = cids[str(cid)]
            #Here we need to save the smiles into the output file
            #outfile.write(line.strip() + "\t" + cids[cid] + "\t")
        else:
            continue
            #outfile.write(line.strip() + "\t\t\t\t\t" )

        cc = line[0]
        print(cc)
        print(type(cc))
        if cc in mols.keys():
            print("HERE")
            outfile.write(mols[temp[0]] + "\n")
        else:
            outfile.write("\n")
outfile.close()
infile.close()
"""