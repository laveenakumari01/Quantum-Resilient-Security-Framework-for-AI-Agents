"""
Attack Simulation Test Cases
Testing all attack scenarios
Validates that each attack type is properly simulated and detected.
"""

import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from attack_simulation.malicious_agents import (
    BruteForceAgent,
    DataExfiltrationAgent,
    APIFloodingAgent,
    PrivilegeEscalationAgent
)

def test_brute_force():
    """Test brute force attack simulation and ML detection."""
    print("\n--- Testing Brute Force Attack ---")
    try:
        agent = BruteForceAgent("TEST-BF01")
        result = agent.execute_attack("AGENT-DR01", attempts=5)

        assert result is not None, "Result should not be None"
        assert result["attack_type"] == "BRUTE_FORCE"
        assert result["mitre_id"] == "T1110"
        assert result["attempts"] == 5
        assert result["detected"] == True, "Brute force should be detected!"

        print(f"✅ Brute Force test passed!")
        print(f"   Detected: {result['detected']} | Risk: {result['risk_level']}")
    except AssertionError as e:
        print(f"❌ Test failed: {str(e)}")
    except Exception as e:
        print(f"❌ Error: {str(e)}")

def test_data_exfiltration():
    """Test data exfiltration attack simulation and ML detection."""
    print("\n--- Testing Data Exfiltration Attack ---")
    try:
        agent = DataExfiltrationAgent("TEST-DE01")
        result = agent.execute_attack([
            {"name": "test_db", "size_mb": 200},
            {"name": "test_records", "size_mb": 300}
        ])

        assert result is not None, "Result should not be None"
        assert result["attack_type"] == "DATA_EXFILTRATION"
        assert result["mitre_id"] == "T1041"
        assert result["total_data_mb"] == 500
        assert result["detected"] == True, "Data exfiltration should be detected!"

        print(f"✅ Data Exfiltration test passed!")
        print(f"   Detected: {result['detected']} | Risk: {result['risk_level']}")
    except AssertionError as e:
        print(f"❌ Test failed: {str(e)}")
    except Exception as e:
        print(f"❌ Error: {str(e)}")

def test_api_flooding():
    """Test API flooding attack simulation and ML detection."""
    print("\n--- Testing API Flooding Attack ---")
    try:
        agent = APIFloodingAgent("TEST-AF01")
        result = agent.execute_attack("/api/test", requests_count=100)

        assert result is not None, "Result should not be None"
        assert result["attack_type"] == "API_FLOODING"
        assert result["mitre_id"] == "T1499"
        assert result["requests_sent"] == 100
        assert result["detected"] == True, "API flooding should be detected!"

        print(f"✅ API Flooding test passed!")
        print(f"   Detected: {result['detected']} | Risk: {result['risk_level']}")
    except AssertionError as e:
        print(f"❌ Test failed: {str(e)}")
    except Exception as e:
        print(f"❌ Error: {str(e)}")

def test_privilege_escalation():
    """Test privilege escalation attack simulation and ML detection."""
    print("\n--- Testing Privilege Escalation Attack ---")
    try:
        agent = PrivilegeEscalationAgent("TEST-PE01")
        result = agent.execute_attack([
            "/admin/users", "/admin/delete",
            "/admin/secrets", "/root/access",
            "/system/config", "/admin/keys"
        ])

        assert result is not None, "Result should not be None"
        assert result["attack_type"] == "PRIVILEGE_ESCALATION"
        assert result["mitre_id"] == "T1068"
        assert result["detected"] == True, "Privilege escalation should be detected!"

        print(f"✅ Privilege Escalation test passed!")
        print(f"   Detected: {result['detected']} | Risk: {result['risk_level']}")
    except AssertionError as e:
        print(f"❌ Test failed: {str(e)}")
    except Exception as e:
        print(f"❌ Error: {str(e)}")

def run_all_tests():
    """Run all attack simulation test cases."""
    print("\n" + "="*55)
    print("ATTACK SIMULATION TEST CASES")
    print("Validating Attack Detection")
    print("="*55)

    test_brute_force()
    test_data_exfiltration()
    test_api_flooding()
    test_privilege_escalation()

    print("\n" + "="*55)
    print("   ALL ATTACK TESTS COMPLETE!")
    print("="*55)

if __name__ == "__main__":
    run_all_tests()