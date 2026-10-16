# Data Generator 

## Purpose
This prompt initialises 20 simulated security logs that would be used for the project. This is used because of high sensitive data associated with corporate networks. It builds a realistic, 20-file multi-layer log ecosystem embedded with a hidden cyberattack kill-chain, providing the necessary mock dataset to test our agent without risking real production logs.

## Engineering Strategy
Generating 20 highly detailed logs in a single window can cause an LLM to hit token generation limits, leading to cut-off text or dropped formatting. To prevent this, the data generation strategy is split into two sequential batches of 10 files each, ensuring structural integrity across all 20 network assets.

---

## Batch 1: Files 1 to 10

### Instruction Prompt
Copy and paste this exact prompt into ChatGPT to generate the first half of your log directory folder:

```text
You are a Security Data Generator. Your task is to generate 20 separate, distinct text blocks that mimic raw corporate logs from different network layers. To manage text limits, generate the first 10 files now. I will ask for the remaining 10 in the next prompt.

Ensure each log contains standard technical noise (timestamps, source/destination IPs, IDs) but inject specific attack or policy violation patterns throughout the environment. Format your output exactly as separate file blocks inside Markdown code blocks, clearly labeled:

--- FILE 1: firewall_edge_01.log ---
(8 lines of edge traffic logs. Inject a rapid SSH brute-force attack from an external IP).

--- FILE 2: app_server_web.log ---
(8 lines of HTTP server web logs. Inject a SQL Injection payload like ' OR 1=1 --).

--- FILE 3: internal_auth.log ---
(8 lines of domain controller logs. Inject an employee account logging into a sensitive file server at 3:15 AM).

--- FILE 4: endpoint_detection_edr.log ---
(8 lines of workstation logs. Inject an unknown script executing out of a local AppData\Temp folder).

--- FILE 5: cloud_storage_audit.log ---
(8 lines of AWS S3 logs. Inject an external IP downloading a file named "client_financials_2026.csv").

--- FILE 6: vpn_gateway_east.log ---
(8 lines of VPN access logs. Inject an impossible travel event: a user logging in from New York, and 10 minutes later logging in from Paris).

--- FILE 7: email_security_gateway.log ---
(8 lines of inbound mail routing logs. Inject a high-risk phishing email containing a malicious link like "http://update-your-hr-portal.net").

--- FILE 8: dns_query_server.log ---
(8 lines of DNS server lookups. Inject a data exfiltration pattern via DNS tunneling: multiple long, cryptic subdomains querying a suspicious domain like ://malicious-site.com).

--- FILE 9: database_audit_mysql.log ---
(8 lines of raw SQL execution logs. Inject a database enumeration attempt showing multiple rapid commands like SHOW TABLES; and SELECT * FROM credit_cards;).

--- FILE 10: active_directory_changes.log ---
(8 lines of AD modification logs. Inject a privilege escalation event where a standard user account is suddenly added to the "Domain Admins" security group).

Provide the raw text of these first 10 logs inside clear individual code blocks. Do not add conversational intro text.
```

---

## Batch 2: Files 11 to 20

### Instruction Prompt
Paste this second prompt immediately into the same chat window after Batch 1 completes to finalize your log directory folder:

```text
Excellent. Now generate the remaining 10 log files to complete the 20-file workspace folder. Continue using the exact same format with individual Markdown code blocks:

--- FILE 11: dhcp_lease_tracker.log ---
(8 lines of IP allocation logs. Inject a rogue device MAC address repeatedly requesting local IP leases).

--- FILE 12: proxy_web_filter.log ---
(8 lines of outbound web traffic. Inject an internal workstation bypassing corporate filters to communicate with a known Command and Control (C2) server IP).

--- FILE 13: linux_syslog_web02.log ---
(8 lines of Linux system event logs. Inject a user running sudo commands without authorization or a local root privilege escalation attempt).

--- FILE 14: windows_event_security.log ---
(8 lines of local OS logs. Inject Event ID 4625 (Failed logon) followed by a sudden clearing of the local security event logs to hide tracks).

--- FILE 15: kubernetes_api_audit.log ---
(8 lines of container orchestration logs. Inject an unauthenticated API request attempting to launch a rogue container running a crypto-miner script).

--- FILE 16: api_gateway_prod.log ---
(8 lines of microservice gateway requests. Inject an API rate-limiting violation where a single key is scraping product data via massive automated requests).

--- FILE 17: wireless_controller_office.log ---
(8 lines of corporate Wi-Fi logs. Inject a MAC spoofing warning or a rogue access point broadcast interference event).

--- FILE 18: single_sign_on_okta.log ---
(8 lines of SSO logs. Inject a MFA prompt fatigue attack: multiple push notifications sent to an executive's device in the middle of the night until finally approved).

--- FILE 19: patch_management_status.log ---
(8 lines of system patching logs. Highlight a critical unpatched zero-day vulnerability sitting on a production database server flag).

--- FILE 20: physical_access_badge.log ---
(8 lines of server room badge swipe data. Inject a standard employee badging into a high-security server cage without prior clearance).

Provide the raw text of these final 10 logs inside individual code blocks.
```