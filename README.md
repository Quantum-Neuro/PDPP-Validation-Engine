[English](README.md) | [简体中文](README_zh-CN.md)

# PDPP Validation Engine: Macroscopic Topological Phase Transition & Causal Inference Pipeline

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![ArXiv](https://img.shields.io/badge/arXiv-Pending-red.svg)](https://arxiv.org)

The **Pan-Dimensional Phase Projection (PDPP) Validation Engine** is a highly robust computational pipeline for a phenomenological model. The pipeline is designed to detect macroscopic topological bifurcations in complex biological neural systems (EEG/MEG) and quantify their non-classical causal shielding effects on simulated open quantum systems using Bayesian counterfactual inference.

## 🚀 Core Algorithmic Engineering

Unlike traditional statistical analysis pipelines, this engine discards all hardcoded parameters that could lead to overfitting or forward data leakage. It implements strictly constrained methodological interlocks at the foundational level:

1. **Full Tensor Vectorized Extraction (`scipy.signal`)**: Thoroughly strips away the inefficient loops of the MNE framework. The calculations for the baseline Gamma (30-70Hz) methodological control group and the High-Gamma/Ripple band (80-200Hz) Cross-Frequency Coupling (CFC) are delegated to C/Fortran-level full tensor operations. It incorporates Picard-based Independent Component Analysis (ICA) to rigorously scrub high-frequency spatial artifacts.
2. **Retrospective Blind Sweep & EVT Radar**: Rejects the "Texas Sharpshooter Fallacy" (hardcoding intervention points). The engine enforces a rigorous $2\sigma$ retrospective blind sweep combined with Generalized Extreme Value (GEV) distributions to dynamically lock onto absolute physical topological peaks, establishing this as the sole intervention point while strictly isolating forward data leakage.
3. **Global Constant Auto-Calibration (`auto_calibrate`)**: When simulating quantum dynamic evolution, the optimizer (`minimize_scalar`) is strictly constrained to output a global constant multiplier. This mechanism uniformly stretches the entire thermodynamic timeline, mathematically eliminating any illusion of "Data Leakage" caused by dynamic time-step modifications.
4. **Structural Causal Inference Backend**:
   - Introduces Turing Award laureate Judea Pearl's **Structural Causal Model (SCM)**, discarding traditional Granger tests that can only prove predictive correlation.
   - Employs **Bayesian Structural Time Series (BSTS)** to generate parallel history counterfactual baselines without intervention, strictly elevating correlation to Average Causal Effect.

## 📊 Empirical Verification Results

When applied to high-precision EEG datasets of advanced mental trainees, the engine first utilized the 30-70Hz broadband Gamma as a methodological benchmark to intercept statistical illusions caused by filter boundary variance collapse. Subsequently, within the ICA-scrubbed 80-200Hz High-Gamma/Ripple band, it achieved highly robust statistical causal inference:
- **Topological Bifurcation (EVT FDR-Adjusted)**: q < 0.05 (47.56x probability enhancement)
- **Counterfactual Shielding (KPSS-Stationary BSTS)**: p = 2.11 &times; 10<sup>-34</sup>

*(For the mathematical boundaries, proofs of logical interlocks, and empirical inferences of the algorithm, please refer to the primary research manuscript in the `docs` folder).*

## 📖 Phenomenological Theory & Documentation

This engine is the computational foundation of the **Pan-Dimensional Phase Projection (PDPP)** phenomenological theory. The PDPP model employs the Wigner pseudo-probability function as a cross-scale bridge, mapping Bayesian prediction errors (Friston Free Energy) to environmental dissipation constrained by Landauer's Principle. The model posits that long-range Gamma cross-frequency coupling induces a Decoherence-Free Subspace (DFS) analogous to Fröhlich Condensation, constructing macroscopic topological manifolds via Pitchfork Bifurcation to surpass the $10^{-13}$ second decoherence limit.

Inside the `docs/` folder, you will find the core academic literature detailing the boundaries of this model:

- 📄 **[PDPP_Topological_Shielding_Validation.pdf](https://cdn.jsdelivr.net/gh/Quantum-Neuro/PDPP-Validation-Engine@main/docs/PDPP_Topological_Shielding_Validation.pdf)**
  *The primary research manuscript. It contains the full mathematical derivations of the Bidirectional EVT Radar, the topological mapping equations between classical EEG features and quantum dissipative parameters (&gamma;, &epsilon;), and the rigorous fail-safe counterfactual causal inference results.*

To explicitly detail the Wigner evolution manifold, the Fluctuation-Dissipation Theorem, and the boundary conditions of this phenomenological model, we have prepared comprehensive whitepapers:
- 👉 **[Read PDPP Theoretical Framework Whitepaper (English)](./docs/PDPP_Theoretical_Framework_Whitepaper_EN.md)**
- 👉 **[阅读 PDPP 理论框架白皮书 (简体中文)](./docs/PDPP_Theoretical_Framework_Whitepaper_ZH.md)**

## ⚙️ Quick Start (One-Click Testing)

This project provides dedicated environment-wrapped entry scripts for different operating systems, eliminating the need to configure complex Python environments. After installing Python 3.9+, you can directly double-click the following files to launch the engine testing process:

- **🍎 macOS Users**: Double-click `start.command`
- **🪟 Windows Users**: Double-click `start.bat`
- **🐧 Linux Users**: Execute `./start.sh` in the terminal.

> **✨ Automated Sandbox Environment**: On the first run, the script will automatically create an isolated virtual environment (`.venv`) and strictly align all library dependencies. Please be patient during the initialization configuration!

---

## 💾 Data Provisioning & Connectivity Testing

To comply with data provenance and privacy regulations, **no large raw EEG files are stored in this repository**. The pipeline utilizes a dual-layer data provisioning strategy:

1. **Auto-Download (Primary):** On the first run, if `./data` is empty, the engine will automatically connect to the OpenNeuro AWS S3 server and fetch representative BIDS-compliant samples from dataset `ds003816` *(We gratefully acknowledge the original authors of ds003816 for releasing this dataset into the public domain)*.
2. **Offline Micro-Sample (Fallback):** If offline or restricted, the engine will gracefully downgrade to use the ultra-small downsampled cuts in the built-in `./data_sample` folder. This sample is strictly for **code pipeline connectivity testing (verifying compilation, routing, and crash-free execution)**.

> [!WARNING]
> The sample micro-dataset cannot provide stationary time series satisfying the required degrees of freedom, which will cause the engine to trigger underlying fail-safe mechanisms and abort Bayesian causal calculations. To verify full counterfactual inference, the complete high-precision dataset must be downloaded using the primary method.

---

## 🔬 Custom Data Reproduction Guide

The PDPP Validation Engine supports the import of your own high-precision EEG data for phase transition scanning and causal inference.

**Data Requirements**:
- Supported Formats: `.edf`, `.vhdr` (BrainVision), `.bdf`
- Channel Requirements: Must contain at least frontal (e.g., `Fz`, `F3`) and occipital (e.g., `Oz`, `O1`, `O2`) or parietal (e.g., `Pz`) leads to allow the engine to extract long-range CFC and DMN decoupling topological features.

**Execution Steps**:
1. Place your EEG files into the root `data/` folder (multi-level subdirectory nesting is supported).
2. (Optional) To assist the EVT Radar's judgment, if the data belongs to a "long-term meditator/high-order intervention state," please include `lt` in the filename (e.g., `sub-01_task-meditation_lt.vhdr`); baseline control groups do not require a suffix or can use other suffixes.
3. Open a terminal and execute the main engine entry:
   ```bash
   python main.py
   ```
4. The engine will automatically take over stationarity testing, dynamic peak detection, and BSTS modeling. All analysis results and research reports in Word/PDF formats will be automatically output to the `Report/` folder.

---

🧠 **Citation**

If you utilize the algorithms of this open-source engine (such as the EVT Extreme Value Radar, BSTS Quantum Baseline Calibrator, etc.) in your academic research, please cite our underlying methodological manuscript:
```text
Jia, W., et al. "Macroscopic Topological Phase Transitions of the Neural Network Induce Non-Classical Causal Shielding on Quantum Decoherence: An Empirical Validation." arXiv (2026).
```
