# Ligand Selection from Literature Review 

## Secondary Ligands 

To broaden the chemical landscape surrounding the primary hits, secondary ligands were identified using the ChEMBL web resource client, with Tanimoto similarity employed as the basis for compound selection. A threshold of 0.50 was applied to allow moderate structural flexibility while retaining core molecular features, facilitating the exploration of potentially diverse yet functionally relevant analogs. This similarity-based expansion was initiated from three primary ligands, resulting in a set of eighteen secondary ligands. Such an approach is commonly used in early-stage drug discovery to identify structurally related candidates that may exhibit comparable binding profiles or biological activity.

The code used to obtain the similar molecules is present in the following link: [Link](Code/ligand_selection/ligand_selection.ipynb) 

### Similar compounds to 1,8-Naphthyridine-3-carboxamide (retrieved via ChEMBL Web Resource Client API)

| **ChEMBL ID** | **Similarity (%)** | **SMILES**             |
| ------------- | ------------------ | ---------------------- |
| CHEMBL216226  | 60.00              | `NC(=O)c1cnc2ccccc2c1` |

### Similar compounds to Carnosic acid (retrieved via ChEMBL Web Resource Client API)

| **ChEMBL ID** | **Similarity (%)** | **SMILES**                                                                           |
| ------------- | ------------------ | ------------------------------------------------------------------------------------ |
| CHEMBL4868012 | 80.39              | `COc1c(C(C)C)cc2c(c1O)[C@]1(C(=O)O)CCCC(C)(C)[C@@H]1CC2`                             |
| CHEMBL1096627 | 80.39              | `COc1c(C(C)C)cc2c(c1O)[C@@]1(C(=O)O)CCCC(C)(C)[C@@H]1CC2`                            |
| CHEMBL4471445 | 78.00              | `CNC(=O)[C@]12CCCC(C)(C)[C@@H]1CCc1cc(C(C)C)c(O)c(O)c12`                             |
| CHEMBL2333537 | 78.00              | `COC(=O)[C@]12CCCC(C)(C)[C@@H]1CCc1cc(C(C)C)c(O)c(O)c12`                             |
| CHEMBL4519804 | 76.47              | `CC(C)c1cc2c(c(O)c1O)[C@@]1(C(=O)NN)CCCC(C)(C)[C@@H]1CC2`                            |
| CHEMBL4515503 | 75.00              | `CC(=O)NC(=O)[C@]12CCCC(C)(C)[C@@H]1CCc1cc(C(C)C)c(O)c(O)c12`                        |
| CHEMBL4574206 | 73.58              | `CC(C)c1cc2c(c(O)c1O)[C@@]1(C(=O)NC(N)=O)CCCC(C)(C)[C@@H]1CC2`                       |
| CHEMBL4451825 | 72.22              | `CC(C)c1cc2c(c(O)c1O)[C@@]1(C(=O)NC3CCCCCC3)CCCC(C)(C)[C@@H]1CC2`                    |
| CHEMBL4471914 | 70.91              | `CC(C)c1cc2c(c(O)c1O)[C@@]1(C(=O)NCCO)CCCC(C)(C)[C@@H]1CC2`                          |
| CHEMBL4447764 | 68.97              | `CC(C)c1cc2c(c(O)c1O)[C@@]1(C(=O)NCc3ccccc3)CCCC(C)(C)[C@@H]1CC2`                    |
| CHEMBL4468065 | 67.24              | `CC(C)c1cc2c(c(O)c1O)[C@@]1(C(=O)NCCN(C)C)CCCC(C)(C)[C@@H]1CC2`                      |
| CHEMBL221380  | 66.07              | `COC(=O)[C@]12CCCC(C)(C)[C@@H]1CCc1cc(C(C)C)c(OC)c(O)c12`                            |
| CHEMBL2376099 | 65.38              | `CC(C)c1cc2c(c(O)c1O)[C@@]1(C=O)CCCC(C)(C)[C@@H]1CC2`                                |
| CHEMBL4447390 | 65.00              | `CC(C)c1cc2c(c(O)c1O)[C@@]1(C(=O)NC(=O)c3ccc(Br)cc3)CCCC(C)(C)[C@@H]1CC2`            |
| CHEMBL479111  | 63.64              | `COc1cc2c(cc1C(C)C)CC[C@H]1C(C)(C)CCC[C@]21C(=O)O`                                   |
| CHEMBL4576693 | 63.46              | `CC(C)c1cc2c(c(O)c1O)[C@@]1(CO)CCCC(C)(C)[C@@H]1CC2`                                 |
| CHEMBL4544242 | 60.94              | `CC(C)c1cc2c(c(O)c1O)[C@@]1(C(=O)NC(=O)[C@H](C)NC(=O)OC(C)(C)C)CCCC(C)(C)[C@@H]1CC2` |
| CHEMBL4436108 | 60.00              | `CC(C)c1cc2c(c(O)c1O)[C@@]1(C(=O)NCc3cccnc3)CCCC(C)(C)[C@@H]1CC2`                    |
| CHEMBL2374044 | 100.00             | `CC(C)c1cc2c(c(O)c1O)[C@]1(C(=O)O)CCCC(C)(C)C1CC2`                                   |
| CHEMBL484853  | 100.00             | `CC(C)c1cc2c(c(O)c1O)[C@@]1(C(=O)O)CCCC(C)(C)[C@@H]1CC2`                             |
| CHEMBL5407683 | 100.00             | `CC(C)c1cc2c(c(O)c1O)[C@@]1(C(=O)O)CCCC(C)(C)C1CC2`                                  |

