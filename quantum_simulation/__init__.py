"""
Quantum Attack Simulation Package
Quantum vs Classical Encryption Analysis
Demonstrates vulnerability of classical encryption against quantum attacks.
"""

from .quantum_attack import QuantumAttackSimulator
from .quantum_vs_classical import run_comparison

__all__ = ["QuantumAttackSimulator", "run_comparison"]