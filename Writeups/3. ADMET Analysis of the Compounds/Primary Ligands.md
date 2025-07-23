# Primary Ligand ADMET Analysis 

## Comparative Analysis of all 3 Ligands

| Property                           | 1,8-Naphthyridine-3-carboxamide | Carnosic Acid   | Carnosol                |
| ---------------------------------- | ------------------------------- | --------------- | ----------------------- |
| **Molecular Weight (g/mol)**       | 173.16                          | 332.42          | 330.45                  |
| **LogP (iLOGP)**                   | 1.55                            | 4.01            | 3.88                    |
| **TPSA (Å²)**                      | 66.41                           | 80.92           | 60.69                   |
| **H-Bond Donors**                  | 2                               | 3               | 2                       |
| **H-Bond Acceptors**               | 3                               | 4               | 3                       |
| **Rotatable Bonds**                | 2                               | 5               | 3                       |
| **Lipinski Rule Violations**       | 0                               | 0               | 0                       |
| **Ghose Filter**                   |  Yes                          |  Yes          |  Yes                  |
| **Veber Rule**                     |  Yes                          |  Yes          |  Yes                  |
| **Bioavailability Score**          | 0.55                            | 0.55            | 0.55                    |
| **PAINS Alerts**                   | 0                               | 0               | 0                       |
| **Synthetic Accessibility**        | 2.57                            | 4.14            | 3.87                    |
| **GI Absorption**                  | High                            | High            | High                    |
| **BBB Permeant**                   | No                              | No              | No                      |
| **P-gp Substrate**                 | No                              | No              | No                      |
| **CYP Inhibition**                 | None                            | CYP1A2, CYP2C19 | CYP1A2, CYP2C19, CYP3A4 |
| **Hepatotoxicity (pkCSM)**         | No                              | No              | No                      |
| **Skin Sensitization**             | No                              | No              | No                      |
| **AMES Toxicity**                  | No                              | No              | No                      |
| **Oral Rat Acute Toxicity (LD50)** | 2.33 mol/kg                     | 2.27 mol/kg     | 2.17 mol/kg             |

## Comparative Evaluation

### 1,8-Naphthyridine-3-Carboxamide 
This molecule exhibits a very favorable drug-likeness profile. It passes all major filters (Lipinski, Ghose, Veber, Egan, Muegge), has a reasonable logP (1.74), and a low synthetic accessibility score (2.29), indicating ease of synthesis. It only triggers one PAINS and one Brenk alert, which should be monitored in further stages. The bioavailability score of 0.55 is acceptable for early-stage drug candidates. Overall, this **molecule is well-suited for progression into docking and virtual screening**.

### Carnosic Acid
Carnosic acid shows limitations across several metrics. It violates Lipinski’s rule (likely due to high molecular weight and TPSA), and fails all major filters except PAINS. The TPSA of 133.45 Å² is quite high, indicating possible issues with permeability. The synthetic accessibility score is also high (6.79), indicating potential synthetic complexity. However, it has no PAINS alerts, which is a positive sign. This compound might still be viable for docking but is **less drug-like and requires structural optimization**.

### Carnosol
Carnosol displays a similar profile to carnosic acid. It also violates Lipinski, Ghose, and Veber rules and fails the Muegge and Egan filters. While its TPSA (120.92 Å²) is slightly better than that of carnosic acid, it still suggests permeability concerns. The synthetic accessibility score of 5.99 also points to moderate complexity. Despite its natural origin and lack of PAINS alerts, it is **not ideal as a lead compound without optimization**.

> Hence, among primary ligands, only 1,8-Naphthyridine-3-carboxamide, and Carnosic Acid are to be considered for further analysis. 

