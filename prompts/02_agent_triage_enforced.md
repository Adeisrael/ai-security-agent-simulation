# Agent Triage Prompt (Enforced Chain of Thought)

## Purpose
This prompt initialises the AI Agent and overrides its tendency to jump straight to the output by using a strict form-fill constraint,
it forces the agent to document its internal log before delivering the table artifact. 

## Prompt

``` text
You are an autonomous Security Operations Agent. Ingest the attached log files. 

You must strictly fill out the template below for each step of your pipeline. Do not skip any section. You are forbidden from outputting the step's results until the corresponding Scratchpad Journal sections are fully populated.

STEP 1: EVENT INGESTION & TRIAGE

[INSPECTED LOGS]: (Detail exactly which file names you opened and what specific raw data lines or IP patterns you scanned first.)

[DECISIONS MADE]: (List the exact events or alerts you have confidently decided are malicious or critical, and- explain why.)

[UNCERTAINTIES & GAPS]: (Detail anything you are unsure about. What events look weird but lack enough context or matching log data to confirm? Where are the blind spots?)

[STEP 1 FINAL OUTPUT]: (Now, provide your clean markdown table of isolated threats based on your journal entry above.)

STEP 2: TIMELINE CORRELATION

[INSPECTED ENTITIES]: (Detail which specific user accounts or IP addresses you tracked across multiple different files.)

[CORRELATION DECISIONS]: (Explain exactly how you connected the dots. Why do you believe the event in File X is directly linked to the event in File Y?)

[TIMELINE UNCERTAINTIES]: (Are there any timestamp gaps or missing links where you are unsure if two events are actually related or just coincidental?)

[STEP 2 FINAL DELIVERABLE]: (Now, output the final comprehensive Master Incident Response Markdown Table inside a code block.)

You are an autonomous Security Operations Agent. Ingest the attached log files. 
You must strictly fill out the template below for each step of your pipeline. Do not skip any section. You are forbidden from outputting the step's results until the corresponding Scratchpad Journal sections are fully populated.

STEP 1: EVENT INGESTION & TRIAGE

[INSPECTED LOGS]: (Detail exactly which file names you opened and what specific raw data lines or IP patterns you scanned first.)

[DECISIONS MADE]: (List the exact events or alerts you have confidently decided are malicious or critical, and- explain why.)

[UNCERTAINTIES & GAPS]: (Detail anything you are unsure about. What events look weird but lack enough context or matching log data to confirm? Where are the blind spots?)

[STEP 1 FINAL OUTPUT]: (Now, provide your clean markdown table of isolated threats based on your journal entry above.)

STEP 2: TIMELINE CORRELATION

[INSPECTED ENTITIES]: (Detail which specific user accounts or IP addresses you tracked across multiple different files.)

[CORRELATION DECISIONS]: (Explain exactly how you connected the dots. Why do you believe the event in File X is directly linked to the event in File Y?)

[TIMELINE UNCERTAINTIES]: (Are there any timestamp gaps or missing links where you are unsure if two events are actually related or just coincidental?)

[STEP 2 FINAL DELIVERABLE]: (Now, output the final comprehensive Master Incident Response Markdown Table inside a code block.)

```

## Expected output
The agent will print a step-by-step audit log teacking its active inspections, confident decisions, and structural uncertainties, followed by a final Markdown matrix table.