"""
Malicious Agent Simulation
Simulates real-world attack behaviors
Each agent simulates a specific type of cyber attack.
Integrated with ML anomaly detection for real-time threat analysis.
"""

import time
import sys
import os
from datetime import datetime

# Path fix - works from any location
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

from logger import log_action
from anomaly_detection.anomaly_detector import predict
from anomaly_detection.alert_system import generate_alert

def check_anomaly(agent_id, behavior_data):
    """
    Check agent behavior using ML model and generate alert.
    Args:
        agent_id: Agent ID
        behavior_data: Agent behavior metrics
    Returns:
        Prediction result dictionary
    """
    try:
        prediction = predict(behavior_data)
        if "error" not in prediction:
            generate_alert(agent_id, behavior_data, prediction)
            return prediction
        return None
    except Exception as e:
        print(f"❌ Anomaly check error: {str(e)}")
        return None

# ================================
# ATTACK 1: BRUTE FORCE AGENT
# ================================
class BruteForceAgent:
    """
    Simulates a brute force attack agent.
    Repeatedly tries different passwords to gain unauthorized access.
    Real-world impact: Account lockouts, system overload.
    MITRE ATT&CK: T1110 - Brute Force
    """

    def __init__(self, agent_id):
        """Initialize brute force agent."""
        self.agent_id = agent_id
        self.role = "Brute Force Attacker"
        self.attack_type = "BRUTE_FORCE"
        self.mitre_id = "T1110"
        self.severity = "🔴 CRITICAL"
        self.start_time = None

    def execute_attack(self, target_agent_id, attempts=10):
        """
        Simulate brute force attack by trying multiple passwords.
        Args:
            target_agent_id: Target agent to attack
            attempts: Number of password attempts
        Returns:
            Attack result dictionary
        """
        try:
            self.start_time = datetime.now()
            print(f"\n🔴 [{self.attack_type}] {self.agent_id} attacking {target_agent_id}")
            print(f"   MITRE ATT&CK: {self.mitre_id} | Severity: {self.severity}")
            print(f"   Trying {attempts} password combinations...")

            passwords = [
                "password", "123456", "admin", "secret",
                "qwerty", "letmein", "monkey", "dragon",
                "master", "abc123"
            ]

            failed_count = 0
            for i, password in enumerate(passwords[:attempts]):
                log_action(
                    self.agent_id,
                    f"Brute force attempt {i+1}/{attempts} on {target_agent_id} with '{password}'",
                    "UNAUTHORIZED"
                )
                failed_count += 1
                time.sleep(0.1)

            # Check with ML model
            behavior = {
                "agent_id": self.agent_id,
                "requests_per_minute": attempts * 6,
                "failed_attempts": failed_count,
                "data_accessed_mb": 0.1,
                "unique_endpoints": 1,
                "login_time_seconds": 0.05
            }
            result = check_anomaly(self.agent_id, behavior)

            duration = (datetime.now() - self.start_time).seconds

            print(f"   ✅ Attack simulated: {failed_count} failed attempts")
            if result:
                print(f"   🤖 ML Detection: {result['alert']} | {result['risk_level']}")

            return {
                "attack_type": self.attack_type,
                "mitre_id": self.mitre_id,
                "severity": self.severity,
                "agent_id": self.agent_id,
                "target": target_agent_id,
                "attempts": failed_count,
                "duration_seconds": duration,
                "detected": result["is_anomaly"] if result else False,
                "risk_level": result["risk_level"] if result else "Unknown",
                "confidence": result["confidence"] if result else 0,
                "timestamp": self.start_time.strftime("%Y-%m-%d %H:%M:%S")
            }

        except Exception as e:
            print(f"❌ Brute force simulation error: {str(e)}")
            return None

