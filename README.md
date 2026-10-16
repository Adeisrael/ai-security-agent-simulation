# Autonomous AI Security Agent Simulation

An enterprise-grade demonstration of using **Agentic AI** inside a sandboxed environment to ingest, triage, and correlate multi-file network infrastructure logs.

## 🚀 Project Overview
This project showcases how an autonomous AI agent can replace manual security operations center (SOC) triage pipelines. Using a strict multi-step execution loop and **enforced Chain-of-Thought (CoT) tracking**, the agent independently transforms 20 chaotic corporate log layers into a single, reviewable Incident Response deliverable.

## 🛠️ The Architecture & Data Flow
1. **Source Generation:** Synthesized 20 distinct log layers (Firewall, EDR, Cloud, Active Directory) injected with a stealthily staggered kill-chain attack vector.
2. **Agent Ingestion:** The AI agent analyzes raw text structures, maps overlapping timelines, and exposes interconnected entity indicators (IPs/Usernames).
3. **Self-Documentation:** The agent logs an internal execution journal detailing its active inspections, confident decisions, and structural logical uncertainties.
4. **Deliverable Production:** Generates a structured `.csv` asset.

## 📁 Repository Contents
* `/logs`: The 20 raw mock data assets used to test the environment.
* `/prompts`: The exact prompt templates engineered to enforce agent logic, prevent hallucinations, and override output shortcuts.
* `/deliverables`: The final structured CSV metric.
