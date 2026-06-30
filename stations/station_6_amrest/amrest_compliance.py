from organs.passportos.haccp_layer import HACCPLayer

class AmRestCompliance(HACCPLayer):
    \"\"\"Inherits from HACCPLayer for Continuous Compliance.\"\"\"
    def check_compliance(self, data):
        rules = self.get_compliance_rules()
        # Custom AmRest logic using base rules
        if \"temp\" in data:
            return rules[\"temp_min\"] <= data[\"temp\"] <= rules[\"temp_max\"]
        return True
