# DARTRIX OS: Continuous Cold Chain Compliance
## UiPath AgentHack 2026 Submission

### Project Description
**DARTRIX OS** is an agentic, crash-only software architecture designed to enforce continuous cold chain compliance across industrial food processing and pharmaceutical logistics.

The system operates on a persistent dual-core loop:
- **NEXUS Anomaly Detection**: Evaluates real-time environmental telemetry against critical HACCP (Hazard Analysis and Critical Control Points) thresholds.
- **CYCLUS Corrective Action (6-9-3-6 Loop)**: Executes automated, feedback-driven corrective adjustments when anomalies are detected, ensuring complete traceability via PassportOS.

---

### Agent Type
- **Coded Agent**: Custom Python-driven agentic logic featuring **DualCoreManager** and **SoniaCommander** decision analysis, orchestrated via UiPath APIs.

---

### UiPath Components Used
- **UiPath Orchestrator**: Manages operational queues, secures API credentials, and logs system-wide transactional ticks.
- **UiPath Robots**: Executes low-level terminal actions, dispatches alerts, and updates physical SCADA interface settings based on CYCLUS directives.
- **UiPath Integration Service**: Connects real-time IoT sensor telemetry streams directly to the DARTRIX OS ingestion layer.

---

### Setup and Installation

#### 1. Clone the repository
```bash
git clone https://github.com/Dirigentrix/dartrix-wankel-696.git
cd dartrix-wankel-696
```

#### 2. Environment Configuration
Ensure **Python 3.14+** is installed. Set your API credentials:
```bash
export DASHSCOPE_API_KEY="your_key"
```

#### 3. Local Execution (Demo Mode)
To run the zero-dependency AgentHack demo flow:
```bash
python agenthack_cycleflow.py
```

#### 4. Production Execution (Modular Mode)
To run the full multi-agent system with persistent SQLite WAL storage:
```bash
python main.py
```

---

### Architecture Overview
The DARTRIX engine utilizes a unique dual-core orchestration:
- **CYCLUS (Core 1)**: Sequential 6->9->6 flow logic for deterministic execution.
- **NEXUS (Core 2)**: Anomaly calculation and Qwen-enabled orchestration for intelligent response.
- **NINIA Layer**: Interceptor layer for payload analysis and routing.

### Internal Commands
- `tick`: Advance the cycle.
- `status`: View core numerology and states.
- `route <msg>`: Manually route a message through Ninia.
