
## Head Impact Power (HIP) Calculation

The **Head Impact Power (HIP)** is a biomechanical metric that quantifies the rate of change in kinetic energy of the head during an impact event. The calculation of HIP is based on both **linear** and **rotational** motion, considering the accelerations and velocities along three axes (X, Y, Z). The highest value of HIP during the event is used to assess the likelihood of head injury.

---

### **Formula for HIP Calculation**

The **HIP** is calculated using the following formula:

$$HIP = 4.50 \left( \int a_x \cdot dt \right) + 4.50 \left( \int a_y \cdot dt \right) + 4.50 \left( \int a_z \cdot dt \right) + 0.016 \left( \int \alpha_x \cdot dt \right) + 0.024 \left( \int \alpha_y \cdot dt \right) + 0.022 \left( \int \alpha_z \cdot dt \right)$$

Where:
- $$a_x, a_y, a_z$$ are the **linear accelerations** along the three axes (X, Y, Z),
- $$\alpha_x, \alpha_y, \alpha_z$$ are the **angular accelerations** along the three axes (X, Y, Z),
- $$t$$ represents **time**.

This equation integrates the contributions from both **linear** and **rotational motion** to determine the **rate of change** in kinetic energy during the impact event. The **maximum** value of this power is used to define the **maximum Head Impact Power (HIP)**.

---

### **Background**

The concept of Head Impact Power (HIP) is grounded in the idea that the probability of head injury is closely related to the **rate of change in kinetic energy** during an impact. This hypothesis was proposed by Newman and Shewchenko in 2000, and it is based on data from instrumented Hybrid III anthropomorphic test dummies, which simulate head impacts in various contexts (e.g., football players in head-to-head collisions). The **maximum** value of HIP during an impact event is used to assess the risk of head injury.

The core idea is that head injury severity correlates with the maximum rate at which kinetic energy is transferred to the head during an impact.

---

## Data Requirements for HIP Calculation

According to the formula for calculating HIP, the following data is required:

1. **Linear accelerations** $$(a_x, a_y, a_z)$$: These represent the accelerations of the head along the three axes (X, Y, Z). They are typically measured using accelerometers or motion capture systems.

2. **Angular accelerations** $$(\alpha_x, \alpha_y, \alpha_z)$$: These describe the rotational accelerations of the head along the three axes (X, Y, Z). These are also measured using accelerometers or motion capture systems.

3. **Time intervals**: The time between data points is necessary for accurate integration of the accelerations to calculate the rate of change in kinetic energy.

4. **Kinematic Data**: These values include both linear and angular velocities and are often collected from video recordings, simulation models, or instrumented headforms used in crash tests and sports injury studies. These velocities are calculated by integrating the corresponding accelerations over time.
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

$$ {magnitude} = \frac{\sqrt{x^2 + y^2 + z^2}}{9810}$$

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
1. Newman, J.A. and Shewchenko, N., 2000. A proposed new biomechanical head injury assessment function-the maximum power index (No. 2000-01-SC16). SAE Technical Paper.
