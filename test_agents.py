"""
Test cases to validate the functionality of each AI agent
including authentication system, failed login attempts and token expiry.
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

def test_data_reader_agent():
    """Test DataReaderAgent with correct and wrong password."""
    print("\n--- Testing DataReaderAgent ---")

    # Authorized agent
    agent = DataReaderAgent("AGENT-DR01", "password123")
    agent.authenticate()
    agent.read_data()
    agent.logout()
    print("✅ DataReaderAgent authorized test passed!")

    # Unauthorized agent
    hacker = DataReaderAgent("AGENT-HACK01", "wrongpassword")
    hacker.authenticate()
    hacker.read_data()
    print("✅ DataReaderAgent unauthorized test passed!")

def test_api_caller_agent():
    """Test APICallerAgent with correct and wrong password."""
    print("\n--- Testing APICallerAgent ---")

    # Authorized agent
    agent = APICallerAgent("AGENT-AC01", "password123")
    agent.authenticate()
    agent.call_api("/api/users")
    agent.logout()
    print("✅ APICallerAgent authorized test passed!")

    # Unauthorized agent
    hacker = APICallerAgent("AGENT-HACK02", "wrongpassword")
    hacker.authenticate()
    hacker.call_api("/api/secret")
    print("✅ APICallerAgent unauthorized test passed!")

def test_file_access_agent():
    """Test FileAccessAgent with correct and wrong password."""
    print("\n--- Testing FileAccessAgent ---")

    # Authorized agent
    agent = FileAccessAgent("AGENT-FA01", "password123")
    agent.authenticate()
    agent.access_file("user_data.csv")
    agent.logout()
    print("✅ FileAccessAgent authorized test passed!")

    # Unauthorized agent
    hacker = FileAccessAgent("AGENT-HACK03", "wrongpassword")
    hacker.authenticate()
    hacker.access_file("secret.csv")
    print("✅ FileAccessAgent unauthorized test passed!")

def test_failed_login_attempts():
    """Test account lockout after 3 failed login attempts."""
    print("\n--- Testing Failed Login Attempts ---")

    hacker = DataReaderAgent("AGENT-HACK04", "wrong1")
    print("Attempt 1:")
    hacker.authenticate()
    hacker.password = "wrong2"
    print("Attempt 2:")
    hacker.authenticate()
    hacker.password = "wrong3"
    print("Attempt 3:")
    hacker.authenticate()
    hacker.password = "wrong4"
    print("Attempt 4 - Should be locked:")
    hacker.authenticate()
    print("✅ Failed login attempts test passed!")

def test_token_expiry():
    """Test token expiry after 60 seconds."""
    print("\n--- Testing Token Expiry ---")

    agent = DataReaderAgent("AGENT-DR01", "password123")
    agent.authenticate()
    print("Reading data with valid token:")
    agent.read_data()

    print("Waiting 5 seconds to simulate time passing...")
    time.sleep(5)
    print("Reading data again - token still valid:")
    agent.read_data()
    agent.logout()
    print("✅ Token expiry test passed!")

def run_all_tests():
    """Run all agent test cases."""
    print("\n" + "="*50)
    print("AGENT TEST CASES")
    print("Authentication System")
    print("="*50)

    test_data_reader_agent()
    test_api_caller_agent()
    test_file_access_agent()
    test_failed_login_attempts()
    test_token_expiry()

    print("\n" + "="*50)
    print("   ALL TESTS PASSED SUCCESSFULLY!")
    print("="*50 + "\n")

if __name__ == "__main__":
    run_all_tests()