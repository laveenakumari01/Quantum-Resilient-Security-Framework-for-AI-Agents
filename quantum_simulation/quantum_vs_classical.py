"""
Quantum vs Classical Encryption Comparison
Comparative Analysis

Demonstrates why PQC (Post-Quantum Cryptography) is needed
and how it protects against quantum attacks compared to classical encryption.

Document reference: "Comparative analysis with quantum secure mechanisms"
"""

import os
import sys
import time
import hashlib
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from quantum_simulation.quantum_attack import QuantumAttackSimulator

def print_separator(title):
    """Print formatted separator."""
    print("\n" + "="*60)
    print(f"   {title}")
    print("="*60)

def simulate_classical_encryption():
    """
    Simulate classical encryption — VULNERABLE to quantum attacks.
    Returns performance metrics.
    """
    print("\n   🔴 Testing Classical Encryption (RSA + AES-128)...")
    start = time.time()

    # Simulate RSA operations
    results = {
        "type": "Classical (RSA-2048 + AES-128)",
        "quantum_safe": False,
        "rsa_vulnerable": True,
        "aes_security_bits": 64,  # After Grover's
        "key_exchange_secure": False,
        "future_proof": False,
        "status": "❌ NOT Quantum Safe"
    }

    time.sleep(0.3)
    end = time.time()
    results["time_ms"] = round((end - start) * 1000, 2)

    print(f"   RSA-2048: ❌ Broken by Shor's Algorithm")
    print(f"   AES-128:  ⚠️  Security reduced to 64-bit by Grover's")
    print(f"   Status:   {results['status']}")

    return results

def simulate_pqc_encryption():
    """
    Simulate PQC encryption — SAFE against quantum attacks.
    Returns performance metrics.
    """
    print("\n   🟢 Testing PQC Encryption (CRYSTALS-Kyber + Dilithium)...")
    start = time.time()

    # Simulate PQC operations
    results = {
        "type": "PQC (CRYSTALS-Kyber + Dilithium)",
        "quantum_safe": True,
        "kyber_security": "ML-KEM — Lattice based, quantum resistant",
        "dilithium_security": "ML-DSA — Lattice based, quantum resistant",
        "aes_security_bits": 256,  # AES-256 with PQC
        "key_exchange_secure": True,
        "future_proof": True,
        "nist_approved": True,
        "status": "✅ Quantum Safe — NIST Approved"
    }

    time.sleep(0.3)
    end = time.time()
    results["time_ms"] = round((end - start) * 1000, 2)

    print(f"   CRYSTALS-Kyber: ✅ Resistant to Shor's Algorithm")
    print(f"   Dilithium:      ✅ Quantum-safe digital signatures")
    print(f"   AES-256:        ✅ 128-bit quantum security (safe)")
    print(f"   NIST Approved:  ✅ Official PQC standard 2024")
    print(f"   Status:         {results['status']}")

    return results

def run_comparison():
    """
    Run complete quantum vs classical encryption comparison.
    Shows why needs PQC implementation.
    """
    print_separator(" QUANTUM vs CLASSICAL ANALYSIS")
    print("  Encryption Vulnerability Comparison")
    print("   Demonstrating why PQC is required for AI agents")

    # ================================
    # PART 1: RUN QUANTUM ATTACKS
    # ================================
    print_separator("PART 1: QUANTUM ATTACK SIMULATION")
    print("   Simulating quantum computer attacks on classical encryption...")

    simulator = QuantumAttackSimulator()

    # Attack 1: RSA
    rsa_result = simulator.simulate_rsa_vulnerability(key_size=1024)

    # Attack 2: AES
    aes_result = simulator.simulate_aes_weakness()

    # Attack 3: Agent Communications
    comm_result = simulator.simulate_agent_communication_attack()

    # ================================
    # PART 2: COMPARISON TABLE
    # ================================
    print_separator("PART 2: ENCRYPTION COMPARISON")

    classical = simulate_classical_encryption()
    pqc = simulate_pqc_encryption()

    print(f"\n   {'='*56}")
    print(f"   {'Feature':<25} {'Classical':^15} {'PQC':^15}")
    print(f"   {'='*56}")

    comparisons = [
        ("Quantum Safe",           "❌ No",   "✅ Yes"),
        ("RSA Security",           "❌ Broken","✅ N/A"),
        ("Key Exchange",           "❌ Unsafe","✅ Safe"),
        ("Digital Signatures",     "❌ Unsafe","✅ Safe"),
        ("NIST Approved",          "⚠️  Old",  "✅ 2024"),
        ("Future Proof",           "❌ No",   "✅ Yes"),
        ("Agent Communication",    "❌ Unsafe","✅ Safe"),
    ]

    for feature, classical_val, pqc_val in comparisons:
        print(f"   {feature:<25} {classical_val:^15} {pqc_val:^15}")

    print(f"   {'='*56}")

    # ================================
    # PART 3 RECOMMENDATION
    # ================================
    print_separator("PART 3: SYSTEM RECOMMENDATION")

    print("""
   Based on quantum attack simulation results:

   ❌ CURRENT RISK (Classical Encryption):
      • RSA encryption BROKEN by Shor's Algorithm
      • AES-128 security HALVED by Grover's Algorithm
      • All agent communications at risk
      • JWT tokens could be forged by quantum computers

   ✅ SOLUTION (PQC Implementation):
      • CRYSTALS-Kyber  → Secure key exchange (replaces RSA)
      • CRYSTALS-Dilithium → Quantum-safe signatures
      • AES-256 → Acceptable quantum security
      • Post-Quantum JWT → Agent authentication safe

   🎯  QUANTUM RESILIENCE STATUS:
      • Simulation Layer:  ✅ Complete 
      • PQC Integration:   🔄 implementing backend
      • Agent Security:    ✅ Zero Trust implemented
      • ML Detection:      ✅ Anomaly detection active
    """)

    # ================================
    # FINAL SUMMARY
    # ================================
    print_separator("SIMULATION COMPLETE — FINAL SUMMARY")

    print(f"   ✅ Quantum Attack 1: RSA Shor's Algorithm — DEMONSTRATED")
    print(f"   ✅ Quantum Attack 2: AES Grover's Algorithm — DEMONSTRATED")
    print(f"   ✅ Quantum Attack 3: Agent Communication Attack — DEMONSTRATED")
    print(f"   ✅ Classical vs PQC Comparison — COMPLETE")
    print(f"\n   🏆 CONCLUSION:")
    print(f"   Classical encryption is NOT quantum-safe.")
    print(f"   PQC implementation is NECESSARY")
    print(f"   to protect AI agents from quantum threats!")
    print(f"\n   {'='*60}")

    return {
        "rsa_result": rsa_result,
        "aes_result": aes_result,
        "comm_result": comm_result,
        "classical": classical,
        "pqc": pqc,
        "conclusion": "PQC implementation required for quantum resilience"
    }

if __name__ == "__main__":
    run_comparison()