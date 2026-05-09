"""
Advanced Attack Scenario Modeling
Advanced Multi-Vector Attack Simulations

Includes:
1. Quantum + Classical Combined Attack
2. Zero Day Exploit Simulation
3. Supply Chain Attack
4. Insider Threat Simulation

These advanced scenarios demonstrate how real hackers
combine multiple attack types for maximum impact.
"""

import sys
import os
import time
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from logger import log_action
from anomaly_detection.anomaly_detector import predict
from anomaly_detection.alert_system import generate_alert

def print_separator(title):
    """Print formatted separator."""
    print("\n" + "="*60)
    print(f"   {title}")
    print("="*60)

def check_ml_detection(agent_id, behavior):
    """
    Check agent behavior with ML anomaly detection model.
    Args:
        agent_id: Agent ID
        behavior: Behavior metrics dict
    Returns:
        Prediction result
    """
    try:
        prediction = predict(behavior)
        if "error" not in prediction:
            generate_alert(agent_id, behavior, prediction)
            return prediction
        return None
    except Exception as e:
        print(f"❌ ML detection error: {str(e)}")
        return None

# ================================
# ADVANCED SCENARIO 1
# Quantum + Classical Combined
# ================================
def scenario_quantum_classical_combined():
    """
    Advanced Scenario 1: Quantum-Assisted Classical Attack

    Stage 1: Quantum attack breaks RSA encryption
    Stage 2: Broken encryption used to steal agent tokens
    Stage 3: Stolen tokens used for classical data theft

    Why dangerous: Quantum enables attacks that were impossible before!
    MITRE ATT&CK: T1600 + T1110 + T1041
    """
    print_separator("ADVANCED SCENARIO 1: QUANTUM + CLASSICAL COMBINED")
    print("   Most dangerous attack — quantum enables classical!")
    print("   MITRE: T1600 + T1110 + T1041")
    print("   Severity: 🔴 CRITICAL")

    results = []

    # Stage 1: Quantum breaks encryption
    print("\n   📍 Stage 1/3: Quantum Attack — Breaking RSA Encryption...")
    print("   ⚡ Shor's Algorithm initializing quantum superposition...")
    time.sleep(0.5)
    print("   ⚡ Quantum Fourier Transform applied...")
    time.sleep(0.3)
    print("   🚨 RSA encryption BROKEN!")
    print("   🔓 Agent JWT tokens EXPOSED!")

    log_action("ADV-ATTACKER-01",
              "Quantum Shor's Algorithm broke RSA — JWT tokens exposed",
              "UNAUTHORIZED")

    results.append({
        "stage": 1,
        "type": "QUANTUM_RSA_BREAK",
        "success": True,
        "detail": "RSA-2048 broken via Shor's Algorithm simulation"
    })

    # Stage 2: Token theft
    print("\n   📍 Stage 2/3: Stealing Agent Tokens Using Broken Encryption...")
    stolen_tokens = []
    agents = ["AGENT-DR01", "AGENT-AC01", "AGENT-FA01"]

    for agent in agents:
        token = f"STOLEN_JWT_{agent}_QUANTUM_DECRYPTED_2026"
        stolen_tokens.append({"agent": agent, "token": token})
        log_action("ADV-ATTACKER-01",
                  f"JWT token stolen from {agent} via quantum decryption",
                  "UNAUTHORIZED")
        print(f"   🔑 Token stolen: {agent} ✅")
        time.sleep(0.2)

    results.append({
        "stage": 2,
        "type": "TOKEN_THEFT",
        "tokens_stolen": len(stolen_tokens),
        "detail": f"{len(stolen_tokens)} JWT tokens compromised"
    })

    # Stage 3: Classical attack with stolen tokens
    print("\n   📍 Stage 3/3: Classical Data Theft With Stolen Tokens...")

    behavior = {
        "agent_id": "ADV-ATTACKER-01",
        "requests_per_minute": 150,
        "failed_attempts": 0,
        "data_accessed_mb": 350.0,
        "unique_endpoints": 20,
        "login_time_seconds": 0.05
    }

    ml_result = check_ml_detection("ADV-ATTACKER-01", behavior)

    for token in stolen_tokens:
        log_action("ADV-ATTACKER-01",
                  f"Using stolen token — accessing {token['agent']} resources",
                  "UNAUTHORIZED")
        time.sleep(0.1)

    print(f"   🚨 Full system access achieved using {len(stolen_tokens)} stolen tokens!")

    results.append({
        "stage": 3,
        "type": "CLASSICAL_DATA_THEFT",
        "tokens_used": len(stolen_tokens),
        "detail": "Complete system compromise via quantum-assisted attack"
    })

    detected = ml_result["is_anomaly"] if ml_result else False

    print(f"\n   {'='*50}")
    print(f"   SCENARIO 1 SUMMARY")
    print(f"   Stages Completed: 3/3")
    print(f"   Tokens Stolen: {len(stolen_tokens)}")
    print(f"   ML Detection: {'✅ DETECTED' if detected else '⚠️ PARTIAL'}")
    if ml_result:
        print(f"   Risk Level: {ml_result['risk_level']}")
        print(f"   Confidence: {ml_result['confidence']:.1f}%")
    print(f"   {'='*50}")

    return {
        "scenario": "QUANTUM_CLASSICAL_COMBINED",
        "stages": results,
        "ml_detected": detected,
        "severity": "🔴 CRITICAL",
        "mitre": "T1600 + T1110 + T1041",
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

# ================================
# ADVANCED SCENARIO 2
# Zero Day Exploit
# ================================
def scenario_zero_day_exploit():
    """
    Advanced Scenario 2: Zero Day Exploit Simulation

    Phase 1: Reconnaissance — finding vulnerabilities
    Phase 2: Exploit development
    Phase 3: Execute exploit — bypass authentication

    Why dangerous: No patch exists — hardest to defend!
    MITRE ATT&CK: T1203 - Exploitation for Client Execution
    """
    print_separator("ADVANCED SCENARIO 2: ZERO DAY EXPLOIT")
    print("   Exploiting UNKNOWN vulnerability — no patch exists!")
    print("   MITRE: T1203 — Exploitation for Client Execution")
    print("   Severity: 🔴 CRITICAL")
    print("   Detection Difficulty: ⚠️ VERY HARD")

    results = []

    # Phase 1: Reconnaissance
    print("\n   📍 Phase 1/3: Reconnaissance — Finding Vulnerabilities...")
    vulnerabilities = [
        {"component": "Agent Auth Module", "type": "Buffer Overflow", "severity": "Critical"},
        {"component": "API Communication Layer", "type": "SQL Injection", "severity": "High"},
        {"component": "Token Validation System", "type": "Race Condition", "severity": "Critical"},
    ]

    for vuln in vulnerabilities:
        print(f"   🔍 Found: {vuln['component']} — {vuln['type']} ({vuln['severity']})")
        log_action("ZD-ATTACKER-01",
                  f"Zero-day found: {vuln['component']} — {vuln['type']}",
                  "UNAUTHORIZED")
        time.sleep(0.2)

    results.append({
        "phase": "RECONNAISSANCE",
        "vulnerabilities_found": len(vulnerabilities),
        "critical_count": 2
    })

    # Phase 2: Exploit development
    print("\n   📍 Phase 2/3: Crafting Zero-Day Exploit Payload...")
    print("   ⚙️  Building buffer overflow payload...")
    time.sleep(0.3)
    print("   ⚙️  Bypassing input validation...")
    time.sleep(0.3)
    print("   ⚙️  Creating race condition trigger...")
    time.sleep(0.3)
    print("   ✅ Zero-day exploit payload READY!")

    log_action("ZD-ATTACKER-01",
              "Zero-day exploit crafted for agent authentication module",
              "UNAUTHORIZED")

    results.append({
        "phase": "EXPLOIT_DEVELOPMENT",
        "exploit_type": "Buffer Overflow + Race Condition",
        "payload_ready": True
    })

    # Phase 3: Execute
    print("\n   📍 Phase 3/3: Executing Zero-Day Exploit...")

    behavior = {
        "agent_id": "ZD-ATTACKER-01",
        "requests_per_minute": 45,
        "failed_attempts": 8,
        "data_accessed_mb": 25.0,
        "unique_endpoints": 12,
        "login_time_seconds": 0.08
    }

    ml_result = check_ml_detection("ZD-ATTACKER-01", behavior)

    print(f"   💥 Buffer overflow triggered on Auth Module!")
    print(f"   💥 Race condition exploited — token validation bypassed!")
    print(f"   💥 Unauthorized admin access achieved!")

    log_action("ZD-ATTACKER-01",
              "Zero-day executed — authentication bypass successful",
              "UNAUTHORIZED")

    results.append({
        "phase": "EXECUTION",
        "exploit_successful": True,
        "auth_bypassed": True
    })

    detected = ml_result["is_anomaly"] if ml_result else False

    print(f"\n   {'='*50}")
    print(f"   SCENARIO 2 SUMMARY")
    print(f"   Vulnerabilities Found: {len(vulnerabilities)}")
    print(f"   Exploit Success: ✅ YES")
    print(f"   ML Detection: {'✅ DETECTED' if detected else '⚠️ PARTIAL DETECTION'}")
    if ml_result:
        print(f"   Risk Level: {ml_result['risk_level']}")
        print(f"   Confidence: {ml_result['confidence']:.1f}%")
    print(f"   {'='*50}")

    return {
        "scenario": "ZERO_DAY_EXPLOIT",
        "phases": results,
        "ml_detected": detected,
        "severity": "🔴 CRITICAL",
        "mitre": "T1203",
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

# ================================
# ADVANCED SCENARIO 3
# Supply Chain Attack
# ================================
def scenario_supply_chain_attack():
    """
    Advanced Scenario 3: Supply Chain Attack

    Step 1: Compromise a trusted agent
    Step 2: Use trusted agent to attack other agents
    Step 3: Exfiltrate data through trusted channel

    Why dangerous: Trusted agents bypass security checks!
    MITRE ATT&CK: T1195 - Supply Chain Compromise
    """
    print_separator("ADVANCED SCENARIO 3: SUPPLY CHAIN ATTACK")
    print("   Compromising TRUSTED agent to attack the system!")
    print("   MITRE: T1195 — Supply Chain Compromise")
    print("   Severity: 🔴 CRITICAL")
    print("   Why dangerous: Trusted agents bypass Zero Trust checks!")

    results = []
    trusted_agent = "AGENT-DR01"

    # Step 1: Compromise trusted agent
    print(f"\n   📍 Step 1/3: Compromising Trusted Agent ({trusted_agent})...")
    print(f"   🎯 {trusted_agent} has valid credentials — perfect target!")
    print(f"   💉 Injecting malicious payload into {trusted_agent}...")
    time.sleep(0.5)
    print(f"   ✅ {trusted_agent} COMPROMISED — now under attacker control!")

    log_action("SC-ATTACKER-01",
              f"Supply chain: {trusted_agent} successfully compromised",
              "UNAUTHORIZED")

    results.append({
        "step": "COMPROMISE",
        "target": trusted_agent,
        "success": True
    })

    # Step 2: Lateral movement
    print(f"\n   📍 Step 2/3: Lateral Movement via Compromised Agent...")
    targets = ["AGENT-AC01", "AGENT-FA01"]

    for target in targets:
        print(f"   🔄 {trusted_agent} (compromised) → attacking {target}...")
        log_action(trusted_agent,
                  f"SUPPLY CHAIN ATTACK: Compromised agent attacking {target}",
                  "UNAUTHORIZED")
        time.sleep(0.3)
        print(f"   ✅ {target} credentials stolen via trusted channel!")

    results.append({
        "step": "LATERAL_MOVEMENT",
        "agents_attacked": targets,
        "success": True
    })

    # Step 3: Exfiltration
    print(f"\n   📍 Step 3/3: Data Exfiltration Through Trusted Channel...")

    behavior = {
        "agent_id": trusted_agent,
        "requests_per_minute": 35,
        "failed_attempts": 1,
        "data_accessed_mb": 180.0,
        "unique_endpoints": 8,
        "login_time_seconds": 1.2
    }

    ml_result = check_ml_detection(trusted_agent, behavior)

    print(f"   📤 180MB data exfiltrated through trusted {trusted_agent}!")
    print(f"   ⚠️  Looks like normal traffic — hard to detect!")

    log_action(trusted_agent,
              "Supply chain exfiltration: 180MB stolen through trusted channel",
              "UNAUTHORIZED")

    results.append({
        "step": "EXFILTRATION",
        "data_stolen_mb": 180,
        "channel": trusted_agent
    })

    detected = ml_result["is_anomaly"] if ml_result else False

    print(f"\n   {'='*50}")
    print(f"   SCENARIO 3 SUMMARY")
    print(f"   Trusted Agent Compromised: {trusted_agent}")
    print(f"   Agents Attacked: {len(targets)}")
    print(f"   Data Stolen: 180MB")
    print(f"   ML Detection: {'✅ DETECTED' if detected else '⚠️ HARD TO DETECT'}")
    if ml_result:
        print(f"   Risk Level: {ml_result['risk_level']}")
        print(f"   Confidence: {ml_result['confidence']:.1f}%")
    print(f"   {'='*50}")

    return {
        "scenario": "SUPPLY_CHAIN_ATTACK",
        "steps": results,
        "ml_detected": detected,
        "severity": "🔴 CRITICAL",
        "mitre": "T1195",
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

# ================================
# ADVANCED SCENARIO 4
# Insider Threat
# ================================
def scenario_insider_threat():
    """
    Advanced Scenario 4: Insider Threat Simulation

    Legitimate agent slowly steals data over multiple rounds.
    Each round steals small amounts to avoid detection.

    Why dangerous: Authorized agent — looks completely normal!
    MITRE ATT&CK: T1078 - Valid Accounts
    """
    print_separator("ADVANCED SCENARIO 4: INSIDER THREAT SIMULATION")
    print("   Legitimate agent SLOWLY stealing data — hardest to detect!")
    print("   MITRE: T1078 — Valid Accounts")
    print("   Severity: 🟡 HIGH")
    print("   Why dangerous: Agent is authorized — looks completely normal!")

    results = []
    insider_agent = "AGENT-FA01"
    total_stolen = 0
    rounds = 4

    print(f"\n   📍 Simulating slow data theft over {rounds} rounds...")
    print(f"   Agent: {insider_agent} (AUTHORIZED — has valid credentials)")

    for round_num in range(1, rounds + 1):
        mb_stolen = round_num * 3
        total_stolen += mb_stolen

        print(f"\n   🕐 Round {round_num}/{rounds} — Slow exfiltration...")
        print(f"   📤 {mb_stolen}MB stolen this round (total: {total_stolen}MB)")

        behavior = {
            "agent_id": insider_agent,
            "requests_per_minute": 5 + round_num,
            "failed_attempts": 0,
            "data_accessed_mb": float(mb_stolen),
            "unique_endpoints": 2 + round_num,
            "login_time_seconds": 1.5
        }

        ml_result = check_ml_detection(insider_agent, behavior)
        detected_this_round = ml_result["is_anomaly"] if ml_result else False

        log_action(insider_agent,
                  f"Insider threat round {round_num}: {mb_stolen}MB slowly exfiltrated",
                  "UNAUTHORIZED")

        status = "🚨 DETECTED" if detected_this_round else "😴 UNDETECTED"
        risk = ml_result["risk_level"] if ml_result else "N/A"
        print(f"   ML Detection: {status} | Risk: {risk}")

        results.append({
            "round": round_num,
            "mb_stolen": mb_stolen,
            "detected": detected_this_round
        })

        time.sleep(0.3)

    detected_rounds = sum(1 for r in results if r["detected"])
    detection_rate = detected_rounds / rounds * 100

    print(f"\n   {'='*50}")
    print(f"   SCENARIO 4 SUMMARY")
    print(f"   Total Data Stolen: {total_stolen}MB")
    print(f"   Rounds Detected: {detected_rounds}/{rounds}")
    print(f"   Detection Rate: {detection_rate:.0f}%")
    if detected_rounds < rounds:
        print(f"   ⚠️  {rounds - detected_rounds} rounds went UNDETECTED!")
        print(f"   ⚠️  Insider threats evade ML detection when slow!")
        print(f"")
        print(f"   📌 WHY THIS IS INTENTIONAL:")
        print(f"   Single-request ML models cannot detect slow theft.")
        print(f"   Real system uses time-series cumulative analysis.")
        print(f"   This demonstrates a known ML limitation by design.")
        print(f"   PQC + Zero Trust adds extra layer beyond ML alone.")
    else:
        print(f"   ✅ All rounds detected — ML model is effective!")
    print(f"   {'='*50}")

    return {
        "scenario": "INSIDER_THREAT",
        "rounds": results,
        "total_data_stolen_mb": total_stolen,
        "detected_rounds": detected_rounds,
        "detection_rate": f"{detection_rate:.0f}%",
        "severity": "🟡 HIGH",
        "mitre": "T1078",
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

# ================================
# RUN ALL ADVANCED SCENARIOS
# ================================
def run_all_advanced_scenarios():
    """Run all 4 advanced attack scenarios and show summary."""
    print_separator(" ADVANCED ATTACK SCENARIOS")
    print("    Advanced Attack Scenario Modeling")
    print("   4 sophisticated multi-vector attacks simulated")

    results = []

    results.append(scenario_quantum_classical_combined())
    results.append(scenario_zero_day_exploit())
    results.append(scenario_supply_chain_attack())
    results.append(scenario_insider_threat())

    # Final Summary
    print_separator("ADVANCED SCENARIOS FINAL SUMMARY")

    scenario_names = [
        "Quantum+Classical Combined",
        "Zero Day Exploit",
        "Supply Chain Attack",
        "Insider Threat"
    ]

    detected = 0
    for i, result in enumerate(results):
        if result:
            is_detected = result.get("ml_detected",
                         result.get("detected_rounds", 0) > 0)
            status = "✅ DETECTED" if is_detected else "⚠️ PARTIAL"
            severity = result.get("severity", "N/A")
            mitre = result.get("mitre", "N/A")
            print(f"   {scenario_names[i]:<30} {status} | {severity}")
            print(f"   {'':30} MITRE: {mitre}")
            if is_detected:
                detected += 1

    detection_rate = (detected / len(results) * 100) if results else 0

    print(f"\n   Total Advanced Scenarios: {len(results)}")
    print(f"   Detected: {detected}")
    print(f"   Detection Rate: {detection_rate:.0f}%")

    if detection_rate >= 75:
        print(f"\n   🏆 System handles advanced attacks well!")
    else:
        print(f"\n   ⚠️  Some advanced attacks evade detection!")
        print(f"   📌 Recommendation: Implement PQC + enhance ML training!")

    print("="*60)
    return results

if __name__ == "__main__":
    run_all_advanced_scenarios()