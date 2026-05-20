from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
import json
import threading
from typing import List, Dict, Any

# Core application background processing imports
from core.log_parser import ObservabilityLogParser
from core.orchestrator import FinOpsAIOperationsOrchestrator
from core.cloud_executor import AutonomousCloudInfrastructureExecutor

app = FastAPI(
    title="Enterprise AI FinOps & Observability Control Engine",
    version="2026.1.1",
    description="Production-ready multi-threaded secure autonomous cloud governance core network engine"
)

# Cross-Origin Resource Sharing logic integration models setup (React configuration security layer initialization)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

DB_PATH = "test_infrastructure.json"
CONFIG_PATH = "config/agent_config.json"

# Production Thread Synchronization Primitive (Prevents absolute system write corruption deadlocks during state mutations)
file_system_mutex_lock = threading.Lock()

class DynamicConfigLoader:
    @staticmethod
    def load_governance_policy() -> Dict[str, Any]:
        """Loads live threshold logic limits directly from external metadata without restarting runtime nodes."""
        if not os.path.exists(CONFIG_PATH):
            return {"observability_thresholds": {"underutilization_cpu_percentage": 10.0}}
        try:
            with open(CONFIG_PATH, 'r') as file:
                return json.load(file)
        except Exception:
            return {"observability_thresholds": {"underutilization_cpu_percentage": 10.0}}

@app.get("/api/v1/observability/metrics")
def get_cluster_metrics():
    """Endpoint exposing real-time safe transactional database file array processing snapshots."""
    with file_system_mutex_lock:
        try:
            parser = ObservabilityLogParser(infrastructure_file_path=DB_PATH)
            return {"status": "SUCCESS", "data": parser.fetch_realtime_metrics()}
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Database Read Fault Intercepted: {str(e)}")

@app.get("/api/v1/finops/analyze")
def analyze_and_optimize_costs():
    """Runs data streams matching live operational configuration definitions dynamically."""
    with file_system_mutex_lock:
        try:
            # Step 1: Read dynamic threshold policies from decentralized config system layer
            config_data = DynamicConfigLoader.load_governance_policy()
            cpu_limit = config_data.get("observability_thresholds", {}).get("underutilization_cpu_percentage", 10.0)
            
            parser = ObservabilityLogParser(infrastructure_file_path=DB_PATH)
            orchestrator = FinOpsAIOperationsOrchestrator()
            
            # Step 2: Dynamic analysis using policy injection parameters
            waste = parser.extract_underutilized_nodes(cpu_threshold=cpu_limit)
            recommendations = orchestrator.evaluate_cost_impact(waste_resources=waste)
            
            return {
                "status": "ANALYSIS_COMPLETE",
                "active_policy_cpu_threshold": cpu_limit,
                "detected_idle_nodes_count": len(waste),
                "optimization_strategies": recommendations
            }
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"AI Engine Optimization Pass Aborted: {str(e)}")

@app.post("/api/v1/finops/execute")
def enforce_autonomous_governance():
    """Executes atomic isolated mutation updates utilizing transaction isolation thread parameters protection."""
    with file_system_mutex_lock:
        try:
            config_data = DynamicConfigLoader.load_governance_policy()
            cpu_limit = config_data.get("observability_thresholds", {}).get("underutilization_cpu_percentage", 10.0)
            
            parser = ObservabilityLogParser(infrastructure_file_path=DB_PATH)
            orchestrator = FinOpsAIOperationsOrchestrator()
            executor = AutonomousCloudInfrastructureExecutor(infrastructure_file_path=DB_PATH)
            
            waste = parser.extract_underutilized_nodes(cpu_threshold=cpu_limit)
            recommendations = orchestrator.evaluate_cost_impact(waste_resources=waste)
            
            if not recommendations:
                return {"status": "SKIPPED", "message": "Cluster resources match exact optimization metrics targets configuration profiles."}
                
            success = executor.execute_infrastructure_downscale(recommendations=recommendations)
            
            if success:
                return {
                    "status": "INFRASTRUCTURE_MUTATED",
                    "applied_actions": recommendations
                }
            else:
                raise HTTPException(status_code=500, detail="State controller mutation runtime sequence fault.")
                
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Governance Enforcement Error: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)