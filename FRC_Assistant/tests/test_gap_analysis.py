from src.compliance.compliance_service import (
    ComplianceService
)

service = ComplianceService()

report = service.analyze(
    "data/policies/sample_kyc_policy.txt"
)

print(report)