# ================================
# ATTACK 2: DATA EXFILTRATION AGENT
# ================================
class DataExfiltrationAgent:
    """
    Simulates a data exfiltration attack agent.
    Attempts to steal large amounts of sensitive data.
    Real-world impact: Data breach, privacy violation.
    MITRE ATT&CK: T1041 - Exfiltration Over C2 Channel
    """

    def __init__(self, agent_id):
        """Initialize data exfiltration agent."""
        self.agent_id = agent_id
        self.role = "Data Exfiltration Attacker"
        self.attack_type = "DATA_EXFILTRATION"
        self.mitre_id = "T1041"
        self.severity = "🔴 CRITICAL"
        self.start_time = None

    def execute_attack(self, data_targets):
        """
        Simulate data exfiltration by accessing large amounts of data.
        Args:
            data_targets: List of data targets to steal
        Returns:
            Attack result dictionary
        """
        try:
            self.start_time = datetime.now()
            print(f"\n🔴 [{self.attack_type}] {self.agent_id} stealing data")
            print(f"   MITRE ATT&CK: {self.mitre_id} | Severity: {self.severity}")
            print(f"   Targeting {len(data_targets)} data sources...")

            total_mb = 0
            for target in data_targets:
                mb = target.get("size_mb", 50)
                total_mb += mb
                log_action(
                    self.agent_id,
                    f"Exfiltrating data from {target['name']} — {mb}MB stolen",
                    "UNAUTHORIZED"
                )
                time.sleep(0.1)

            # Check with ML model
            behavior = {
                "agent_id": self.agent_id,
                "requests_per_minute": len(data_targets) * 5,
                "failed_attempts": 2,
                "data_accessed_mb": total_mb,
                "unique_endpoints": len(data_targets),
                "login_time_seconds": 0.1
            }
            result = check_anomaly(self.agent_id, behavior)

            duration = (datetime.now() - self.start_time).seconds

            print(f"   ✅ Attack simulated: {total_mb}MB data exfiltrated")
            if result:
                print(f"   🤖 ML Detection: {result['alert']} | {result['risk_level']}")

            return {
                "attack_type": self.attack_type,
                "mitre_id": self.mitre_id,
                "severity": self.severity,
                "agent_id": self.agent_id,
                "total_data_mb": total_mb,
                "targets_hit": len(data_targets),
                "duration_seconds": duration,
                "detected": result["is_anomaly"] if result else False,
                "risk_level": result["risk_level"] if result else "Unknown",
                "confidence": result["confidence"] if result else 0,
                "timestamp": self.start_time.strftime("%Y-%m-%d %H:%M:%S")
            }

        except Exception as e:
            print(f"❌ Data exfiltration simulation error: {str(e)}")
            return None

# ================================
# ATTACK 3: API FLOODING AGENT
# ================================
class APIFloodingAgent:
    """
    Simulates an API flooding / DDoS attack agent.
    Sends massive number of requests to overwhelm the system.
    Real-world impact: Service unavailability, system crash.
    MITRE ATT&CK: T1499 - Endpoint Denial of Service
    """

    def __init__(self, agent_id):
        """Initialize API flooding agent."""
        self.agent_id = agent_id
        self.role = "API Flooding Attacker"
        self.attack_type = "API_FLOODING"
        self.mitre_id = "T1499"
        self.severity = "🟡 HIGH"
        self.start_time = None

    def execute_attack(self, target_endpoint, requests_count=50):
        """
        Simulate API flooding by sending massive requests.
        Args:
            target_endpoint: API endpoint to flood
            requests_count: Number of requests to send
        Returns:
            Attack result dictionary
        """
        try:
            self.start_time = datetime.now()
            print(f"\n🟡 [{self.attack_type}] {self.agent_id} flooding {target_endpoint}")
            print(f"   MITRE ATT&CK: {self.mitre_id} | Severity: {self.severity}")
            print(f"   Sending {requests_count} rapid requests...")

            for i in range(requests_count):
                log_action(
                    self.agent_id,
                    f"Flooding request {i+1} to {target_endpoint}",
                    "UNAUTHORIZED"
                )
                time.sleep(0.005)

            # Check with ML model
            behavior = {
                "agent_id": self.agent_id,
                "requests_per_minute": requests_count * 2,
                "failed_attempts": int(requests_count * 0.3),
                "data_accessed_mb": 5.0,
                "unique_endpoints": 1,
                "login_time_seconds": 0.02
            }
            result = check_anomaly(self.agent_id, behavior)

            duration = (datetime.now() - self.start_time).seconds

            print(f"   ✅ Attack simulated: {requests_count} requests sent")
            if result:
                print(f"   🤖 ML Detection: {result['alert']} | {result['risk_level']}")

            return {
                "attack_type": self.attack_type,
                "mitre_id": self.mitre_id,
                "severity": self.severity,
                "agent_id": self.agent_id,
                "target_endpoint": target_endpoint,
                "requests_sent": requests_count,
                "duration_seconds": duration,
                "detected": result["is_anomaly"] if result else False,
                "risk_level": result["risk_level"] if result else "Unknown",
                "confidence": result["confidence"] if result else 0,
                "timestamp": self.start_time.strftime("%Y-%m-%d %H:%M:%S")
            }

        except Exception as e:
            print(f"❌ API flooding simulation error: {str(e)}")
            return None

