"""
APICallerAgent for AI Agents.
Makes real API calls to backend endpoints.
"""

import sys
import os
import requests

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from logger import log_action
from agents.agent_base import BaseAgent

BACKEND_URL = "http://localhost:8000"

class APICallerAgent(BaseAgent):
    """
    APICallerAgent makes real API calls to backend endpoints.
    """

    def __init__(self, agent_id, password):
        """
        Initialize the agent with ID and password.
        Args:
            agent_id: Unique ID of the agent
            password: Password for authentication
        """
        super().__init__(agent_id, "API Caller", password)

    def call_api(self, endpoint):
        """
        Make a real API call to the backend.
        Args:
            endpoint: The API endpoint to call (e.g. /agent/task)
        """
        try:
            # Check if agent is authenticated
            if not self.is_authenticated():
                log_action(self.agent_id, f"Attempted API call to {endpoint} - BLOCKED", "UNAUTHORIZED")
                return

            # Real HTTP call to backend
            response = requests.get(
                f"{BACKEND_URL}{endpoint}",
                headers={"Authorization": f"Bearer {self.token}"},
                timeout=5
            )

            if response.status_code == 200:
                data = response.json()
                log_action(self.agent_id, f"API call to {endpoint} - Response: {data}")
            else:
                log_action(self.agent_id, f"API call to {endpoint} - Failed: {response.status_code}", "ERROR")

        except requests.exceptions.ConnectionError:
            log_action(self.agent_id, "Backend not running! Start: uvicorn backend:app --reload", "ERROR")
        except Exception as e:
            log_action(self.agent_id, f"Error while calling API {endpoint}: {str(e)}", "ERROR")