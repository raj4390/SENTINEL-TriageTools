
## Head Impact Power (HIP) Calculation

The **Head Impact Power (HIP)** is a biomechanical metric that quantifies the rate of change in kinetic energy of the head during an impact event. The calculation of HIP is based on both **linear** and **rotational** motion, considering the accelerations and velocities along three axes (X, Y, Z). The highest value of HIP during the event is used to assess the likelihood of head injury.

---

### **Formula for HIP Calculation**

The **HIP** is calculated using the following formula:

$$HIP = \int \left( \alpha_x \cdot \dot{\omega}_x + \alpha_y \cdot \dot{\omega}_y + \alpha_z \cdot \dot{\omega}_z \right) dt$$

Where:
- \( lpha_x, lpha_y, lpha_z \) are the **angular accelerations** along the three axes (X, Y, Z),
- \( \dot{\omega}_x, \dot{\omega}_y, \dot{\omega}_z \) are the **angular velocities** along the three axes (X, Y, Z),
- \( t \) represents **time**.

This equation integrates the contributions from both **linear** and **rotational motion** to determine the **rate of change** in kinetic energy during the impact event. The **maximum** value of this power is used to define the **maximum Head Impact Power (HIP)**.

---

### **Background**

The concept of Head Impact Power (HIP) is grounded in the idea that the probability of head injury is closely related to the **rate of change in kinetic energy** during an impact. This hypothesis was proposed by Newman and Shewchenko in 2000, and it is based on data from instrumented Hybrid III anthropomorphic test dummies, which simulate head impacts in various contexts (e.g., football players in head-to-head collisions). The **maximum** value of HIP during an impact event is used to assess the risk of head injury.

The core idea is that head injury severity correlates with the maximum rate at which kinetic energy is transferred to the head during an impact.

---

### **Data Requirements**

To calculate HIP, the following data is required:
1. **Angular accelerations** (\( lpha_x, lpha_y, lpha_z \)): These measure the rotational acceleration of the head along the three axes (X, Y, Z). They are usually recorded using accelerometers or motion capture systems.
2. **Angular velocities** (\( \dot{\omega}_x, \dot{\omega}_y, \dot{\omega}_z \)): These describe the rate of change of the angular displacement of the head. They are calculated from the acceleration data using integration.
3. **Time**: The time intervals between measurements are necessary for accurate integration.
4. **Kinematic Data**: These values are often collected from video recordings, simulation models, or instrumented headforms, such as those used in crash tests and sports injury studies.

---

### **Interpretation and Usage**

- **Maximum Head Impact Power (HIP)**: The HIP value represents the highest rate of change in the kinetic energy of the head during an impact. A higher HIP indicates a more severe impact, which increases the likelihood of injury.
- **Risk Assessment**: The relationship between HIP and the likelihood of **mild traumatic brain injury (MTBI)** is derived from experimental data. Statistical models and logistic regression are often used to create probability curves that predict injury severity based on HIP values.
- **Usage in Sports**: HIP can be used to evaluate the safety of equipment (e.g., football helmets) and assess the risk of concussion or other head injuries in contact sports.
- **Usage in Vehicle Safety**: In automotive crash testing, HIP helps evaluate how well vehicles protect passengers from head injury during a collision.

---

### **Workflow Explanation**

The following steps outline the workflow for calculating the **Head Impact Power (HIP)**.

#### **1. Input Data and Configuration**
The script accepts inputs via command-line arguments, including:
- **Sampling frequency**: The time interval between successive data points.
- **Path to the CSV file**: The file containing raw acceleration data.
- **Column indices**: Identifiers for the columns containing X, Y, and Z acceleration data.

Example:
```bash
python HIP_Calculator.py --frequency 0.001 --file_path "data.csv" --x_location 2 --y_location 3 --z_location 4
```

#### **2. Data Preprocessing**
The script reads the input CSV file and extracts acceleration data. It calculates the time at each data point using the provided sampling frequency and computes the magnitude of acceleration as:

$$
	ext{magnitude} = rac{\sqrt{x^2 + y^2 + z^2}}{9810}
$$

This formula converts acceleration to G-forces, dividing by 9810 (gravity constant in mm/s²).

#### **3. Butterworth Low-Pass Filtering**
To reduce noise and high-frequency components, the script applies a **Butterworth low-pass filter**:
- **Cutoff Frequency**: 1650 Hz (default).
- **Order**: 2 (default).

#### **4. Head Impact Power Calculation**
The script calculates HIP using angular acceleration and velocity data along three axes. It integrates the contributions from each axis to compute the total power.

#### **5. Output Results**
The script prints the calculated HIP value to the terminal:

**Example Output**:
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

**Steps**:
1. User specifies the file path and column indices for X, Y, Z.  
2. The script computes time and acceleration magnitude for each row.
3. Magnitudes are filtered using a low-pass filter.
4. HIP is calculated for multiple overlapping time windows.
5. The script outputs the maximum HIP value and the time window.

**Output Example**:
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
  | Initialize HICCalculator            |
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
  | Initialize HIC calculation loop     |
  +-------------------------------------+
               |
               v
  +-------------------------------------+
  | For each time window (0 - 15ms):    |
  | - Calculate HIC                     |
  | - Store HIC value and time window   |
  +-------------------------------------+
               |
               v
  +-------------------------------------+
  | Find max HIC and corresponding      |
  | time window                         |
  +-------------------------------------+
               |
               v
  +-------------------------------------+
  | Output max HIC and time window      |
  +-------------------------------------+
               |
               v
  +-------------------------------------+
  | End                                 |
  +-------------------------------------+
```
---

### Reference
1. Kleinberger, M., Sun, E., Eppinger, R., Kuppa, S., & Saul, R. (1998). Development of improved injury criteria for the assessment of advanced automotive restraint systems. NHTSA Docket 4405.9, 12–17. https://www.nhtsa.gov/sites/nhtsa.gov/files/criteria_0.pdf
2. https://help.oasys-software.com/articles/#!this-20-0/standard-sae-filter-options
3. Gurdjian, E. S., Hodgson, V. R., Hardy, W. G., Patrick, L. M., & Lissner, H. R. (1964). Evaluation of the protective characteristics of helmets in sports. Journal of Trauma - Injury, Infection and Critical Care, 4 (3), 309–324. https://doi.org/10.1097/00005373-196405000-00005
4. Gurdjian, E. S., Lissner, H. R., Latimer, F. R., Haddad, B. F., & Webster, J. E. (1953). Quantitative determination of acceleration and intracranial pressure in experimental head injury: Preliminary report. Neurology, 3 (6), 417–423. https://doi.org/10.1212/wnl.3.6.417
5. Gurdjian, E. S., Roberts, V. L., & Thomas, L. M. (1966). Tolerance curves of acceleration and intracranial pressure and protective index in experimental head injury. Journal of Trauma - Injury, Infection and Critical Care, 6 (5), 600–604. https://doi.org/10.1097/00005373-196609000-00005
6. Versace, J. (1971). A Review of the Severity Index. SAE Technical Paper 710881. https://doi.org/10.4271/710881
