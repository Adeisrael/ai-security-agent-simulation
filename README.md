# Autonomous AI Security Agent Simulation

An enterprise-grade demonstration of using **Agentic AI** inside a sandboxed environment to ingest, triage, and correlate multi-file network infrastructure logs.

## 🚀 Project Overview
This project showcases how an autonomous AI agent can replace manual security operations center (SOC) triage pipelines. Using a strict multi-step execution loop and **enforced Chain-of-Thought (CoT) tracking**, the agent independently transforms chaotic corporate log layers into a structured Incident Response deliverable.

## 🛠️ The Architecture & Data Flow
1. **Source Generation:** Synthesized 20 distinct log layers (Firewall, EDR, Cloud, Active Directory) injected with a stealthily staggered kill-chain attack vector.
2. **Agent Ingestion:** The AI agent analyzes raw text structures, maps overlapping timelines, and exposes interconnected entity indicators (IPs/Usernames).
3. **Self-Documentation:** The agent logs an internal execution journal detailing its active inspections, confident decisions, and structural logical uncertainties.
4. **Deliverable Production:** Generates a structured `.csv` asset.

## 🧪 Evaluation & Results

I evaluated the agent on a set of 20 synthetic log layers containing a deliberately injected attack vector.
*   **Detection Rate:** The agent successfully correlated the firewall block with the Active Directory anomaly, identifying the lateral movement (True Positive).
*   **Confidence Handling:** The agent correctly flagged the AD login as "Medium" confidence (0.78) requiring human review, rather than falsely escalating it to "High" severity, demonstrating basic uncertainty awareness.

## ⚠️ Limitations & Future Work

*   **Synthetic Data:** The logs are synthetic and do not contain the noise of a real enterprise environment. Future work would involve testing against a public dataset like CIC-IDS2017.
*   **Cost/Latency:** This simulation does not measure the API latency or cost of running the LLM at scale, which is critical for SOC deployment.
*   **Prompt Injection:** The agent currently trusts the log inputs. Future work will focus on hardening the agent against indirect prompt injection attacks embedded in the logs themselves.

## 📁 Repository Contents
* `/logs`: The 20 raw mock data assets used to test the environment.
* `/prompts`: The exact prompt templates engineered to enforce agent logic, prevent hallucinations, and override output shortcuts.
* `/deliverables`: The final structured CSV metric.
* `agent.py`: The Python script that executes the analysis.
