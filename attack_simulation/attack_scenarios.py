"""
Attack Scenario Modeling
Complete attack scenario simulations
Includes individual scenarios and Advanced Persistent Threat (APT) simulation.
"""

import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

from attack_simulation.malicious_agents import (
    BruteForceAgent,
    DataExfiltrationAgent,
    APIFloodingAgent,
    PrivilegeEscalationAgent
)
from attack_simulation.attack_report import generate_attack_report

def print_separator(title):
    """Print formatted separator."""
    print("\n" + "="*55)
    print(f"   {title}")
    print("="*55)

def run_attack_scenario(scenario_name):
    """
    Run a specific attack scenario.
    Args:
        scenario_name: Name of attack scenario to run
    Returns:
        Attack result dictionary
    """
    try:
        scenarios = {
            "brute_force": _scenario_brute_force,
            "data_exfiltration": _scenario_data_exfiltration,
            "api_flooding": _scenario_api_flooding,
            "privilege_escalation": _scenario_privilege_escalation,
            "apt": _scenario_apt
        }

        if scenario_name not in scenarios:
            print(f"❌ Unknown scenario: {scenario_name}")
            print(f"   Available: {list(scenarios.keys())}")
            return None

        return scenarios[scenario_name]()

    except Exception as e:
        print(f"❌ Error running scenario: {str(e)}")
        return None

def _scenario_brute_force():
    """Scenario 1: Brute Force Attack."""
    print_separator("SCENARIO 1: BRUTE FORCE ATTACK")
    print("   An attacker tries multiple passwords")
    print("   to gain unauthorized access to an agent account.")
    print("   MITRE ATT&CK: T1110")

    agent = BruteForceAgent("ATTACKER-BF01")
    result = agent.execute_attack(
        target_agent_id="AGENT-DR01",
        attempts=10
    )

    if result:
        status = "✅ DETECTED" if result["detected"] else "❌ NOT DETECTED"
        print(f"\n   Result: {status} | Risk: {result['risk_level']}")
    return result

def _scenario_data_exfiltration():
    """Scenario 2: Data Exfiltration Attack."""
    print_separator("SCENARIO 2: DATA EXFILTRATION ATTACK")
    print("   An attacker steals large amounts of sensitive data")
    print("   from multiple database sources.")
    print("   MITRE ATT&CK: T1041")

    agent = DataExfiltrationAgent("ATTACKER-DE01")
    result = agent.execute_attack(
        data_targets=[
            {"name": "user_database", "size_mb": 150},
            {"name": "financial_records", "size_mb": 200},
            {"name": "secret_keys", "size_mb": 100},
            {"name": "admin_data", "size_mb": 180}
        ]
    )

    if result:
        status = "✅ DETECTED" if result["detected"] else "❌ NOT DETECTED"
        print(f"\n   Result: {status} | Risk: {result['risk_level']}")
    return result

def _scenario_api_flooding():
    """Scenario 3: API Flooding / DDoS Attack."""
    print_separator("SCENARIO 3: API FLOODING ATTACK")
    print("   An attacker floods the API with massive requests")
    print("   to cause service disruption.")
    print("   MITRE ATT&CK: T1499")

    agent = APIFloodingAgent("ATTACKER-AF01")
    result = agent.execute_attack(
        target_endpoint="/api/users",
        requests_count=10
    )

    if result:
        status = "✅ DETECTED" if result["detected"] else "❌ NOT DETECTED"
        print(f"\n   Result: {status} | Risk: {result['risk_level']}")
    return result

def _scenario_privilege_escalation():
    """Scenario 4: Privilege Escalation Attack."""
    print_separator("SCENARIO 4: PRIVILEGE ESCALATION ATTACK")
    print("   An attacker attempts to access restricted")
    print("   admin endpoints beyond their authorization.")
    print("   MITRE ATT&CK: T1068")

    agent = PrivilegeEscalationAgent("ATTACKER-PE01")
    result = agent.execute_attack(
        restricted_endpoints=[
            "/admin/users", "/admin/settings",
            "/admin/delete", "/admin/secrets",
            "/admin/keys", "/admin/database",
            "/root/access", "/system/config"
        ]
    )

    if result:
        status = "✅ DETECTED" if result["detected"] else "❌ NOT DETECTED"
        print(f"\n   Result: {status} | Risk: {result['risk_level']}")
    return result

