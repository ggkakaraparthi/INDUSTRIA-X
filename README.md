# Nexora
NEURAX HACKATHON 3.0
DOMAIN 2 · AI IN INDUSTRY AND AUTOMATION
Problem Statement: Visual Inspection & Defect Root-Cause Assistant
# AI-Driven Manufacturing Process Intelligence

## 1. Project Overview

Manufacturing systems continuously generate process information such as demand, production output, processing time, waiting time, resource utilization, queue levels and quality-related production outcomes. Converting this data into timely operational decisions is an important challenge in intelligent manufacturing.

Our project develops an **AI-assisted Manufacturing Process Intelligence system** that analyzes manufacturing-process data to identify inefficient process conditions, detect potential bottlenecks, investigate contributing factors, estimate operational impact, and provide explainable recommendations for process improvement.

The system is designed around the **AI in Automation Industries** theme and uses a manufacturing dataset generated through **Discrete-Event Simulation (DES)**.

---

## 2. Problem We Address

A manufacturing process may experience:

* High resource utilization
* Increasing waiting or queue time
* Uneven utilization across production stages
* Reduced production throughput
* Accumulation of parts between processes
* Variations in production performance under different demand conditions
* Quality-related output variations

Traditional monitoring can show these measurements individually, but the decision-maker still needs to answer:

> **Where is the process becoming inefficient, what factors are associated with the problem, and what action should be investigated?**

Our system aims to connect these measurements into a single analytical pipeline.

---

## 3. Research Foundation

Our dataset is based on the research work:

**K. C. Chan, M. Rabaev and H. Pratama,
"Generation of synthetic manufacturing datasets for machine learning using discrete-event simulation,"
Production & Manufacturing Research, Vol. 10, No. 1, pp. 337–353, 2022.**

DOI: 10.1080/21693277.2022.2086642

The research proposes the use of **Discrete-Event Simulation (DES)** to generate large synthetic manufacturing datasets for machine-learning research. The authors designed three manufacturing simulation models with increasing levels of complexity and released the resulting datasets publicly through Mendeley Data.

The research identifies DES-generated data as useful for manufacturing ML applications because real production data can be difficult to obtain, while simulation can generate controlled production scenarios containing process variability.

---

## 4. Dataset

### Dataset

**Manufacturing Data Shared Facility – Discrete-Event Simulation**

Source:

Mendeley Data
https://data.mendeley.com/datasets/3rw227zxt7/2

The dataset contains three manufacturing simulation models:

### Model 1 — Sequential Manufacturing Process

Model 1 represents a simple sequential production line involving:

**Drilling → Milling → Assembly**

The dataset records manufacturing characteristics including:

* Demand
* Production rate
* Value-added time
* Waiting time at individual processes
* Resource utilization

The research describes Model 1 as the simplest manufacturing layout and intentionally creates different utilization levels through different resource capacities.

### Model 2 — Extended Sequential Process

Model 2 provides a more detailed representation of the manufacturing flow, including:

* Part-flow information
* Processing time
* Queue/waiting information
* Storage information
* Production output
* Resource utilization

This allows the system to investigate not only resource usage but also the movement and accumulation of parts through the manufacturing process.

### Model 3 — Flexible Manufacturing System

Model 3 is the most complex of the three simulation models and contains **77 features**.

The dataset includes groups of variables representing:

* Resource utilization
* Queue levels
* SKU-related production counters
* Production after quality checking
* Process and manufacturing information

The research describes Model 3 as a flexible manufacturing layout containing multiple manufacturing cells and a final painting and quality-checking stage.

---

## 5. Why Synthetic Manufacturing Data?

The dataset is not collected directly from a physical factory.

It is generated using **Discrete-Event Simulation**, which models manufacturing events and process behavior.

The research framework follows the general pipeline:

```text
Manufacturing Layout
        ↓
Demand / Process Definition
        ↓
Discrete-Event Simulation
        ↓
Manufacturing Experiments
        ↓
Synthetic Production Data
        ↓
Machine Learning / Data Analysis
```

This is important because our project is not claiming that the dataset represents measurements from one real factory.

Instead, we use the simulated manufacturing scenarios as a controlled environment for developing and demonstrating AI-based manufacturing analysis.

---

# 6. Proposed Solution

Our system transforms raw manufacturing-process data into actionable process intelligence.

