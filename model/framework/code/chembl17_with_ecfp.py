from bs4 import BeautifulSoup
import requests
import csv
import sys
# Input Parameters


input_file = open(sys.argv[1], 'r')
Lines = input_file.readlines()[1:]
fp     = 'ECfp4'
db     = 'ChEMBL17_DrugBank17_UNPD17'
nnc    = '100'

data = []
for input_smiles in Lines:
    input_smiles = input_smiles.strip() 
    url = 'https://gdb-chembl-simsearch.gdb.tools/search?smi=' + input_smiles +  '&fp=' + fp + '&db=' + db + '&nnc=' + nnc
    r = requests.get(url)
    soup = BeautifulSoup(r.text, features = 'html.parser')
    results = soup.find_all('script')
    T = str(results[-1]).splitlines()
    T = [i for i in T if not ('molData+' not in i)]
    del T[0]  # first row is input SMILE 
    smiles_list = []
    similarity_indices = []
    for i in T:
        x = i.split('+\"')
        x1 = x[1].split("molData+")
        x2 = x1[0]
        smiles_list.append(x2.strip(' ')) 
        similarity_indices.append(x[3].strip('\"'))
        
    data+= [[smiles_list, similarity_indices]]


header = ["sim-{0}".format(i+1) for i in range(len(smiles_list))]
with open(sys.argv[2], "w") as f:
    writer = csv.writer(f)
    writer.writerow(header)
    for d in data:
        writer.writerow(d[0])
