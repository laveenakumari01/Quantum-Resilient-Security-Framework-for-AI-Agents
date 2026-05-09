"""
Real-time Alert Generation System
Intelligent Monitoring
Monitors agent behavior using ML model and generates alerts.
"""

import json
import os
import sys
from datetime import datetime

# Fix path to work from any location
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
ALERTS_DIR = os.path.join(BASE_DIR, "anomaly_detection", "alerts")
ALERTS_FILE = os.path.join(ALERTS_DIR, "alerts.json")

from anomaly_detection.anomaly_detector import predict

def generate_alert(agent_id, behavior_data, prediction_result):
    """
    Generate and save alert for agent behavior.
    Args:
        agent_id: Unique agent ID
        behavior_data: Agent behavior metrics
        prediction_result: ML model prediction result
    Returns:
        Alert dictionary
    """
    try:
        os.makedirs(ALERTS_DIR, exist_ok=True)

        # Include risk_level in alert payload
        alert = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "agent_id": agent_id,
            "is_anomaly": prediction_result["is_anomaly"],
            "risk_level": prediction_result["risk_level"],
            "confidence": round(prediction_result["confidence"], 2),
            "alert_message": prediction_result["alert"],
            "behavior": behavior_data
        }

        # Load existing alerts
        alerts = []
        if os.path.exists(ALERTS_FILE):
            with open(ALERTS_FILE, "r") as f:
                try:
                    alerts = json.load(f)
                except Exception:
                    alerts = []

        # Append and save
        alerts.append(alert)
        with open(ALERTS_FILE, "w") as f:
            json.dump(alerts, f, indent=2)

        # Display result on screen
        if prediction_result["is_anomaly"]:
            print(f"🚨 ALERT | {agent_id} | {prediction_result['risk_level']} | Confidence: {prediction_result['confidence']:.1f}%")
        else:
            print(f"✅ OK    | {agent_id} | {prediction_result['risk_level']} | Confidence: {prediction_result['confidence']:.1f}%")

        return alert

    except Exception as e:
        print(f"❌ Error generating alert: {str(e)}")
        return None

def monitor_agents(agents_behavior):
    """
    Monitor multiple agents and generate real-time alerts.
    Args:
        agents_behavior: List of agent behavior dicts
    """
    try:
        print("\n" + "="*50)
        print("REAL-TIME AGENT MONITORING")
        print("Alert Generation System")
        print("="*50 + "\n")

        alerts_generated = 0
        total_agents = len(agents_behavior)

        for behavior in agents_behavior:
            agent_id = behavior.get("agent_id", "Unknown")
            prediction = predict(behavior)

            if "error" not in prediction:
                alert = generate_alert(agent_id, behavior, prediction)
                if prediction["is_anomaly"]:
                    alerts_generated += 1
            else:
                print(f"❌ Error for {agent_id}: {prediction['error']}")

        print(f"\n{'='*50}")
        print(f"   MONITORING COMPLETE")
        print(f"   Total Agents Monitored: {total_agents}")
        print(f"   Alerts Generated: {alerts_generated}")
        print(f"   Normal Agents: {total_agents - alerts_generated}")
        print(f"   Alerts saved: {ALERTS_FILE}")
        print(f"{'='*50}")

    except Exception as e:
        print(f"❌ Error in monitoring: {str(e)}")

if __name__ == "__main__":
    agents = [
        {
            "agent_id": "AGENT-DR01",
            "requests_per_minute": 5,
            "failed_attempts": 0,
            "data_accessed_mb": 2.0,
            "unique_endpoints": 2,
            "login_time_seconds": 1.5
        },
        {
            "agent_id": "AGENT-AC01",
            "requests_per_minute": 8,
            "failed_attempts": 1,
            "data_accessed_mb": 3.0,
            "unique_endpoints": 3,
            "login_time_seconds": 2.0
        },
        {
            "agent_id": "AGENT-FA01",
            "requests_per_minute": 6,
            "failed_attempts": 0,
            "data_accessed_mb": 1.5,
            "unique_endpoints": 2,
            "login_time_seconds": 1.8
        },
        {
            "agent_id": "AGENT-HACK01",
            "requests_per_minute": 180,
            "failed_attempts": 18,
            "data_accessed_mb": 350.0,
            "unique_endpoints": 45,
            "login_time_seconds": 0.02
        },
        {
            "agent_id": "AGENT-HACK02",
            "requests_per_minute": 120,
            "failed_attempts": 12,
            "data_accessed_mb": 200.0,
            "unique_endpoints": 25,
            "login_time_seconds": 0.05
        }
    ]

    monitor_agents(agents)