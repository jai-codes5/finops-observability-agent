from fastapi import FastAPI, HTTPException, BackgroundTasks
from pydantic import BaseModel
from typing import List, Dict, Any
import os

# Absolute explicit package paths modules bindings import
from core.log_parser import ObservabilityLogParser
from core.orchestrator import FinOpsAIOperationsOrchestrator
from core.cloud_executor import AutonomousCloudInfrastructureExecutor

app = FastAPI(
    title="Enterprise AI FinOps & Observability Control Engine",
    version="2026.1.0",
    description="Production-ready asynchronous autonomous cloud governance network platform"
)

DB_PATH = "test_infrastructure.json"

@app.get("/api/v1/observability/metrics")
def get_cluster_metrics():
    """Endpoint exposing full server system tracking parameters."""
    try:
        parser = ObservabilityLogParser(infrastructure_file_path=DB_PATH)
        return {"status": "SUCCESS", "data": parser.fetch_realtime_metrics()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/v1/finops/analyze")
def analyze_and_optimize_costs():
    """Runs data pipeline through sequential autonomous analysis and optimization passes."""
    try:
        parser = ObservabilityLogParser(infrastructure_file_path=DB_PATH)
        orchestrator = FinOpsAIOperationsOrchestrator()
        
        # Phase 1: Catch wasted allocations
        waste = parser.extract_underutilized_nodes(cpu_threshold=10.0)
        
        # Phase 2: Compute target reduction margins
        recommendations = orchestrator.evaluate_cost_impact(waste_resources=waste)
        
        return {
            "status": "ANALYSIS_COMPLETE",
            "detected_idle_nodes_count": len(waste),
            "optimization_strategies": recommendations
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/v1/finops/execute")
def enforce_autonomous_governance():
    """Executes state-driven optimization parameters to downscale resources safely."""
    try:
        parser = ObservabilityLogParser(infrastructure_file_path=DB_PATH)
        orchestrator = FinOpsAIOperationsOrchestrator()
        executor = AutonomousCloudInfrastructureExecutor(infrastructure_file_path=DB_PATH)
        
        waste = parser.extract_underutilized_nodes(cpu_threshold=10.0)
        recommendations = orchestrator.evaluate_cost_impact(waste_resources=waste)
        
        if not recommendations:
            return {"status": "SKIPPED", "message": "Infrastructure operates at optimal cost constraints."}
            
        success = executor.execute_infrastructure_downscale(recommendations=recommendations)
        
        if success:
            return {
                "status": "INFRASTRUCTURE_MUTATED",
                "message": "Optimization strategies successfully executed on live clusters.",
                "applied_actions": recommendations
            }
        else:
            raise HTTPException(status_code=500, detail="State mutation aborted during cluster update cycle.")
            
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)