def _scenario_apt():
    """
    Scenario 5: Advanced Persistent Threat (APT) Simulation.
    Combines multiple attacks like real hackers do:
    Step 1: Brute Force to gain access
    Step 2: Privilege Escalation to get admin rights
    Step 3: Data Exfiltration to steal data
    Step 4: API Flooding to cover tracks
    """
    print_separator("SCENARIO 5: ADVANCED PERSISTENT THREAT (APT)")
    print("   Simulates a sophisticated multi-stage attack")
    print("   combining 4 attack types like real hackers!")
    print("   This is the most dangerous attack scenario.")

    results = []
    agent_id = "APT-ATTACKER-01"

    print("\n   📍 Stage 1/4: Gaining Initial Access...")
    bf_agent = BruteForceAgent(agent_id)
    r1 = bf_agent.execute_attack("AGENT-DR01", attempts=8)
    if r1:
        results.append(r1)

    print("\n   📍 Stage 2/4: Escalating Privileges...")
    pe_agent = PrivilegeEscalationAgent(agent_id)
    r2 = pe_agent.execute_attack([
        "/admin/users", "/admin/secrets",
        "/root/access", "/system/config"
    ])
    if r2:
        results.append(r2)

    print("\n   📍 Stage 3/4: Stealing Data...")
    de_agent = DataExfiltrationAgent(agent_id)
    r3 = de_agent.execute_attack([
        {"name": "user_database", "size_mb": 200},
        {"name": "financial_records", "size_mb": 300},
        {"name": "secret_keys", "size_mb": 150}
    ])
    if r3:
        results.append(r3)

    print("\n   📍 Stage 4/4: Covering Tracks (API Flooding)...")
    af_agent = APIFloodingAgent(agent_id)
    r4 = af_agent.execute_attack("/api/logs", requests_count=10)
    if r4:
        results.append(r4)

    # APT Summary
    detected = sum(1 for r in results if r and r["detected"])
    print(f"\n   {'='*45}")
    print(f"   APT ATTACK SUMMARY")
    print(f"   Total Stages: {len(results)}")
    print(f"   Stages Detected: {detected}/{len(results)}")
    if detected == len(results):
        print(f"   🏆 ALL STAGES DETECTED — System fully protected!")
    else:
        print(f"   ⚠️  {len(results)-detected} stages were missed!")
    print(f"   {'='*45}")

    return {
        "attack_type": "APT",
        "stages": results,
        "total_stages": len(results),
        "detected_stages": detected,
        "fully_detected": detected == len(results)
    }

def run_all_scenarios():
    """Run all attack scenarios including APT and generate report."""
    print_separator("ATTACK SCENARIO SIMULATION")
    print("Complete Attack Modeling")
    print("   Testing system resilience against 5 attack scenarios")

    results = []

    # Run 4 individual scenarios
    results.append(run_attack_scenario("brute_force"))
    results.append(run_attack_scenario("data_exfiltration"))
    results.append(run_attack_scenario("api_flooding"))
    results.append(run_attack_scenario("privilege_escalation"))

    # Run APT scenario
    apt_result = run_attack_scenario("apt")

    # Summary
    print_separator("ATTACK SIMULATION SUMMARY")

    attack_names = [
        "Brute Force        (T1110)",
        "Data Exfiltration  (T1041)",
        "API Flooding       (T1499)",
        "Privilege Escalation(T1068)"
    ]

    detected = 0
    total = len([r for r in results if r is not None])

    for i, result in enumerate(results):
        if result:
            status = "✅ DETECTED" if result["detected"] else "❌ MISSED"
            risk = result.get("risk_level", "")
            print(f"   {attack_names[i]:<30} {status} | {risk}")
            if result["detected"]:
                detected += 1

    if apt_result:
        apt_status = "✅ FULLY DETECTED" if apt_result["fully_detected"] else f"⚠️ {apt_result['detected_stages']}/{apt_result['total_stages']} DETECTED"
        print(f"   APT Multi-Stage Attack           {apt_status}")

    detection_rate = (detected / total * 100) if total > 0 else 0

    print(f"\n   Total Individual Attacks: {total}")
    print(f"   Detected:                 {detected}")
    print(f"   Detection Rate:           {detection_rate:.1f}%")

    if detection_rate == 100:
        print(f"\n   🏆 PERFECT DETECTION — System is fully secure!")
    elif detection_rate >= 75:
        print(f"\n   ✅ GOOD DETECTION — System is mostly secure!")
    else:
        print(f"\n   ⚠️  LOW DETECTION — System needs improvement!")

    # Generate report
    print_separator("GENERATING ATTACK REPORT")
    all_results = [r for r in results if r] + ([apt_result] if apt_result else [])
    generate_attack_report(all_results)

    print("="*55)
    return results

if __name__ == "__main__":
    run_all_scenarios()