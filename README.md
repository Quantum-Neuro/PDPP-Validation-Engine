[English](README.md) | [简体中文](README_zh-CN.md)

# PDPP Validation Engine: Macroscopic Topological Phase Transition & Causal Inference Pipeline

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![ArXiv](https://img.shields.io/badge/arXiv-Pending-red.svg)]()

The **Pan-Dimensional Phase Projection (PDPP) Validation Engine** is an industrial-grade, fail-safe algorithmic pipeline designed to detect macroscopic topological phase transitions in complex neural systems (EEG/MEG) and quantify their non-classical causal shielding effects on simulated open quantum systems.

## 🚀 Key Features

Unlike traditional statistical pipelines, this engine is built with strict industrial-grade fail-safe interlocks to prevent false positives (P-hacking) and ensure robust causal inference:

1. **Bidirectional EVT Radar**: Utilizes Generalized Extreme Value (GEV) distributions to identify both *Generative Phase Transitions* (high-energy cross-frequency bursts) and *Deconstructive Phase Transitions* (ultra-low entropy zero-point states/Nirodha).
2. **Logical Interlock (Fail-Safe Mechanism)**: Automatically aborts downstream quantum causal calculations if the input data falls within classical thermal noise boundaries, strictly utilizing negative controls to prevent overfitting.
3. **Smart Length-Finding Algorithm**: Automatically parses large EEG matrices to extract the most contiguous, noise-free time series to satisfy the degrees of freedom required by Bayesian inference.
4. **Dual Causal Inference Backends**: 
   - **VAR Granger Causality** for predictive driving in generative states.
   - **Bayesian Structural Time Series (BSTS)** for counterfactual inference in deconstructive shielding states.

## 📊 Empirical Breakthroughs

When applied to high-precision EEG datasets of advanced mental trainees, this engine successfully intercepted all classical noise samples (Inverse Negative Controls) and achieved unprecedented statistical significance in positive samples:
- **Generative Drive**: p = 7.43 &times; 10<sup>-14</sup>
- **Counterfactual Shielding (Absolute Silence)**: p = 3.76 &times; 10<sup>-27</sup>

*(For full mathematical derivation and empirical results, please refer to our [Research Manuscript](https://cdn.jsdelivr.net/gh/Quantum-Neuro/PDPP-Validation-Engine@main/docs/PDPP_Topological_Shielding_Validation.pdf) in the `/docs` folder).*

## 📖 Theoretical Framework & Documentation

This engine serves as the computational backbone for the **Pan-Dimensional Phase Projection (PDPP)** theoretical framework. The PDPP theory bridges macroscopic neurodynamics with open quantum systems, proposing that biological neural networks can undergo topological phase transitions capable of actively shielding quantum decoherence.

Inside the `docs/` folder, you will find the core academic literature detailing this framework:

- 📄 **[PDPP_Topological_Shielding_Validation.pdf](https://cdn.jsdelivr.net/gh/Quantum-Neuro/PDPP-Validation-Engine@main/docs/PDPP_Topological_Shielding_Validation.pdf)**
  *The primary research manuscript. It contains the full mathematical derivations of the Bidirectional EVT Radar, the topological mapping equations between classical EEG features (DMN Decoupling, Theta-Gamma PAC) and quantum parameters (&gamma;, &epsilon;), and the rigorous causal inference results.*

We highly encourage researchers in quantum biology, cognitive neuroscience, and complex systems to review this document to understand the profound physical implications behind the algorithmic processes executed by this engine.

For general researchers looking to quickly understand how the PDPP framework bridges different disciplines, we have prepared an **Interdisciplinary Rosetta Stone Matrix**:
- 👉 **[Read PDPP Theoretical Framework Whitepaper (English)](./docs/PDPP_Theoretical_Framework_Whitepaper_EN.md)**
- 👉 **[Read PDPP Theoretical Framework Whitepaper (Simplified Chinese)](./docs/PDPP_Theoretical_Framework_Whitepaper_ZH.md)**

## ⚙️ Quick Start (One-Click Execution)

This project provides dedicated "double-click" entry scripts for different operating systems, eliminating the need to configure complex terminal environments. After installing Python 3.9+, you can directly **double-click** the corresponding file below to launch the engine:

- **🍎 macOS Users**: Double-click `start.command`
- **🪟 Windows Users**: Double-click `start.bat`
- **🐧 Linux Users**: Execute `./start.sh` in the terminal, or double-click `start.sh` in a GUI environment.

> **✨ Automated Sandbox Environment**: On the first run, the script will automatically create an isolated virtual environment (`.venv`) and use `pip` to perfectly align all dependencies. Once complete, the engine will start seamlessly. Please be patient during the first initialization!

---

## 💾 Data Provisioning (Auto-Download & Sample Dataset)

To keep this repository extremely lightweight and comply with data provenance regulations, **no real EEG data files are stored in this repository**. Instead, the pipeline features a dual-layer automated data provisioning system:

1. **Auto-Download (Primary Method):** When you run the engine for the first time, if your `./data` folder is empty, the engine will automatically connect to the OpenNeuro official AWS S3 server and fetch 24 representative BIDS-compliant sample files from dataset `ds003816`.
2. **Offline Sample Dataset (Fallback):** If your network connection is unstable, blocked, or completely offline, the auto-download will gracefully fail and the engine will automatically fall back to the `./data_sample` folder. This folder contains a tiny micro-sample (< 5MB, 10-second downsampled cuts) strictly for **code pipeline connectivity testing**. 

> [!WARNING]
> The Sample Dataset is composed of extremely brief micro-samples intended *only* to prove that the code architecture compiles, routes, and runs without crashing. **Do not expect complete or statistically significant validation results when using the Sample Dataset.** Genuine replication of the extreme value phase transitions requires the full high-precision dataset to be downloaded via the primary method.

---

### 💻 Developer CLI (Terminal/CMD)

```bash
# Clone the repository
git clone https://github.com/Quantum-Neuro/PDPP-Validation-Engine.git
cd PDPP-Validation-Engine

# Run the automated validation pipeline (dependencies will auto-install if missing)
python main.py
```

🧠 Citation
If you use this validation engine or the PDPP theoretical framework in your research, please cite our paper:
Jia, W., et al. "Macroscopic Topological Phase Transitions of the Neural Network Induce Non-Classical Causal Shielding on Quantum Decoherence: An Empirical Validation." arXiv (2026).