```text
                 MANUFACTURING DATA
                         ↓
                DATA PREPROCESSING
                         ↓
              EXPLORATORY DATA ANALYSIS
                         ↓
          ┌──────────────┼──────────────┐
          ↓              ↓              ↓
       QUALITY       BOTTLENECK      IMPACT
       / AI          ANALYSIS        ANALYSIS
          │              │              │
          └──────────────┼──────────────┘
                         ↓
                  ROOT-CAUSE ANALYSIS
                         ↓
                  AI INSIGHT ENGINE
                         ↓
                  RECOMMENDATIONS
                         ↓
                  INTERACTIVE UI
```

The exact machine-learning task and model will be selected after analysing the provided dataset and determining which target variables and relationships are statistically meaningful.

---

# 7. Core Intelligence Modules

## Module 1 — AI-Based Manufacturing Analysis

This module investigates whether manufacturing performance or abnormal process conditions can be predicted from available process variables.

Potential information includes:

* Demand
* Production rate
* Processing time
* Waiting time
* Utilization
* Queue levels
* SKU/process information

Possible ML approaches will be selected based on the structure of the target variable, rather than assuming a particular algorithm beforehand.

Potential tasks include:

* Performance prediction
* Classification
* Regression
* Anomaly detection
* Feature-importance analysis

---

## Module 2 — Bottleneck and Root-Cause Analysis

This module focuses on identifying process stages associated with manufacturing inefficiency.

The analysis will examine relationships among:

```text
Utilization
     +
Queue / Waiting Time
     +
Processing Time
     +
Production Output
     ↓
Process Behaviour
```

A process stage will not be labelled as a causal bottleneck from a single measurement.

Instead, the system will analyse multiple observations and supporting indicators to identify **potential bottleneck conditions and associated factors**.

For example:

```text
High Utilization
       +
Increasing Queue
       +
Increased Waiting
       +
Reduced Output
       ↓
Potential Process Constraint
```

The research itself highlights bottleneck analysis as one of the manufacturing applications for which machine-learning approaches can be applied.

---

## Module 3 — Operational Impact and Decision Dashboard

The final module converts analytical results into an understandable operational view.

The dashboard will present, where supported by the dataset:

* Demand
* Production output
* Production rate
* Resource utilization
* Waiting/queue levels
* Process performance
* Potential bottlenecks
* Important contributing variables
* Estimated operational impact
* AI-generated recommendations

If monetary cost information is not available in the supplied dataset, the system will not present invented monetary values as actual factory costs. Instead, operational measures such as throughput, waiting time, utilization and production output will be used, or monetary estimates will be explicitly identified as assumption-based.

---

# 8. AI Decision Flow

The intended decision flow is:

```text
"What is happening?"
        ↓
Process monitoring
        ↓
"Where is it happening?"
        ↓
Bottleneck / abnormal-condition analysis
        ↓
"What factors are associated with it?"
        ↓
Root-cause analysis
        ↓
"What could be affected?"
        ↓
Operational impact
        ↓
"What should be investigated?"
        ↓
AI-assisted recommendation
```

The system therefore focuses not only on prediction, but on connecting **prediction → explanation → operational impact → recommendation**.

---

# 9. Example Insight

An example output of the proposed system could be:

```text
PROCESS ALERT

Potential Constraint:
Assembly Stage

Observed Indicators:
• High resource utilization
• Increased waiting/queue level
• Lower production throughput

Associated Factors:
• Process utilization
• Waiting time
• Demand level

Operational Impact:
Potential reduction in production efficiency.

Recommended Investigation:
Review assembly-stage capacity and operating
conditions under the observed demand scenario.
```

This is an analytical recommendation rather than an automatic claim that a single variable caused the observed result.

---

# 10. Team Architecture

Our three-member team works on independent modules simultaneously.

### Member 1 — AI / Manufacturing Prediction

Responsibilities:

* Data preprocessing
* Feature engineering
* ML model development
* Model evaluation
* Feature importance / explainability
* Quality and production-performance analysis

### Member 2 — Bottleneck / Root-Cause Intelligence

Responsibilities:

* Process-flow analysis
* Utilization analysis
* Queue and waiting-time analysis
* Bottleneck identification
* Root-cause investigation
* Process-performance relationships

### Member 3 — Impact / Dashboard / Integration

Responsibilities:

* KPI computation
* Operational-impact analysis
* Interactive dashboard
* Visualization
* Integration of outputs from Members 1 and 2
* Final recommendation interface

---

# 11. Technology Stack

### Programming

* Python

### Data Processing

* Pandas
* NumPy

### Machine Learning

