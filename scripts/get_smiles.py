import os
path = os.getcwd()
os.chdir("mol-files")
sdfs = os.listdir(os.getcwd())
os.chdir(path)
for elem in sdfs:
    if elem.endswith(".mol"):
        #babel -isdf infile.sdf -ocan outfile.smi -b
        os.system("babel -isdf mol-files/" + elem + " -ocan ../smiles/" + elem.replace("mol","smi") + " -b")
    else:
        print(elem)