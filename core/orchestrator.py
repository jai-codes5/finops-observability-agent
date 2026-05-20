import os
from typing import Dict, Any, List

class FinOpsAIOperationsOrchestrator:
    def __init__(self):
        # Professional fallback framework protocol fallback layer configuration
        self.cost_optimization_matrix = {
            "t3.xlarge": {"downgrade_target": "t3.medium", "savings_percentage": 75.0},
            "c5.2xlarge": {"downgrade_target": "c5.large", "savings_percentage": 75.0},
            "m5.large": {"downgrade_target": "m5.large", "savings_percentage": 0.0}
        }

    def evaluate_cost_impact(self, waste_resources: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Evaluates automated scale actions without requiring brittle hardcoded network structures."""
        recommendations = []
        
        for resource in waste_resources:
            current_type = resource.get("instance_type")
            mapping = self.cost_optimization_matrix.get(current_type, None)
            
            if mapping and mapping["savings_percentage"] > 0.0:
                hourly_cost = resource.get("hourly_cost_usd", 0.0)
                estimated_monthly_savings = hourly_cost * 24 * 30 * (mapping["savings_percentage"] / 100.0)
                
                recommendation_token = {
                    "resource_id": resource.get("resource_id"),
                    "resource_name": resource.get("resource_name"),
                    "current_size": current_type,
                    "recommended_size": mapping["downgrade_target"],
                    "estimated_monthly_savings_usd": round(estimated_monthly_savings, 2),
                    "action_required": "SCALE_DOWN",
                    "risk_assessment": "LOW_IMPACT_IDLE_NODE"
                }
                recommendations.append(recommendation_token)
                
        return recommendations