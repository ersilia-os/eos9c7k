# Similarity search in ChEMBL, DrugBank and UNPD

Given a molecule, this model for its 100 nearest neighbors, according to ECFP4 Tanimoto similarity, in the medicinal chemistry database ChEMBL17\_DrugBank17\_UNPD17. This combined database contains all the compounds from the three collections (DrugBank, ChEMBL22 and Universal natural product directory (UNPD)) with up to 17 heavy atoms. It features a total of 128k compounds. The whole ChEMBL17\_DrugBank17\_UNPD17 database is not downloaded with the model, by using it you post queries to an online server external to Ersilia.

## Identifiers

* EOS model ID: `eos9c7k`
* Slug: `medchem17-similarity`

## Characteristics

* Input: `Compound`
* Input Shape: `Single`
* Task: `Similarity`
* Output: `Compound`
* Output Type: `String`
* Output Shape: `List`
* Interpretation: List of 100 nearest neighbors

## References

* [Publication](https://onlinelibrary.wiley.com/doi/abs/10.1002/minf.201900031)
* [Source Code](https://gdb-medchem-simsearch.gdb.tools/)
* Ersilia contributor: [Amna-28](https://github.com/Amna-28)

## Ersilia model URLs
* [GitHub](https://github.com/ersilia-os/eos9c7k)
* [AWS S3](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos9c7k.zip)
* [DockerHub](https://hub.docker.com/r/ersiliaos/eos9c7k) (AMD64, ARM64)

## Citation

If you use this model, please cite the [original authors](https://onlinelibrary.wiley.com/doi/abs/10.1002/minf.201900031) of the model and the [Ersilia Model Hub](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff).

## License

This package is licensed under a GPL-3.0 license. The model contained within this package is licensed under a None license.

Notice: Ersilia grants access to these models 'as is' provided by the original authors, please refer to the original code repository and/or publication if you use the model in your research.

## About Us

The [Ersilia Open Source Initiative](https://ersilia.io) is a Non Profit Organization ([1192266](https://register-of-charities.charitycommission.gov.uk/charity-search/-/charity-details/5170657/full-print)) with the mission is to equip labs, universities and clinics in LMIC with AI/ML tools for infectious disease research.

[Help us](https://www.ersilia.io/donate) achieve our mission!