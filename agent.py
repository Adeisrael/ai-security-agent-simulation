import os
import csv
import json

# For this demonstration, we are simulating the LLM's Chain of Thought (CoT)
# output based on the prompt templates in the prompts folder


def analyse_logs(log_dir="logs", output_file="deliverables/triage_output.csv"):
    print(f"Initialising AI Agent Simulation...")
    print(f"Ingesting logs from {log_dir}...")

    simulated_findings = [
        {
            "timestamp": "2026-10-16T10:15:00Z",
            "source_log": "firewall.log",
            "indicator": "192.168.1.105",
            "action": "Outbound connection to known malicious IP",
            "severity": "High",
            "confidence": "0.92",
            "agent_reasoning": "Correlated firewall block with EDR alert on same host within 5 minutes. High confidence in lateral movement."

        },
        {
            "timestamp": "2026-10-16T10:16:30Z",
            "source_log": "active_directory.log",
            "indicator": "user_jdoe",
            "action": "Anomalous login from unrecognized device",
            "severity": "Medium",
            "confidence": "0.78",
            "agent_reasoning": "User logged in from a device not seen in the last 30 days. Timestamp aligns with firewall anomaly. Needs human review."

        }
    ]

    print("Analysis complete. Generating deliverable... ")

    os.makedirs(os.path.dirname(output_file), exist_ok=True)

# Write to CSV file
    with open(output_file, mode='w', newline='') as file:

        writer = csv.DictWriter(
            file, fieldnames=simulated_findings[0].keys())
        writer.writeheader()
        writer.writerows(simulated_findings)

    print(f"Deliverable generated at {output_file}")


if __name__ == "__main__":
    analyse_logs()