* Scikit-learn

### Visualization

* Matplotlib
* Plotly

### Application

* Streamlit

### Development

* Jupyter Notebook
* Git
* GitHub

The final algorithm selection will depend on the characteristics of the supplied manufacturing data.

---

# 12. System Architecture

```text
                  ┌───────────────────────┐
                  │ Manufacturing Dataset │
                  │ Model 1 / 2 / 3       │
                  └───────────┬───────────┘
                              ↓
                    ┌──────────────────┐
                    │ Data Preprocessing│
                    └────────┬─────────┘
                             ↓
                  ┌─────────────────────┐
                  │ Feature Engineering │
                  └─────────┬───────────┘
                            ↓
              ┌─────────────┼─────────────┐
              ↓             ↓             ↓
        ┌──────────┐  ┌────────────┐  ┌──────────┐
        │ AI/ML    │  │ Bottleneck │  │ Impact   │
        │ Analysis │  │ + Root     │  │ Analysis │
        │          │  │ Cause      │  │          │
        └────┬─────┘  └─────┬──────┘  └────┬─────┘
             │              │              │
             └──────────────┼──────────────┘
                            ↓
                   ┌──────────────────┐
                   │ Insight Engine   │
                   └────────┬─────────┘
                            ↓
                   ┌──────────────────┐
                   │ Recommendations  │
                   └────────┬─────────┘
                            ↓
                   ┌──────────────────┐
                   │ Streamlit UI     │
                   └──────────────────┘
```

---

# 13. Expected Outputs

The completed prototype is expected to provide:

### Manufacturing KPIs

* Production output
* Production rate
* Resource utilization
* Waiting time
* Queue levels

### AI Analysis

* Predicted manufacturing performance or condition
* Important contributing features
* Anomaly/abnormal-condition indicators where applicable

### Process Intelligence

* Potential bottleneck
* Supporting evidence
* Associated process factors

### Decision Support

* Operational impact
* Explainable insights
* Recommended areas for investigation

---

# 14. Research-to-Prototype Connection

The project is directly inspired by the dataset's research foundation.

The research establishes that DES can be used to generate manufacturing datasets suitable for subsequent machine-learning and data-analysis tasks. It also demonstrates increasing dataset dimensionality as manufacturing-system complexity increases: the first model contains a small set of process variables, while the third model contains 77 dimensions.

Our contribution is **not the generation of the synthetic dataset itself**.

Instead, our prototype uses the generated manufacturing data as the input to an **AI-assisted decision-support layer**:

```text
Research Contribution
DES → Synthetic Manufacturing Data
             ↓
       OUR CONTRIBUTION
Data → AI Analysis → Bottleneck/Root Cause
                   → Impact
                   → Recommendation
```

This distinction keeps the project technically and academically accurate.

---

# 15. Limitations

* The dataset is synthetic rather than directly collected from a physical production facility.
* Results obtained from simulation data may not directly represent every real manufacturing environment.
* The dataset does not by itself establish causal relationships between process variables.
* Monetary impact can only be calculated when appropriate cost information or explicit assumptions are available.
* The final ML task depends on the target variables and structure of the provided data.

---

# 16. Future Scope

The prototype can be extended toward:

* Real-time factory data integration
* Digital-twin-based monitoring
* Predictive maintenance
* Quality prediction
* Production scheduling
* Capacity optimization
* What-if process simulation
* Reinforcement-learning-based process optimization
* Integration with Industrial IoT systems
* Validation using real production data

---

# 17. Project Status

### Phase 1 — Dataset Understanding

In progress

### Phase 2 — Data Preprocessing

Planned

### Phase 3 — AI / Process Intelligence

Planned

### Phase 4 — Bottleneck and Root-Cause Analysis

Planned

### Phase 5 — Dashboard Integration

Planned

### Phase 6 — Testing and Demonstration

Planned

---

# 18. Reference

Chan, K. C., Rabaev, M., & Pratama, H. (2022).

**Generation of synthetic manufacturing datasets for machine learning using discrete-event simulation.**

*Production & Manufacturing Research, 10(1), 337–353.*

DOI: 10.1080/21693277.2022.2086642

Dataset:

**Manufacturing Data Shared Facility – Discrete-Event Simulation**

Mendeley Data, Version 2.

---

## License / Dataset Attribution

The original research and dataset are attributed to their respective authors and repository. The dataset is distributed under the license specified by Mendeley Data.

This project uses the dataset for hackathon development and analytical experimentation.
