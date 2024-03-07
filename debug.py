import pandas as pd

df = pd.read_csv("01_NA_Family_A_Smiles.csv")

df = df.head(10)
df.to_csv("inp_smi.csv", index=False)