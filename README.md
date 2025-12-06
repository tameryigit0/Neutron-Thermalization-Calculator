# Neutron-Thermalization-Calculator
"A Python CLI tool to calculate neutron thermalization collisions and lethargy with stochastic error analysis. Supports Light Water, Heavy Water, and Graphite."
# Neutron Thermalization Calculator ⚛️

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Topic](https://img.shields.io/badge/Physics-Nuclear%20Engineering-orange)

A Python-based command-line tool designed to simulate and calculate the moderation (slowing down) process of fast neutrons in a nuclear reactor environment. It utilizes **Fermi Age Theory** approximations to estimate the number of collisions required to reach thermal energy levels.

## 🚀 Features

* **Multi-Moderator Support:** Built-in data for Light Water ($H_2O$), Heavy Water ($D_2O$), and Graphite ($C$).
* **Stochastic Error Calculation:** Provides a **Standard Deviation ($\sigma$)** to account for the random nature of neutron scattering.
* **Lethargy Analysis:** Computes the total logarithmic energy decrement.
* **Physics-Aware Inputs:** Validates energy levels (MeV to eV conversion) and targets.

## 📊 Error Analysis & Model Limitations (Crucial)

This tool separates the "error" into two distinct categories as discussed in reactor physics:

### 1. Statistical Deviation (The "Dice Roll" Effect)
Since neutron scattering is probabilistic, the calculated number of collisions is an **average**. The actual number for any single neutron varies.
* **Formula:** $\sigma \approx \sqrt{\frac{2}{3A} \cdot n}$
* **Impact:** High variance in light nuclei (H2O), low variance in heavy nuclei (Graphite).

### 2. Physical Model Limitations
The code assumes an ideal "Elastic Scattering" model. In a real reactor, the following factors introduce deviations:

| Error Source | Description & Effect |
| :--- | :--- |
| **Chemical Binding** | At low energies (<1 eV), atoms in molecules (like H in H₂O) are not free. They are bound by chemical bonds. **Result:** Neutrons struggle to lose energy in the final thermalization stage, requiring *more* collisions than calculated. |
| **Absorption (Capture)** | The model assumes 100% scattering. In reality, moderators (especially Light Water) absorb some neutrons. **Result:** Not all neutrons successfully reach thermal energy; some are lost to capture. |
| **Resonance Regions** | The code uses a constant $\xi$ (average energy loss). In reality, cross-sections fluctuate at specific resonance energies. **Result:** Minor deviations in specific energy bands. |

## 🛠️ Installation & Usage

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/Neutron-Thermalization-Calculator.git](https://github.com/YOUR_USERNAME/Neutron-Thermalization-Calculator.git)
    ```

2.  **Run the script:**
    ```bash
    python main.py
    ```

## 💻 Example Output

```text
Please select a moderator:
1. Light Water (H2O) [High scattering, high uncertainty]
...
AVG. NUMBER OF COLLISIONS : 19.8
STANDARD DEVIATION (Error): +/- 3.63 collisions
ANALYSIS: Most neutrons will reach thermal energy levels between 16 and 24 collisions.
