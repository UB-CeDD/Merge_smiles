# Merge Smiles Files

This repository contains a script used to merge two smiles (.smi) files into a single csv file. One file contains manually-drawn molecules and the other smiles obtained from PubChem.

The `/data` folder contains example files to run the pipeline.
The original input file, in this example `01_NA_Family_A_Smiles.csv` contains all the molecules we want to concatenate, both the ones from PubChem (with PubChem ID) and the manually drawn.

## Usage
To use this repository, clone it and create a conda environment with the requirements specified in requirements.txt. To process sdf files, you will need to install Open Babel.

### 1. Extract SMILEs from sdf files 
Get sdf files from PubChem using a list of PubChem IDs:
```
mkdir sdfs #create a folder to store the sdf files
python scripts/download_sdfs.py #prepare the download.sh file
chmod +x scripts/download.sh 
bash scripts/download.sh 
cat sdfs/* > structures.sdf #get all individual sdf files into one
babel -isdf sdfs/structures.sdf -ocan data/pubchem_smiles.smi -b #concatenate SMILES from the SDF file into a single .smi file
```

### 2. Extract SMILES from manually drawn molecules
To obtain the SMILES from the `mol-files` simply run:

```
#use the file mol-files.rar from Fidele and extract the files into a folder mol-files
mkdir smiles
python scripts/get_smiles.py #this will extract the mol file as a .smi file
cat smiles/* > mol_smiles.smi #concatenate all SMILES into a single file
```
You should have a mol-files folder in your root with the files you want to process, and you will get a mol_smiles.smi file as output

### 3. Merge SMILES files

```
python data/merge_smiles.py 
python data/compare_smiles.py
```