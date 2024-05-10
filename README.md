# Merge Smiles Files

This repository contains a script used to merge two smiles (.smi) files into a single csv file. One file contains manually-drawn molecules and the other smiles obtained from PubChem.

The `/data` folder contains example files to run the pipeline.
The original input file, in this example `01_NA_Family_A_Smiles.csv` contains all the molecules we want to concatenate, both the ones from PubChem (with PubChem ID) and the manually drawn.

## Usage
To use this repository, just clone it and follow the commands below. To process sdf files, you will need to install Open Babel.

### 1. Extract SMILEs from sdf files 
Get sdf files from PubChem using a list of PubChem IDs:

```
mkdir sdfs #create a folder to store the sdf files
python scripts/download_sdfs.py # prepare the download.sh file
OR
python3 scripts/download_sdfs.py # for WSL and Ubuntu users
bash scripts/download.sh  # download sdf files
cat sdfs/* > sdfs/structures.sdf # get all individual sdf files into one
babel -isdf sdfs/structures.sdf -ocan data/pubchem_smiles.smi -b #concatenate SMILES from the SDF file into a single .smi file
OR
obabel -isdf sdfs/structures.sdf -O data/pubchem_smiles.smi -b # for users running OpenBabel v3 or higher
```

### 2. Extract SMILES from manually drawn molecules
To obtain the SMILES from the `mol-files` simply run:

```
#use the file mol-files.rar from Fidele and extract the files into the folder mol-files
#place the mol-files folder in this repository
mkdir smiles
python scripts/get_smiles.py #this will extract the mol file as a .smi file
OR
python3 scripts/get_smiles.py # for WSL and Ubuntu users
cat smiles/* > data/mol_smiles.smi #concatenate all SMILES into a single file
```
You should have a mol-files folder in the root of the repository with the files you want to process, and you will get a mol_smiles.smi file as output

### 3. Merge SMILES files

To obtain a csv file with the molecules identified by their Compound Code and their PubChem CID (if available) and the SMILES from either the PubChem download or the manual files, run the following:

```
python scripts/merge_smiles.py
OR
python3 scripts/merge_smiles.py # for WSL and Ubuntu users 
```
