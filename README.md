# Neutron-Thermalization-Calculator
"A Python CLI tool to calculate neutron thermalization collisions and lethargy with stochastic error analysis. Supports Light Water, Heavy Water, and Graphite."
# Neutron Thermalization Calculator ⚛️

A Python-based CLI tool to calculate the number of collisions required to slow down (moderate) fast neutrons to thermal energy levels using Fermi Age Theory approximations.

## 🚀 Features

* **Multi-Moderator Support:** Calculate for Light Water ($H_2O$), Heavy Water ($D_2O$), and Graphite ($C$).
* **Stochastic Analysis:** Unlike simple calculators, this tool provides a **Standard Deviation** ($\sigma$) to account for the probabilistic nature of neutron scattering.
* **Lethargy Calculation:** Computes the logarithmic energy decrement based on input MeV.
* **Safety Checks:** Includes input validation and boundary checks for energy levels.

## 📋 Prerequisites

* Python 3.x

## 🔧 Installation & Usage

1.  Clone the repository:
    ```bash
    git clone [https://github.com/KULLANICI_ADIN/Neutron-Thermalization-Calculator.git](https://github.com/KULLANICI_ADIN/Neutron-Thermalization-Calculator.git)
    ```
2.  Navigate to the directory:
    ```bash
    cd Neutron-Thermalization-Calculator
    ```
3.  Run the script:
    ```bash
    python main.py
    ```

## 🧠 Physics Background & Error Analysis

### Why is there an "Error Margin" (Standard Deviation)?

Neutron moderation is a **stochastic (probabilistic)** process, not a deterministic one. 

1.  **Random Nature of Scattering:** When a neutron hits a nucleus, the energy loss depends on the scattering angle. A neutron might lose a lot of energy in a "head-on" collision or very little in a "glancing" blow.
2.  **The Statistical Spread:** The calculated number of collisions ($n$) is merely an **average**. 
    * For light nuclei (like Hydrogen in $H_2O$), the variance is high because a single collision can dramatically change the neutron's energy.
    * For heavy nuclei (like Carbon in Graphite), the process is more gradual and "stable," resulting in a lower standard deviation.

This tool calculates the **Standard Deviation ($\sigma$)** using the approximation:

$$ \sigma \approx \sqrt{\frac{2}{3A} \cdot n} $$

Where $A$ is the atomic mass number and $n$ is the average number of collisions. The tool gives you a confidence interval where ~68% of neutrons will fall.

### Key Formulas Used

* **Lethargy ($u$):**
    $$ u = \ln \left( \frac{E_0}{E_{thermal}} \right) $$
    
* **Average Number of Collisions ($n$):**
    $$ n = \frac{u}{\xi} $$
    *(Where $\xi$ is the average logarithmic energy decrement per collision)*

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
*Developed for educational purposes in Nuclear Engineering.*
