
## Head Impact Power (HIP) Calculation

The **Head Impact Power (HIP)** is calculated using the following formula:

```
HIP = ∫ (α_x * ω̇_x + α_y * ω̇_y + α_z * ω̇_z) dt
```

Where:
- `α_x`, `α_y`, `α_z` are the angular accelerations along the three axes (x, y, z),
- `ω̇_x`, `ω̇_y`, `ω̇_z` are the angular velocities along the three axes (x, y, z),
- `t` represents time.

This equation integrates the contributions from both **linear** and **rotational motion** to determine the rate of change in kinetic energy during a head impact event. The highest value of this power during the event is used to define the **maximum Head Impact Power (HIP)**, which is a critical measure for assessing the risk of head injury.

---

### **How the Code Works**

This script calculates the **Head Impact Power (HIP)** from acceleration data collected over time. It incorporates preprocessing, filtering, and HIP computation through numerical integration. The workflow ensures the results are accurate and applicable to real-world scenarios.

---

### **Workflow Explanation**

#### 1. Input Data and Configuration
The script accepts inputs via command-line arguments, including:
- **Sampling frequency**: The time interval between successive data points.
- **Path to the CSV file**: The file containing raw acceleration data.
- **Column indices**: Identifiers for the columns containing X, Y, and Z acceleration data.

Example:
```bash
python HIP_Calculator.py --frequency 0.001 --file_path "data.csv" --x_location 2 --y_location 3 --z_location 4
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

#### 4. Head Impact Power Calculation
The script calculates HIP using angular acceleration and velocity data along three axes. It integrates the contributions from each axis to compute the total power.

#### 5. Output Results
The script prints the calculated HIP value to the terminal:

Example Output:
```
The Head Impact Power (HIP) value is: 15.67 kW
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
python HIP_Calculator.py --frequency 0.001 --file_path "data.csv" --x_location 1 --y_location 2 --z_location 3
```

**Output**:
```
The Head Impact Power (HIP) value is: 12.34 kW
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
  | Calculate angular power terms       |
  | (raise to appropriate powers)       |
  +-------------------------------------+
               |
               v
  +-------------------------------------+
  | Perform numerical integration       |
  +-------------------------------------+
               |
               v
  +-------------------------------------+
  | Output HIP value                    |
  +-------------------------------------+
               |
               v
  +-------------------------------------+
  | End                                 |
  +-------------------------------------+
```

---

### **Reference**
1. Newman, J.A., Shewchenko, N., Welbourne, E. (2000). A Proposed New Biomechanical Head Injury Assessment Function - The Maximum Power Index. Stapp Car Crash Journal.
