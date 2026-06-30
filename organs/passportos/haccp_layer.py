import re

class HACCPLayer:
    \"\"\"Single source of truth for HACCP rules and SSCC validation.\"\"\"
    
    @staticmethod
    def validate_sscc(sscc: str) -> bool:
        \"\"\"SD- followed by 15 digits (18 chars total).\"\"\"
        return bool(re.match(r\"^SD-\\d{15}$\", sscc))

    @staticmethod
    def get_compliance_rules():
        return {
            \"temp_min\": -18.0,
            \"temp_max\": 4.0,
            \"label_required\": True,
            \"traceability_enabled\": True
        }
