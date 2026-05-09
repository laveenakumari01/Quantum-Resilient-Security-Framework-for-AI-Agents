"""
FileAccessAgent for NftCipher AI Agents.
Fetches real task data from backend endpoints.
"""

import sys
import os
import requests

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from logger import log_action
from agents.agent_base import BaseAgent

BACKEND_URL = "http://localhost:8000"

class FileAccessAgent(BaseAgent):
    """
    FileAccessAgent fetches real task data from backend.
    """

    def __init__(self, agent_id, password):
        """
        Initialize the agent with ID and password.
        Args:
            agent_id: Unique ID of the agent
            password: Password for authentication
        """
        super().__init__(agent_id, "File Access", password)

    def access_file(self, filename):
        """
        Fetch task data from backend (represents file/resource access).
        Args:
            filename: Name of the file/resource being accessed
        """
        try:
            # Check if agent is authenticated
            if not self.is_authenticated():
                log_action(self.agent_id, f"Attempted to access file: {filename} - DENIED", "UNAUTHORIZED")
                return

            # Real HTTP call to backend
            response = requests.get(
                f"{BACKEND_URL}/agent/task",
                headers={"Authorization": f"Bearer {self.token}"},
                timeout=5
            )

            if response.status_code == 200:
                data = response.json()
                log_action(self.agent_id, f"File access request for {filename} - Backend response: {data}")
            else:
                log_action(self.agent_id, f"File access failed for {filename}: {response.status_code}", "ERROR")

        except requests.exceptions.ConnectionError:
            log_action(self.agent_id, "Backend not running! Start: uvicorn backend:app --reload", "ERROR")
        except Exception as e:
            log_action(self.agent_id, f"Error while accessing file {filename}: {str(e)}", "ERROR")