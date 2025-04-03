
### **GAMBIT Injury Criteria Calculation Workflow**

The **GAMBIT (Generalized Acceleration Model for Brain Injury Threshold)** is a model used to evaluate the likelihood of brain injury based on both translational and rotational accelerations. The model considers the combined effects of these two types of motion during an impact event, such as in vehicle collisions. GAMBIT integrates both translational (linear) and rotational (angular) accelerations to assess the severity of a potential brain injury.

---

### **Workflow Explanation**

#### **1. Introduction to GAMBIT**

The GAMBIT model computes the injury risk by using a formula that integrates the effects of both translational and rotational accelerations:

\(
G(t) = \left( rac{a(t)}{a_c} ight)^n + \left( rac{a_r(t)}{a_r^c} ight)^m
\)

Where:
- \( a(t) \) is the translational acceleration,
- \( a_r(t) \) is the rotational acceleration,
- \( a_c \) and \( a_r^c \) are the critical translational and rotational accelerations, respectively, beyond which brain injury is likely,
- \( n \) and \( m \) are empirical constants that adjust the influence of each type of acceleration.

The value of \( G(t) \) can be used to evaluate the likelihood of injury. If \( G(t) > 1 \), the injury threshold has been exceeded, and brain injury is more likely. If \( G(t) < 1 \), the injury threshold has not been exceeded, and the risk of injury is lower.

---

#### **2. Data Preprocessing**

To compute the GAMBIT value, the first step is to gather and preprocess the acceleration data. The input data typically comes from experiments or simulations that measure both **translational** and **rotational** accelerations.

**Key steps:**
1. **Sampling Frequency**: The frequency at which the data is collected. It is important to maintain consistent sampling to ensure data accuracy.
2. **Acceleration Data**: The raw acceleration values (both translational and rotational) need to be extracted from the dataset. These values are often measured using accelerometers or sensors placed on a rigid body (e.g., headform in crash tests).
3. **Magnitude Calculation**: Using the formula:

\(
	ext{magnitude} = rac{\sqrt{x^2 + y^2 + z^2}}{9810}
\)

This formula converts the measured acceleration values into G-forces, dividing by 9810 (gravity constant in mm/s²). This step ensures that the data is in an appropriate scale for further analysis.

---

#### **3. Data Filtering**

The raw data collected during impact events often contains high-frequency noise due to vibrations and other sources. To eliminate these noise components, a **Butterworth low-pass filter** is applied. The filtering process helps focus on the accelerations that contribute to brain injury.

**Key Parameters**:
- **Cutoff Frequency**: 1650 Hz (default). This is the frequency at which the filter will begin to attenuate higher-frequency components.
- **Order**: 2 (default). This parameter determines the sharpness of the filter.

Filtering helps in isolating the primary inertial components of the acceleration signal.

---

#### **4. GAMBIT Calculation**

Once the data is preprocessed and filtered, the GAMBIT injury criterion is calculated using the formula:

\(
G(t) = \left( rac{a(t)}{a_c} ight)^n + \left( rac{a_r(t)}{a_r^c} ight)^m
\)

Where:
- \( G(t) \) is the GAMBIT value, representing the likelihood of brain injury.
- \( a(t) \) is the translational acceleration.
- \( a_r(t) \) is the rotational acceleration.

If the value of \( G(t) \) exceeds 1, this suggests that the injury threshold has been crossed, indicating a higher likelihood of brain injury. Conversely, if \( G(t) \) is less than 1, the risk is considered lower.

This calculation is based on both the instantaneous translational and rotational accelerations measured during the impact event. The empirical constants \( n \) and \( m \) are adjusted based on available experimental data and the specific context of the crash or impact.

---

#### **5. Output Results**

The final output of the calculation is the GAMBIT value, which is printed to the terminal or saved for further analysis:

**Example Output**:

```
The GAMBIT Injury Criterion (G) value is: 1.20
```

This result provides a quantifiable measure of brain injury risk, which can be used to evaluate the safety of the impact event.

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

This example demonstrates how the script processes the input CSV, applies filtering, and calculates the GAMBIT injury criterion.

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
