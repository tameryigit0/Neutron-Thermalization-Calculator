# Neutron-Thermalization-Calculator
"A Python CLI tool to calculate neutron thermalization collisions and lethargy with stochastic error analysis. Supports Light Water, Heavy Water, and Graphite."
# Neutron Thermalization Calculator ⚛️

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Topic](https://img.shields.io/badge/Physics-Nuclear%20Engineering-orange)

A Python-based command-line tool designed to simulate the **neutron moderation (slowing down)** process. It calculates the number of collisions required to bring a fast neutron (MeV range) down to thermal energy levels (eV range) using **Fermi Age Theory** approximations.

Unique to this tool is the inclusion of **Stochastic Error Analysis**, which estimates the statistical variance inherent in neutron scattering.

## 🧮 Mathematical Framework

The code implements the following core nuclear physics formulas to derive its results:

### 1. Energy Conversion
First, the input energy is converted from Mega-electron Volts (MeV) to electron Volts (eV) to match thermal scales.
$$E_{eV} = E_{MeV} \cdot 10^6$$

### 2. Lethargy ($u$)
Neutrons lose energy logarithmically. "Lethargy" is the dimensionless measure of this energy loss from the initial high-energy state ($E_0$) to the final thermal state ($E_{th}$).
$$u = \ln \left( \frac{E_0}{E_{th}} \right)$$

### 3. Average Number of Collisions ($\bar{n}$)
The expected number of collisions depends on the total Lethargy ($u$) and the moderator's efficiency ($\xi$).
$$\bar{n} = \frac{u}{\xi}$$
*Where $\xi$ (Average Logarithmic Energy Decrement) is a material constant:*
* *H₂O $\approx$ 0.920*
* *D₂O $\approx$ 0.509*
* *Graphite $\approx$ 0.158*

### 4. Standard Deviation ($\sigma$)
Since scattering is probabilistic, the actual number of collisions for any single neutron follows a statistical distribution. The tool calculates the standard deviation based on the Atomic Mass Number ($A$):
$$\sigma \approx \sqrt{\frac{2}{3A} \cdot \bar{n}}$$

---

## 📊 Error Analysis & Model Limitations

This tool distinguishes between **Statistical Uncertainty** (calculated by the code) and **Physical Model Limitations** (theoretical assumptions).

### 1. Statistical Uncertainty (The "Dice Roll")
The output `STANDARD DEVIATION (+/-)` represents the natural spread of data.
* **Light Nuclei (e.g., Hydrogen, A=1):** High variance. A neutron might stop in 1 collision or 30.
* **Heavy Nuclei (e.g., Carbon, A=12):** Low variance. The slowing-down process is more deterministic and stable.

### 2. Physical Model Limitations (Real-World Factors)
The code assumes ideal elastic scattering. In a real reactor core, the following factors introduce deviations:

| Error Source | Description & Effect |
| :--- | :--- |
| **Chemical Binding** | At low energies (<1 eV), atoms in molecules (like H in H₂O) are not free; they are bound by chemical forces. **Effect:** Neutrons struggle to lose energy in the final stage, requiring *more* collisions than calculated. |
| **Absorption (Capture)** | The model assumes 100% scattering. In reality, moderators (especially Light Water) absorb some neutrons. **Effect:** Not all neutrons successfully reach thermal energy; some are lost to capture. |
| **Resonance Regions** | The code uses a constant $\xi$. In reality, cross-sections fluctuate at specific resonance energies. **Effect:** Minor deviations in specific energy bands. |

---

## 🚀 Features & Usage

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/Neutron-Thermalization-Calculator.git](https://github.com/YOUR_USERNAME/Neutron-Thermalization-Calculator.git)
    ```
2.  **Run the script:**
    ```bash
    python main.py
    ```

### Example Output
```text
MODERATOR: Light Water (H2O)
Energy Change: 2.0 MeV -> 0.025 eV
----------------------------------------
AVG. NUMBER OF COLLISIONS : 19.8
STANDARD DEVIATION (Error): +/- 3.63 collisions
----------------------------------------
ANALYSIS: Most neutrons will reach thermal energy levels between 16 and 24 collisions.