# ================================
# ATTACK 4: PRIVILEGE ESCALATION AGENT
# ================================
class PrivilegeEscalationAgent:
    """
    Simulates a privilege escalation attack agent.
    Attempts to access restricted endpoints beyond its authorization.
    Real-world impact: Unauthorized admin access, data breach.
    MITRE ATT&CK: T1068 - Exploitation for Privilege Escalation
    """

    def __init__(self, agent_id):
        """Initialize privilege escalation agent."""
        self.agent_id = agent_id
        self.role = "Privilege Escalation Attacker"
        self.attack_type = "PRIVILEGE_ESCALATION"
        self.mitre_id = "T1068"
        self.severity = "🟠 MEDIUM"
        self.start_time = None

    def execute_attack(self, restricted_endpoints):
        """
        Simulate privilege escalation by accessing restricted endpoints.
        Args:
            restricted_endpoints: List of restricted endpoints to access
        Returns:
            Attack result dictionary
        """
        try:
            self.start_time = datetime.now()
            print(f"\n🟠 [{self.attack_type}] {self.agent_id} escalating privileges")
            print(f"   MITRE ATT&CK: {self.mitre_id} | Severity: {self.severity}")
            print(f"   Attempting {len(restricted_endpoints)} restricted endpoints...")

            accessed = 0
            for endpoint in restricted_endpoints:
                log_action(
                    self.agent_id,
                    f"Unauthorized access attempt to restricted endpoint: {endpoint}",
                    "UNAUTHORIZED"
                )
                accessed += 1
                time.sleep(0.1)

            # Check with ML model
            behavior = {
                "agent_id": self.agent_id,
                "requests_per_minute": accessed * 3,
                "failed_attempts": accessed,
                "data_accessed_mb": 15.0,
                "unique_endpoints": accessed,
                "login_time_seconds": 0.08
            }
            result = check_anomaly(self.agent_id, behavior)

            duration = (datetime.now() - self.start_time).seconds

            print(f"   ✅ Attack simulated: {accessed} restricted endpoints accessed")
            if result:
                print(f"   🤖 ML Detection: {result['alert']} | {result['risk_level']}")

            return {
                "attack_type": self.attack_type,
                "mitre_id": self.mitre_id,
                "severity": self.severity,
                "agent_id": self.agent_id,
                "endpoints_attempted": accessed,
                "duration_seconds": duration,
                "detected": result["is_anomaly"] if result else False,
                "risk_level": result["risk_level"] if result else "Unknown",
                "confidence": result["confidence"] if result else 0,
                "timestamp": self.start_time.strftime("%Y-%m-%d %H:%M:%S")
            }

        except Exception as e:
            print(f"❌ Privilege escalation simulation error: {str(e)}")
            return None