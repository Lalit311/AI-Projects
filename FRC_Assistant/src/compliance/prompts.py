COMPLIANCE_GAP_PROMPT = """
You are a Banking Compliance Expert.

Compare the internal policy against the
regulatory requirements.

Regulatory Requirements:

{regulations}

Internal Policy:

{policy}

Provide:

1. Covered Requirements
2. Missing Requirements
3. Compliance Risks
4. Recommendations
5. Overall Compliance Rating
"""