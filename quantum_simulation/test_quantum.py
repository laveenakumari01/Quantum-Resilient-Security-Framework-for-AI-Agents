"""
Quantum Simulation Test Cases
Testing quantum attack demonstrations
"""

import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from quantum_simulation.quantum_attack import QuantumAttackSimulator

def test_rsa_vulnerability():
    """Test RSA vulnerability demonstration."""
    print("\n--- Testing RSA Vulnerability ---")
    try:
        simulator = QuantumAttackSimulator()
        result = simulator.simulate_rsa_vulnerability(key_size=1024)

        assert result is not None
        assert result["vulnerable"] == True
        assert result["attack"] == "RSA_SHOR_ALGORITHM"

        print(f"✅ RSA vulnerability test passed!")
        print(f"   Status: {result['status']}")
    except AssertionError as e:
        print(f"❌ Test failed: {str(e)}")
    except Exception as e:
        print(f"❌ Error: {str(e)}")

def test_aes_weakness():
    """Test AES weakness demonstration."""
    print("\n--- Testing AES Weakness ---")
    try:
        simulator = QuantumAttackSimulator()
        result = simulator.simulate_aes_weakness()

        assert result is not None
        assert result["vulnerable"] == True
        assert result["quantum_security_bits"] == 64

        print(f"✅ AES weakness test passed!")
        print(f"   Status: {result['status']}")
    except AssertionError as e:
        print(f"❌ Test failed: {str(e)}")
    except Exception as e:
        print(f"❌ Error: {str(e)}")

def test_agent_communication_attack():
    """Test agent communication attack."""
    print("\n--- Testing Agent Communication Attack ---")
    try:
        simulator = QuantumAttackSimulator()
        result = simulator.simulate_agent_communication_attack()

        assert result is not None
        assert result["agents_targeted"] == 3
        assert result["communications_decrypted"] == 3

        print(f"✅ Agent communication attack test passed!")
        print(f"   Status: {result['status']}")
    except AssertionError as e:
        print(f"❌ Test failed: {str(e)}")
    except Exception as e:
        print(f"❌ Error: {str(e)}")

def run_all_tests():
    """Run all quantum simulation tests."""
    print("\n" + "="*60)
    print("QUANTUM SIMULATION TEST CASES")
    print("Validating Quantum Attack Demos")
    print("="*60)

    test_rsa_vulnerability()
    test_aes_weakness()
    test_agent_communication_attack()

    print("\n" + "="*60)
    print("   ALL QUANTUM TESTS COMPLETE!")
    print("="*60)

if __name__ == "__main__":
    run_all_tests()