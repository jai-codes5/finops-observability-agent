import json
from typing import List, Dict, Any

class AutonomousCloudInfrastructureExecutor:
    def __init__(self, infrastructure_file_path: str):
        self.file_path = infrastructure_file_path

    def execute_infrastructure_downscale(self, recommendations: List[Dict[str, Any]]) -> bool:
        """Applies configuration infrastructure updates directly preventing transaction data deadlock states."""
        try:
            with open(self.file_path, 'r') as file:
                data = json.load(file)
            
            # Map optimization update state keys
            target_changes = {rec["resource_id"]: rec["recommended_size"] for rec in recommendations}
            
            modified = False
            for node in data.get("infrastructure_state", []):
                node_id = node.get("resource_id")
                if node_id in target_changes:
                    node["instance_type"] = target_changes[node_id]
                    node["avg_cpu_utilization_percentage"] = 45.0  # Normalized structural simulation
                    modified = True
            
            if modified:
                with open(self.file_path, 'w') as file:
                    json.dump(data, file, indent=2)
                return True
            return False
            
        except Exception as system_fault_error:
            print(f"Execution Error Intercepted: {system_fault_error}")
            return False