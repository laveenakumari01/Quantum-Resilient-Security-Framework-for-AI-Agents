# Quantum Resilient Security Framework for AI Agents
A quantum-resilient security framework built to protect AI agents from modern and future cyber threats. It combines Post-Quantum Cryptography, JWT-based authentication, Zero Trust architecture, and Machine Learning to detect and respond to attacks in real time.

## About the Project
Traditional security systems are not built to handle quantum-era threats. This framework addresses that gap by simulating how AI agents operate in a secure environment where every request is verified, every anomaly is detected, and both classical and quantum attacks are tested.
The system includes autonomous AI agents that authenticate before performing tasks, a FastAPI backend that enforces security policies, a trained ML model that detects suspicious behavior, and a React.js dashboard that displays live activity and threat alerts.

## Key Features

JWT authentication with token expiry and automatic lockout after failed attempts
Zero Trust policy — every agent is verified on every request
Role-Based Access Control (RBAC) for different agent types
Random Forest ML model that detects Brute Force, API Flooding, Data Exfiltration, and Privilege Escalation
Real-time risk-scored alerts (HIGH / MEDIUM / LOW)
Attack simulation using MITRE ATT&CK framework
Quantum attack simulation using Shor's Algorithm (RSA) and Grover's Algorithm (AES)
Post-Quantum Cryptography simulation using CRYSTALS-Kyber and CRYSTALS-Dilithium (NIST 2024)
Live React.js dashboard connected to the backend


## Tech Stack
LayerTechnologyBackendPython, FastAPI, UvicornFrontendReact.js, ViteAuthenticationJWT (python-jose), PassLibMachine LearningScikit-learn, Pandas, NumPySecurityPQC Simulation, Zero Trust, RBAC

## Project Structure
├── agents/                    # AI agent classes (DataReader, APICaller, FileAccess)
├── auth/                      # JWT authentication system
├── anomaly_detection/         # ML model training, alert system, data generation
├── attack_simulation/         # Attack agents and scenarios (MITRE ATT&CK)
├── quantum_simulation/        # Quantum attack and PQC comparison
├── xcipher-frontend/          # React.js frontend (dashboard, login, docs)
├── backend.py                 # Main FastAPI server
├── simulation.py              # Agent simulation runner
├── run_all.py                 # Runs everything together
└── requirements.txt           # Python dependencies