[English](README.md) | [简体中文](README_zh-CN.md)

# PDPP 验证引擎：宏观拓扑相变与因果推断管线

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![ArXiv](https://img.shields.io/badge/arXiv-Pending-red.svg)]()

**泛维度相位投影（PDPP）验证引擎**是一个工业级的、具备故障安全（fail-safe）机制的算法管线。该管线旨在检测复杂神经系统（EEG/MEG）中的宏观拓扑相变，并量化其对模拟的开放量子系统产生的非经典因果屏蔽效应。

## 🚀 核心特性

与传统的统计学管线不同，本引擎内置了严格的工业级逻辑互锁（防错）机制，以杜绝假阳性（P-hacking）并确保因果推断的极度鲁棒性：

1. **双向极值理论（EVT）雷达**：利用广义极值（GEV）分布来识别*生成性相变*（高能跨频爆发）与*解构性相变*（超低熵零点状态/灭尽定）。
2. **逻辑互锁（防错机制）**：如果输入数据落入经典热噪声边界内，引擎将自动中止下游的量子因果计算，严格使用负对照来防止模型过拟合。
3. **智能寻长算法**：自动解析庞大的脑电矩阵，提取最连续、无噪声的时间序列，以满足贝叶斯推断所需的自由度要求。
4. **双因果推断后端**：
   - **VAR 格兰杰因果（Granger Causality）**：用于生成状态下的预测驱动力分析。
   - **贝叶斯结构时间序列（BSTS）**：用于解构性屏蔽状态下的反事实推断。

## 📊 实证突破

当应用于高阶心智训练者的高精度脑电数据集时，本引擎成功拦截了所有的经典噪声样本（反向负对照），并在阳性样本中取得了史无前例的统计学显著性：
- **生成性驱动力（Generative Drive）**：p = 7.43 &times; 10<sup>-14</sup>
- **反事实屏蔽（绝对寂静状态）**：p = 3.76 &times; 10<sup>-27</sup>

*（有关完整的数学推导与实证结果，请参阅 `docs` 文件夹中的 [研究手稿](docs/PDPP_Topological_Shielding_Validation.pdf)）。*

## 📖 理论框架与文档

本引擎是**泛维度相位投影（PDPP）**理论框架的计算基座。PDPP 理论桥接了宏观神经动力学与开放量子系统，提出生物神经网络能够经历宏观拓扑相变，从而主动屏蔽量子退相干环境。

在 `docs/` 文件夹中，您可以找到详细阐述该框架的核心学术文献：

- 📄 **[`PDPP_Topological_Shielding_Validation.pdf`](docs/PDPP_Topological_Shielding_Validation.pdf)**
  *主要研究手稿。包含了双向 EVT 雷达的完整数学推导、经典脑电特征（DMN 解耦、Theta-Gamma 跨频耦合）与量子参数（&gamma;, &epsilon;）之间的拓扑映射方程，以及极其严谨的因果推断结果。*

我们强烈鼓励量子生物学、认知神经科学以及复杂系统领域的学者阅读此文档，以理解该引擎执行的算法流程背后极其深远的物理学意义。

## ⚙️ 快速启动（一键执行）

本项目为不同操作系统提供了专用的“双击”入口脚本，免去了配置复杂终端环境的烦恼。在安装 Python 3.9+ 之后，您可以直接**双击**下方的对应文件来启动引擎：

- **🍎 macOS 用户**：双击 `start.command`
- **🪟 Windows 用户**：双击 `start.bat`
- **🐧 Linux 用户**：在终端执行 `./start.sh`，或在图形界面中双击 `start.sh`。

> **✨ 自动化沙盒环境**：在首次运行时，脚本将自动创建一个隔离的虚拟环境（`.venv`）并使用 `pip` 完美对齐所有依赖项。配置完成后，引擎将无缝启动。首次初始化时请耐心等待！

---

## 💾 数据获取（自动下载与示例数据集）

为了保持本仓库的极致轻量化并严格遵守数据溯源合规要求，**本仓库内未存储任何真实的脑电原始文件**。取而代之的是，管线内置了双层自动化数据获取系统：

1. **自动拉取（首选方案）：** 当您首次运行引擎且 `./data` 文件夹为空时，引擎将自动连接至 OpenNeuro 官方的 AWS S3 服务器，提取 `ds003816` 数据集中 24 个符合 BIDS 标准的代表性样本。
2. **离线示例数据集（备选方案）：** 如果您的网络连接不稳定、受限或完全离线，自动下载将平滑退出，引擎会自动降级使用 `./data_sample` 文件夹。该文件夹内包含一个极微小的测试样本（< 5MB，10 秒降采样截断），仅严格用于**代码管线连通性测试**。

> [!WARNING]
> 示例数据集（Sample Dataset）由极其短暂的微样本组成，其*唯一目的*是证明代码架构能够成功编译、路由且运行不崩溃。**请不要指望使用示例数据集跑出完整的或具有统计学显著性的验证结果。** 真正复现极值相变的震撼结果，需要通过首选方案下载高精度的全量数据集。

---

### 💻 开发者命令行运行 (Developer CLI)

```bash
# 克隆仓库
git clone https://github.com/Quantum-Neuro/PDPP-Validation-Engine.git
cd PDPP-Validation-Engine

# 运行自动化验证管线（如果缺少依赖，将自动安装）
python main.py
```

🧠 引用 (Citation)
如果您在研究中使用了本验证引擎或 PDPP 理论框架，请引用我们的论文：
Jia, W., et al. "Macroscopic Topological Phase Transitions of the Neural Network Induce Non-Classical Causal Shielding on Quantum Decoherence: An Empirical Validation." arXiv (2026).
