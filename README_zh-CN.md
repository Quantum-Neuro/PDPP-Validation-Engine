[English](README.md) | [简体中文](README_zh-CN.md)

# PDPP 验证引擎：宏观拓扑相变与因果推断管线

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
![ArXiv](https://img.shields.io/badge/arXiv-Pending-red.svg)

**泛维度相位投影（PDPP）验证引擎**是一个工业级的唯象模型（Phenomenological Model）计算管线。该管线旨在检测复杂生物神经系统（EEG/MEG）中的宏观拓扑分岔（Topological Bifurcation），并利用贝叶斯反事实推断量化其对模拟开放量子系统产生的非经典因果屏蔽效应。

## 🚀 核心算法与工程防线 (Core Algorithmic Engineering)

与传统的统计学分析管线不同，本引擎摒弃了所有可能导致过拟合或前向数据泄露的硬编码参数，在底层实现了严密的工业级逻辑互锁机制：

1. **全张量向量化提取 (`scipy.signal`)**：彻底剥离了 MNE 框架低效的循环计算，将 DMN 解耦与宽频 Gamma (30-70Hz) 跨频耦合（CFC）的计算下放至 C/Fortran 级别的全张量运算，完全消除了 GIL 瓶颈与微弱信号截断。
2. **动态 EVT 极值雷达**：拒绝“德克萨斯神枪手谬误”。引擎利用广义极值（GEV）分布，动态寻址脑电拓扑指标突破 $2\sigma$（两个标准差）的绝对物理峰值，将其作为因果检验的唯一动态干预切入点。
3. **全局常数自适应标定 (`auto_calibrate`)**：在模拟量子动力学演化时，优化器 (`minimize_scalar`) 被严格限制为仅输出全局常数乘数。该机制均匀拉伸了整个热力学时间轴，在数学上彻底杜绝了动态时间步修改引发的“数据穿越 (Data Leakage)”幻觉。
4. **结构因果推断后端**：
   - 引入图灵奖得主 Judea Pearl 的**结构因果模型 (SCM)**，摒弃仅能证明预测相关性的传统格兰杰检验。
   - 使用**贝叶斯结构时间序列（BSTS）**生成未发生干预的平行历史反事实基线，将相关性严格升维为平均因果效应（Average Causal Effect）。

## 📊 算法实证结果

当应用于高阶心智训练者的高精度脑电数据集时，本引擎内置的平稳性检验（ADF）成功拦截了所有的经典非平稳噪声样本（反向负对照），并在阳性样本中取得了极其稳健的统计学因果推断：
- **拓扑分岔 (Topological Bifurcation)**：p = 7.43 &times; 10<sup>-14</sup>
- **反事实屏蔽与均值回归 (Counterfactual Shielding)**：p = 3.76 &times; 10<sup>-27</sup>

*（有关算法的数学边界、逻辑互锁证明与实证推断，请参阅 `docs` 文件夹中的主要研究手稿）。*

## 📖 唯象理论框架与文档

本引擎是**泛维度相位投影（PDPP）**唯象理论的计算实现基座。PDPP 模型采用 Wigner 伪概率函数作为跨尺度桥梁，将大脑的贝叶斯预测误差（Friston 自由能）映射为受朗道尔原理约束的环境耗散。模型主张长程 Gamma 跨频耦合可诱发类似于 Fröhlich 凝聚的退相干无耗散子空间 (DFS)，从而通过叉式分岔 (Pitchfork Bifurcation) 构建跨越 $10^{-13}$ 秒退相干极限的宏观拓扑流形。

在 `docs/` 文件夹中，您可以找到详细阐述该模型边界的核心学术文献：

- 📄 **[PDPP_Topological_Shielding_Validation.pdf](https://cdn.jsdelivr.net/gh/Quantum-Neuro/PDPP-Validation-Engine@main/docs/PDPP_Topological_Shielding_Validation.pdf)**
  *主要研究手稿。包含了双向 EVT 雷达的完整数学推导、经典脑电特征与量子耗散参数（&gamma;, &epsilon;）之间的拓扑映射方程，以及严谨的防错反事实因果推断结果。*

为了详细解释 Wigner 演化流形、涨落耗散定理及该唯象模型的边界条件，我们准备了详细的白皮书文档：
- 👉 **[阅读 PDPP 理论框架白皮书 (简体中文)](./docs/PDPP_Theoretical_Framework_Whitepaper_ZH.md)**
- 👉 **[Read PDPP Theoretical Framework Whitepaper (English)](./docs/PDPP_Theoretical_Framework_Whitepaper_EN.md)**

## ⚙️ 快速启动（一键执行测试）

本项目为不同操作系统提供了专用的环境封装入口脚本，免去了配置复杂 Python 环境的烦恼。在安装 Python 3.9+ 之后，您可以直接双击下方文件启动引擎测试流程：

- **🍎 macOS 用户**：双击 `start.command`
- **🪟 Windows 用户**：双击 `start.bat`
- **🐧 Linux 用户**：在终端执行 `./start.sh`

> **✨ 自动化沙盒环境**：首次运行时，脚本将自动创建隔离的虚拟环境（`.venv`）并严格对齐所有的库依赖。初始化配置时请耐心等待！

---

## 💾 数据获取与代码连通性测试

为了遵守数据溯源与隐私合规要求，**本仓库内未存储任何真实的脑电原始大文件**。管线采用双层数据获取策略：

1. **自动拉取（首选）：** 首次运行且 `./data` 为空时，引擎将自动连接至 OpenNeuro AWS S3 服务器，提取 `ds003816` 数据集中符合 BIDS 标准的代表性样本。
2. **离线微小样本（备选）：** 若离线或受限，引擎将降级使用内置的 `./data_sample` 文件夹中的极微小降采样截断文件。该样本仅用于**代码管线连通性测试（验证编译、路由和无崩溃）**。

> [!WARNING]
> 示例微小数据集无法提供满足自由度的平稳时间序列，会导致引擎触发底层防错机制并中止贝叶斯因果计算。要验证完整的反事实推断，必须使用首选方案下载全量高精度数据集。

---

## 🔬 自定义数据复现指南 (Reproduction Guide)

PDPP 验证引擎支持导入您自己的高精度 EEG 数据进行相变扫描与因果推断。

**数据要求**：
- 支持格式：`.edf`, `.vhdr` (BrainVision), `.bdf`
- 通道要求：必须至少包含额叶（如 `Fz`, `F3`）与枕叶（如 `Oz`, `O1`, `O2`）或顶叶（如 `Pz`）导联，以便引擎提取长程 CFC 与 DMN 解耦拓扑特征。

**执行步骤**：
1. 将您的脑电文件放入根目录的 `data/` 文件夹（支持多层级子目录嵌套）。
2. （可选）为协助 EVT 雷达判断，若数据属于“长期冥想者/高阶干预状态”，请在文件名中包含 `lt`（如 `sub-01_task-meditation_lt.vhdr`）；基线对照组可不加或加其他后缀。
3. 打开终端执行主引擎入口：
   ```bash
   python main.py
   ```
4. 引擎将自动接管平稳性检验、动态峰值侦测及 BSTS 建模。所有分析结果及 Word/PDF 格式的研究报告将自动输出至 `Report/` 文件夹。

---

🧠 **引用 (Citation)**

如果您在学术研究中调用了本开源引擎的算法（如 EVT 极值雷达、BSTS 量子基线标定器等），请引用我们的底层方法论手稿：
```text
Jia, W., et al. "Macroscopic Topological Phase Transitions of the Neural Network Induce Non-Classical Causal Shielding on Quantum Decoherence: An Empirical Validation." arXiv (2026).
```
