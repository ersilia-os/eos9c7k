# Similarity search in ChEMBL, DrugBank and UNPD

Finds the 100 structures most similar to a query in a merged medicinal chemistry index of 128,011 molecules with at most 17 heavy atoms, assembled by Awale and colleagues from ChEMBL 22 (105,423 compounds), DrugBank (2,284) and the Universal Natural Product Database (20,302). Because bioactive, approved and natural product chemistry sit in one index, a hit may come from any of the three, which helps when looking for precedent across chemical traditions. Ranking uses ECFP4 similarity, with approximate nearest-neighbour search run on a remote server.

This model was incorporated on 2022-08-18.Last packaged on 2026-09-01.

## Information
### Identifiers
- **Ersilia Identifier:** `eos9c7k`
- **Slug:** `medchem17-similarity`

### Domain
- **Task:** `Sampling`
- **Subtask:** `Similarity search`
- **Biomedical Area:** `Any`
- **Target Organism:** `Any`
- **Tags:** `Similarity`, `ChEMBL`, `DrugBank`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `100`
- **Output Consistency:** `Fixed`
- **Interpretation:** 100 nearest neighbours by ECFP4 similarity in a 128,011-molecule ChEMBL, DrugBank and natural product index.

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| smi_00 | string |  | Sampled smiles 0 from a similarity search in ChEMBL17_DrugBank17_UNPD17 |
| smi_01 | string |  | Sampled smiles 1 from a similarity search in ChEMBL17_DrugBank17_UNPD17 |
| smi_02 | string |  | Sampled smiles 2 from a similarity search in ChEMBL17_DrugBank17_UNPD17 |
| smi_03 | string |  | Sampled smiles 3 from a similarity search in ChEMBL17_DrugBank17_UNPD17 |
| smi_04 | string |  | Sampled smiles 4 from a similarity search in ChEMBL17_DrugBank17_UNPD17 |
| smi_05 | string |  | Sampled smiles 5 from a similarity search in ChEMBL17_DrugBank17_UNPD17 |
| smi_06 | string |  | Sampled smiles 6 from a similarity search in ChEMBL17_DrugBank17_UNPD17 |
| smi_07 | string |  | Sampled smiles 7 from a similarity search in ChEMBL17_DrugBank17_UNPD17 |
| smi_08 | string |  | Sampled smiles 8 from a similarity search in ChEMBL17_DrugBank17_UNPD17 |
| smi_09 | string |  | Sampled smiles 9 from a similarity search in ChEMBL17_DrugBank17_UNPD17 |

_10 of 100 columns are shown_
### Source and Deployment
- **Source:** `Online`
- **Source Type:** `External`
- **DockerHub**: [https://hub.docker.com/r/ersiliaos/eos9c7k](https://hub.docker.com/r/ersiliaos/eos9c7k)
- **Docker Architecture:** `AMD64`, `ARM64`
- **S3 Storage**: [https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos9c7k.zip](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos9c7k.zip)

### Resource Consumption
- **Model Size (Mb):** `1`
- **Environment Size (Mb):** `315`
- **Image Size (Mb):** `315.95`

**Computational Performance (seconds):**
- 10 inputs: `39.17`
- 100 inputs: `277.45`
- 10000 inputs: `-1`

### References
- **Source Code**: [https://gdb-medchem-simsearch.gdb.tools/](https://gdb-medchem-simsearch.gdb.tools/)
- **Publication**: [https://doi.org/10.1002/minf.201900031](https://doi.org/10.1002/minf.201900031)
- **Publication Type:** `Peer reviewed`
- **Publication Year:** `2019`
- **Ersilia Contributor:** [Amna-28](https://github.com/Amna-28)

### License
This package is licensed under a [GPL-3.0](https://github.com/ersilia-os/ersilia/blob/master/LICENSE) license. The model contained within this package is licensed under a [None](LICENSE) license.

**Notice**: Ersilia grants access to models _as is_, directly from the original authors, please refer to the original code repository and/or publication if you use the model in your research.


## Use
To use this model locally, you need to have the [Ersilia CLI](https://github.com/ersilia-os/ersilia) installed.
The model can be **fetched** using the following command:
```bash
# fetch model from the Ersilia Model Hub
ersilia fetch eos9c7k
```
Then, you can **serve**, **run** and **close** the model as follows:
```bash
# serve the model
ersilia serve eos9c7k
# generate an example file
ersilia example -n 3 -f my_input.csv
# run the model
ersilia run -i my_input.csv -o my_output.csv
# close the model
ersilia close
```

## About Ersilia
The [Ersilia Open Source Initiative](https://ersilia.io) is a tech non-profit organization fueling sustainable research in the Global South.
Please [cite](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff) the Ersilia Model Hub if you've found this model to be useful. Always [let us know](https://github.com/ersilia-os/ersilia/issues) if you experience any issues while trying to run it.
If you want to contribute to our mission, consider [donating](https://www.ersilia.io/donate) to Ersilia!
