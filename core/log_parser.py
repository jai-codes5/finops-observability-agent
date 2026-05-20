import json
import os
from typing import List, Dict, Any

class ObservabilityLogParser:
    def __init__(self, infrastructure_file_path: str):
        self.file_path = infrastructure_file_path

    def fetch_realtime_metrics(self) -> List[Dict[str, Any]]:
        """Reads mock cloud logs with built-in pipeline exceptions handling."""
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"Infrastructure ledger state file missing at {self.file_path}")
        
        try:
            with open(self.file_path, 'r') as file:
                data = json.load(file)
                return data.get("infrastructure_state", [])
        except json.JSONDecodeError:
            return []

    def extract_underutilized_nodes(self, cpu_threshold: float = 10.0) -> List[Dict[str, Any]]:
        """Filters nodes consuming waste energy directly matching pipeline arrays."""
        metrics = self.fetch_realtime_metrics()
        underutilized = []
        
        for node in metrics:
            # Algorithmic anomaly parsing validation
            if node.get("avg_cpu_utilization_percentage", 100.0) < cpu_threshold:
                underutilized.append(node)
        return underutilized