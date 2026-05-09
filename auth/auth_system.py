"""
Authentication System for NftCipher AI Agents.
Integrated with FastAPI JWT backend running locally.
Includes failed login tracking and account lockout.
"""

import requests

# backend running locally
BACKEND_URL = "http://localhost:8000"

# Track failed login attempts
failed_attempts = {}
MAX_ATTEMPTS = 3

# Store active tokens
active_tokens = {}

def login(agent_id, password):
    """
    Login agent using JWT backend.
    Tracks failed attempts and locks account after 3 tries.
    Args:
        agent_id: The unique ID of the agent
        password: The agent's password
    Returns:
        Token if successful, None if failed
    """
    try:
        # Check if account is locked
        if failed_attempts.get(agent_id, 0) >= MAX_ATTEMPTS:
            print(f"🔒 Agent {agent_id} - Account locked due to too many failed attempts!")
            return None

        response = requests.post(
            f"{BACKEND_URL}/token",
            data={"username": agent_id, "password": password},
            timeout=5
        )

        if response.status_code == 200:
            token = response.json().get("access_token")
            active_tokens[agent_id] = token
            failed_attempts[agent_id] = 0
            print(f"✅ Agent {agent_id} logged in successfully!")
            return token
        else:
            failed_attempts[agent_id] = failed_attempts.get(agent_id, 0) + 1
            remaining = MAX_ATTEMPTS - failed_attempts[agent_id]
            if remaining > 0:
                print(f"🚫 Agent {agent_id} - Wrong password! {remaining} attempts remaining!")
            else:
                print(f"🔒 Agent {agent_id} - Account locked due to too many failed attempts!")
            return None

    except requests.exceptions.ConnectionError:
        print(f"❌ Backend not running! Please start: uvicorn backend:app --reload")
        return None
    except Exception as e:
        print(f"❌ Login error: {str(e)}")
        return None

def verify_token(agent_id, token):
    """
    Verify agent token with backend.
    Args:
        agent_id: The unique ID of the agent
        token: The JWT token to verify
    Returns:
        True if valid, False if invalid or expired
    """
    try:
        if not token:
            return False

        response = requests.get(
            f"{BACKEND_URL}/users/me",
            headers={"Authorization": f"Bearer {token}"},
            timeout=5
        )

        if response.status_code == 200:
            return True
        else:
            print(f"⏰ Agent {agent_id} - Token expired or invalid!")
            return False

    except requests.exceptions.ConnectionError:
        print(f"❌ Backend not running!")
        return False
    except Exception as e:
        print(f"❌ Token verification error: {str(e)}")
        return False

def logout(agent_id):
    """
    Logout an agent by removing their token.
    Args:
        agent_id: The unique ID of the agent
    """
    try:
        if agent_id in active_tokens:
            del active_tokens[agent_id]
        print(f"✅ Agent {agent_id} logged out successfully!")
    except Exception as e:
        print(f"❌ Error during logout: {str(e)}")