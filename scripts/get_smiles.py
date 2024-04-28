import os
path = os.getcwd()
os.chdir("mol-files")
sdfs = os.listdir(os.getcwd())
os.chdir(path)
for elem in sdfs:
    if elem.endswith(".mol"):
        #babel -isdf infile.sdf -ocan outfile.smi -b
        try: #try except for uses with babel vs open babel v3 or higher
            os.system("babel -isdf mol-files/" + elem + " -ocan smiles/" + elem.replace("mol","smi") + " -b")

        except:
            os.system("obabel -isdf mol-files/" + elem + " -O smiles/" + elem.replace("mol","smi") + " -b")
    else:
        print(elem)