### Similar compounds to Carnosol (retrieved via ChEMBL Web Resource Client API)

| **ChEMBL ID** | **Similarity (%)** | **SMILES**                                                           |
| ------------- | ------------------ | -------------------------------------------------------------------- |
| CHEMBL483017  | 82.35              | `CC1(C)CCC[C@@]23C(=O)OC(C[C@@H]12)c1cc(C(CO)CO)c(O)c(O)c13`         |
| CHEMBL491307  | 82.35              | `CC(CO)c1cc2c(c(O)c1O)[C@@]13CCCC(C)(C)[C@@H]1C[C@@H]2OC3=O`         |
| CHEMBL478933  | 73.58              | `COc1c(C(C)C)cc2c(c1OC)[C@@]13CCCC(C)(C)[C@@H]1C[C@@H]2OC3=O`        |
| CHEMBL1079367 | 66.07              | `C[C@H]1COc2c1cc1c(c2O)[C@@]23CCCC(C)(C)[C@@H]2C[C@@H]1OC3=O`        |
| CHEMBL2376097 | 64.81              | `CC(C)c1cc2c(c(O)c1O)[C@@]13CCCC(C)(C)[C@@H]1[C@H](OC3=O)[C@@H]2O`   |
| CHEMBL2333536 | 64.81              | `CC(C)c1cc2c(c(O)c1O)[C@@]13CCCC(C)(C)[C@@H]1[C@H](O)[C@@H]2OC3=O`   |
| CHEMBL507166  | 64.81              | `CC(C)c1cc2c(c(O)c1O)[C@@]13CCCC(C)(C)[C@@H]1[C@H](OC3=O)[C@H]2O`    |
| CHEMBL494659  | 64.81              | `CC(C)c1cc2c(c(O)c1O)[C@@]13CCCC(C)(C)[C@@H]1[C@@H](O)[C@@H]2OC3=O`  |
| CHEMBL1081338 | 61.40              | `CO[C@@H]1c2cc(C(C)C)c(O)c(O)c2[C@@]23CCCC(C)(C)[C@@H]2[C@@H]1OC3=O` |
| CHEMBL464376  | 61.40              | `CO[C@H]1c2cc(C(C)C)c(O)c(O)c2[C@@]23CCCC(C)(C)[C@@H]2[C@@H]1OC3=O`  |
| CHEMBL4544522 | 61.11              | `CC(C)c1cc2c(c(O)c1O)[C@@]13CCCC(C)(C)[C@@H]1CC2OC3`                 |
| CHEMBL491879  | 61.11              | `CC(C)c1cc2c(c(O)c1O)[C@@]13CCCC(C)(C)[C@@H]1C[C@@H]2OC3`            |
| CHEMBL1514916 | 100.00             | `CC(C)c1cc2c(c(O)c1O)[C@@]13CCCC(C)(C)C1CC2OC3=O`                    |
| CHEMBL519970  | 100.00             | `CC(C)c1cc2c(c(O)c1O)[C@@]13CCCC(C)(C)[C@@H]1CC2OC3=O`               |
| CHEMBL218693  | 100.00             | `CC(C)c1cc2c(c(O)c1O)[C@@]13CCCC(C)(C)[C@@H]1C[C@@H]2OC3=O`          |
