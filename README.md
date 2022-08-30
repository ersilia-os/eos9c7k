# Similarity search in the 17-subsets of ChEMBL, DrugBank and UNPD
## Model identifiers
- Slug: medchem17-similarity
- Ersilia ID: eos9c7k
- Tags: Similarity

# Model description
Look for 100 nearest neighbors, according to ECFP4 Tanimoto similarity, medicinal chemistry database 17-subsets of ChEMBL, DrugBank and UNPD.
- Input: SMILES 
- Output: SMILES 
- Model type: Generative
- Training set: 
- Mode of training: Online

# Source code
- Code: The model uses the web application available at https://gdb-medchem-simsearch.gdb.tools/
- Checkpoints: N/A

# License
The GPL-v3 license applies to all parts of the repository.

# History 
- We have developed a python script that accesses the web server available at https://gdb-medchem-simsearch.gdb.tools/ to run the predictions.
- `requests` and `BeautifulSoup` libraries are used to post the input to the server and fetch the results.
- Model was incorporated to Ersilia on 8/22/2022

# About us
The [Ersilia Open Source Initiative](https://ersilia.io) is a Non Profit Organization ([1192266](https://register-of-charities.charitycommission.gov.uk/charity-search/-/charity-details/5170657/full-print)) with the mission is to equip labs, universities and clinics in LMIC with AI/ML tools for infectious disease research.

[Help us](https://www.ersilia.io/donate) achieve our mission or [volunteer](https://www.ersilia.io/volunteer) with us!
