"""
Base Agent class for AI Agents.
All agents inherit from this class.
"""

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from auth.auth_system import login, verify_token, logout

class BaseAgent:
    """
    BaseAgent is the parent class for all AI agents.
    It handles authentication and token verification.
    """

    def __init__(self, agent_id, role, password):
        """
        Initialize the agent with ID, role and password.
        Args:
            agent_id: Unique ID of the agent
            role: Role of the agent
            password: Password for authentication
        """
        self.agent_id = agent_id
        self.role = role
        self.password = password
        self.token = None

    def authenticate(self):
        """
        Login the agent and get a token.
        Returns:
            True if login successful, False if failed
        """
        try:
            self.token = login(self.agent_id, self.password)
            if self.token:
                return True
            return False
        except Exception as e:
            print(f"❌ Authentication error: {str(e)}")
            return False

    def is_authenticated(self):
        """
        Check if agent has a valid token.
        Returns:
            True if authenticated, False if not
        """
        try:
            return verify_token(self.agent_id, self.token)
        except Exception as e:
            print(f"❌ Token verification error: {str(e)}")
            return False

    def logout(self):
        """Logout the agent."""
        logout(self.agent_id)
        self.token = None

    def get_info(self):
        """Print agent information."""
        auth_status = "Authenticated" if self.is_authenticated() else "Not Authenticated"
        print(f"\n🤖 Agent ID: {self.agent_id}")
        print(f"   Role: {self.role}")
        print(f"   Status: {auth_status}")