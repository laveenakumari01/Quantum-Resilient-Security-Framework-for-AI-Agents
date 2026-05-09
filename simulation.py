"""
Main simulation script for AI Agents.
Demonstrates authorized and unauthorized agent access.
"""

import sys
import os
import time

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from agents.data_reader_agent import DataReaderAgent
from agents.api_caller_agent import APICallerAgent
from agents.file_access_agent import FileAccessAgent

def print_separator(title):
    print("\n" + "="*50)
    print(f"   {title}")
    print("="*50)

def run_simulation():
    """Run the main simulation with authorized and unauthorized agents."""

    print_separator("AI AGENT SIMULATION")
    print("Authentication System")

    # ================================
    # AUTHORIZED AGENTS - correct password
    # ================================
    reader = DataReaderAgent("AGENT-DR01", "password123")
    caller = APICallerAgent("AGENT-AC01", "password123")
    file_agent = FileAccessAgent("AGENT-FA01", "password123")

    # ================================
    # UNAUTHORIZED AGENTS - wrong password
    # ================================
    hacker_reader = DataReaderAgent("AGENT-HACK01", "wrongpassword")
    hacker_caller = APICallerAgent("AGENT-HACK02", "wrongpassword")

    # ================================
    # LOGIN ALL AGENTS
    # ================================
    print_separator("Agent Authentication")
    reader.authenticate()
    caller.authenticate()
    file_agent.authenticate()
    hacker_reader.authenticate()
    hacker_caller.authenticate()

    # ================================
    # ROUND 1 - AUTHORIZED AGENTS
    # ================================
    print_separator("Round 1: Authorized Agents")
    reader.read_data()
    time.sleep(1)
    caller.call_api("/agent/task")
    time.sleep(1)
    file_agent.access_file("user_data.csv")
    time.sleep(1)

    # ================================
    # ROUND 2 - UNAUTHORIZED AGENTS
    # ================================
    print_separator("Round 2: Unauthorized Access Attempts")
    hacker_reader.read_data()
    time.sleep(0.5)
    hacker_caller.call_api("/agent/task")
    time.sleep(0.5)

    # ================================
    # ROUND 3 - MIXED
    # ================================
    print_separator("Round 3: Mixed Activity")
    reader.read_data()
    hacker_reader.read_data()
    caller.call_api("/agent/data")
    hacker_caller.call_api("/agent/data")

    # ================================
    # LOGOUT ALL AGENTS
    # ================================
    print_separator("Agent Logout")
    reader.logout()
    caller.logout()
    file_agent.logout()

    print_separator("SIMULATION COMPLETE")
    print("✅ Authorized agents completed their tasks")
    print("🚫 Unauthorized agents were blocked")
    print("📄 Logs saved in: logs/agent_activity.log")
    print("="*50 + "\n")

if __name__ == "__main__":
    run_simulation()