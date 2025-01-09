### Validation of HIC Script

The validation of the Head Injury Criterion (HIC) script was conducted using a standard 4.5 kg headform model impacting a flat surface at an angle of 40 degrees and a speed of 40 km/h. The material thickness was varied from **0.2 mm to 2.5 mm**, and the corresponding head acceleration was recorded using the **OpenRadioss explicit solver**.

The calculated HIC values from the script were compared to those obtained from HyperGraph. The results of this comparison are summarized below:

| **Thickness (mm)** | **Script** | **HyperGraph** | **% Difference** |
|---------------------|------------|----------------|-------------------|
| 0.2                 | 441        | 457            | 3.50%            |
| 0.4                 | 1066       | 1082           | 1.48%            |
| 0.50                | 1213       | 1213           | 0.00%            |
| 0.60                | 1287       | 1287           | 0.00%            |
| 0.80                | 1417       | 1417           | 0.00%            |
| 1.00                | 1488       | 1488           | 0.00%            |
| 1.50                | 1635       | 1635           | 0.00%            |
| 1.53                | 1644       | 1648           | 0.24%            |
| 2.00                | 1815       | 1816           | 0.06%            |
| 2.50                | 1985       | 1986           | 0.05%            |

The comparison indicates that the HIC values calculated by the script closely match those obtained from HyperGraph, with negligible differences for most thicknesses. The maximum percentage difference observed was **3.50%** at a thickness of **0.2 mm**.
