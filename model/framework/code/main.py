from bs4 import BeautifulSoup
import requests
import csv
import sys
import urllib

# Input Parameters
input_file = open(sys.argv[1], 'r')
Lines = input_file.readlines()[1:]
fp     = 'ECfp4'
db     = 'ChEMBL17_DrugBank17_UNPD17'
nnc    = '100'

data = []
for input_smiles in Lines:
    input_smiles = input_smiles.strip() 
    url_encoded_smiles = urllib.parse.quote(input_smiles)
    url = 'https://gdb-chembl-simsearch.gdb.tools/search?smi=' + url_encoded_smiles +  '&fp=' + fp + '&db=' + db + '&nnc=' + nnc
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
        x1 = x[1].split(" ")
        x2 = x1[0]
        smiles_list.append(x2.strip(' ')) 
        similarity_indices.append(float(x[3].strip('\"')))
    paired = list(zip(smiles_list, similarity_indices))
    paired.sort(key=lambda x: (-x[1], x[0]))
    sorted_smiles_list = [smi for smi, _ in paired]
    sorted_similarity_indices = [sim for _, sim in paired]
    data += [[sorted_smiles_list, sorted_similarity_indices]]

header = [f"smiles_{i:02}" for i in range(len(smiles_list))]
with open(sys.argv[2], 'w') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    for d in data:
        writer.writerow(d[0])