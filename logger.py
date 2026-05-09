import logging
import os

os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename="logs/agent_activity.log",
    level=logging.INFO,
    format="%(asctime)s | %(message)s"
)

def log_action(agent_id, action, status="SUCCESS"):
    message = f"Agent: {agent_id} | Status: {status} | {action}"
    logging.info(message)
    
    if status == "SUCCESS":
        print(f"✅ {message}")
    elif status == "UNAUTHORIZED":
        print(f"🚫 {message}")
    else:
        print(f"❌ {message}")