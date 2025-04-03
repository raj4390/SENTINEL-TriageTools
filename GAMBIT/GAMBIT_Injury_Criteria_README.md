
## GAMBIT Injury Criteria Calculation

The **GAMBIT (Generalized Acceleration Model for Brain Injury Threshold)** Injury Criteria is calculated using the following formula:

```
G = (a_m^n + a_r^m)^(1/s)
```

Where:
- `a_m` is the translational acceleration,
- `a_r` is the rotational acceleration,
- `n`, `m`, and `s` are empirical constants that can be adjusted based on data. For a linear combination, `n = m = s = 1`.

The GAMBIT injury criterion combines the effects of both translational and rotational accelerations to evaluate the likelihood of brain injury. The model proposes that brain injury occurs when the combined effect of these accelerations exceeds a certain threshold.

---

### **How the Code Works**

This script calculates the **GAMBIT Injury Criterion** from both translational and rotational acceleration data collected over time. The script processes the data, filters noise, and computes the GAMBIT value through numerical integration. The results can be used to evaluate the risk of brain injury during impact events.

---

### **Workflow Explanation**

#### 1. Input Data and Configuration
The script accepts inputs via command-line arguments, including:
- **Sampling frequency**: The time interval between successive data points.
- **Path to the CSV file**: The file containing raw acceleration data.
- **Column indices**: Identifiers for the columns containing translational and rotational acceleration data.

Example:
```bash
python Gambit_Calculator.py --frequency 0.001 --file_path "data.csv" --x_location 2 --y_location 3 --z_location 4
```

#### 2. Data Preprocessing
The script reads the input CSV file and extracts acceleration data. It calculates the time at each data point using the provided sampling frequency and computes the magnitude of acceleration as:

\[ 
	ext{magnitude} = rac{\sqrt{x^2 + y^2 + z^2}}{9810} 
\]

This formula converts acceleration to G-forces, dividing by 9810 (gravity constant in mm/s²).

#### 3. Butterworth Low-Pass Filtering
To reduce noise and high-frequency components, the script applies a Butterworth low-pass filter:
- **Cutoff Frequency**: 1650 Hz (default).
- **Order**: 2 (default).

#### 4. GAMBIT Calculation
The script calculates the **GAMBIT** value using both translational and rotational acceleration data. It integrates the accelerations based on the formula:

\[G = (a_m^n + a_r^m)^{1/s}
\]

#### 5. Output Results
The script prints the calculated GAMBIT value to the terminal:

Example Output:
```
The GAMBIT Injury Criterion (G) value is: 1.20
```

---

### **Example Workflow**

**Input CSV** (Sample rows):
```csv
X,Y,Z
1.23,-0.45,0.67
1.30,-0.50,0.72
...
```

**Command**:
```bash
python Gambit_Calculator.py --frequency 0.001 --file_path "data.csv" --x_location 1 --y_location 2 --z_location 3
```

**Output**:
```
The GAMBIT Injury Criterion (G) value is: 1.15
```

---

### **Flowchart**
```plaintext
  +-------------------------------------+
  | Start                               |
  +-------------------------------------+
               |
               v
  +-------------------------------------+
  | Parse arguments                     |
  | (frequency, file_path, x, y, z)     |
  +-------------------------------------+
               |
               v
  +-------------------------------------+
  | Read and process CSV data           |
  | (calculate time, magnitude, filter) |
  +-------------------------------------+
               |
               v
  +-------------------------------------+
  | Calculate translational and         |
  | rotational accelerations             |
  +-------------------------------------+
               |
               v
  +-------------------------------------+
  | Perform numerical integration       |
  +-------------------------------------+
               |
               v
  +-------------------------------------+
  | Output GAMBIT value                 |
  +-------------------------------------+
               |
               v
  +-------------------------------------+
  | End                                 |
  +-------------------------------------+
```

---

### **Reference**
1. Newman, J.A. (1986). A Generalized Acceleration Model for Brain Injury Threshold (GAMBIT). Biokinetics and Associates Limited.
