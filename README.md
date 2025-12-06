# Neutron-Thermalization-Calculator
"A Python CLI tool to calculate neutron thermalization collisions and lethargy with stochastic error analysis. Supports Light Water, Heavy Water, and Graphite."
# Neutron Thermalization Calculator ⚛️

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Topic](https://img.shields.io/badge/Physics-Nuclear%20Engineering-orange)

A Python-based command-line tool designed to simulate and calculate the moderation (slowing down) process of fast neutrons in a nuclear reactor environment. It utilizes **Fermi Age Theory** approximations to estimate the number of collisions required to reach thermal energy levels.

Unlike simple calculators, this tool includes a **stochastic error analysis**, providing a standard deviation to account for the probabilistic nature of neutron scattering.

## 🚀 Features

* **Multi-Moderator Support:** Built-in data for:
    * Light Water ($H_2O$)
    * Heavy Water ($D_2O$)
    * Graphite ($C$)
* **Lethargy Calculation:** Computes the total logarithmic energy decrement required.
* **Statistical Error Analysis:** Calculates the Standard Deviation ($\sigma$) and confidence intervals for the collision count.
* **Input Validation:** Ensures physical constraints (e.g., Target Energy < Initial Energy) are met.

## 🛠️ Installation & Usage

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/Neutron-Thermalization-Calculator.git](https://github.com/YOUR_USERNAME/Neutron-Thermalization-Calculator.git)
    ```

2.  **Navigate to the directory:**
    ```bash
    cd Neutron-Thermalization-Calculator
    ```

3.  **Run the script:**
    ```bash
    python main.py
    ```

## 💻 Example Output

```text
Please select a moderator:
1. Light Water (H2O) [High scattering, high uncertainty]
2. Heavy Water (D2O) [Low absorption, medium uncertainty]
3. Graphite (C)      [Stable slowing down, low uncertainty]

Your Selection (1/2/3): 1

Enter initial neutron energy (MeV) [e.g., 2]: 2

========================================
MODERATOR: Light Water (H2O)
Energy Change: 2.0 MeV -> 0.025 eV
----------------------------------------
AVG. NUMBER OF COLLISIONS : 19.8
STANDARD DEVIATION (Error): +/- 3.63 collisions
----------------------------------------
ANALYSIS:
Most neutrons will reach thermal energy levels
between 16 and 24 collisions.
========================================
