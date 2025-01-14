### Severity Index (SI)

The SI, introduced by Gadd (1966), aimed to address the limitation of the WSTC by incorporating acceleration magnitude. It operates on the premise that the severity of the head injury depends on both the acceleration and the duration of the pulse. The SI is defined as:

$$ SI =\int_{}^{}a^n \, dt $$

Where, $a$ is head acceleration, $n$ is chosen to be 2.5 based on the straight-line approximation of the slope of WSTC, and $t$ is time in seconds. An SI value of 1000 corresponds to a 50% probability of injury occurrence. However, some critiques of the SI argue that the straight-line approximation to arrive at n = 2.5 may not be the most appropriate fit, and there is no necessity for the fitted line to be linear (Hodgson et al., 1970).

---

### How the Code Works

This script calculates the **Severity Index (SI)** from acceleration data collected over time. It incorporates preprocessing, filtering, and SI computation through numerical integration. The workflow ensures the results are accurate and applicable to real-world scenarios.

---

### Workflow Explanation

#### 1. Input Data and Configuration
The script accepts inputs via command-line arguments, including:
- **Sampling frequency**: The time interval between successive data points.
- **Path to the CSV file**: The file containing raw acceleration data.
- **Column indices**: Identifiers for the columns containing X, Y, and Z acceleration data.

Example:
```bash
python si_calculator.py --frequency 0.001 --file_path "data.csv" --x_location 2 --y_location 3 --z_location 4
```

---

#### 2. Data Preprocessing
The script reads the input CSV file and extracts acceleration data. It calculates the time at each data point using the provided sampling frequency and computes the magnitude of acceleration as:

\[
\text{magnitude} = \frac{\sqrt{x^2 + y^2 + z^2}}{9810}
\]

This formula converts acceleration to G-forces, dividing by 9810 (gravity constant in mm/s²).

---

#### 3. Butterworth Low-Pass Filtering
To reduce noise and high-frequency components, the script applies a Butterworth low-pass filter:
- **Cutoff Frequency**: 1650 Hz (default).
- **Order**: 2 (default).

Filtering ensures that the acceleration data reflects realistic physical phenomena.

---

#### 4. Severity Index Calculation
The script calculates SI by:
- Raising each acceleration magnitude to the power of 2.5.
- Performing numerical integration using the trapezoidal rule:

\[
SI = \sum_{i=1}^{N-1} 0.5 \cdot (t_{i+1} - t_{i}) \cdot \left(a(t_{i})^{2.5} + a(t_{i+1})^{2.5}\right)
\]

Where \(N\) is the total number of time points.

---

#### 5. Output Results
The script prints the calculated SI value to the terminal:

Example Output:
```
The Severity Index (SI) value is: 23.56
```

---

### Example Workflow

**Input CSV** (Sample rows):
```csv
X,Y,Z
1.23,-0.45,0.67
1.30,-0.50,0.72
...
```

**Command**:
```bash
python si_calculator.py --frequency 0.001 --file_path "data.csv" --x_location 1 --y_location 2 --z_location 3
```

**Output**:
```
The Severity Index (SI) value is: 45.67
```

---

### Flowchart
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
  | Calculate acceleration power        |
  | (raise to 2.5)                      |
  +-------------------------------------+
               |
               v
  +-------------------------------------+
  | Perform numerical integration       |
  +-------------------------------------+
               |
               v
  +-------------------------------------+
  | Output SI value                     |
  +-------------------------------------+
               |
               v
  +-------------------------------------+
  | End                                 |
  +-------------------------------------+
```

---

### Reference
1. Gadd, C. W. (1966). Use of a weighted-impulse criterion for estimating injury hazard. SAE Technical Papers. https://doi.org/10.4271/660793
2. Hodgson, V. R., Thomas, L. M., & Prasad, P. (1970). Testing the validity and limitations of the severity index. SAE Technical Papers, 79, 2672–2684. https://doi.org/10.4271/700901
