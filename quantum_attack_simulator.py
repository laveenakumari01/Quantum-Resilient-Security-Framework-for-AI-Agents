import asyncio
import aiohttp
import time
import random

BASE_URL = "http://127.0.0.1:8000"
NUM_REQUESTS = 2000
CONCURRENCY = 150

PAYLOADS = [
    "Normal system login event by user admin",
    "System reboot initiated by user",
    "User requested password reset for account",
    "Failed login attempt from unknown IP address",
    "Potential SQL injection detected: SELECT * FROM users WHERE id = '1' OR '1'='1'",
    "Massive brute force attack originating from multiple IPs",
    "Unauthorized access attempt blocked by firewall",
    "Malware signature match found in memory dump",
    "Quantum entanglement key exchange protocol initiated", # Quantum themed
    "Quantum encryption bypass attempt detected", # Quantum themed
] * 200

async def login(session):
    data = {
        "grant_type": "password",
        "username": "john.doe",
        "password": "secret",
        "scope": "",
        "client_id": "",
        "client_secret": ""
    }
    async with session.post(f"{BASE_URL}/token", data=data) as response:
        if response.status == 200:
            res = await response.json()
            return res.get("access_token")
        else:
            print("Login failed")
            return None

async def attack_worker(name, session, token, queue, results):
    headers = {"Authorization": f"Bearer {token}"}
    while True:
        try:
            payload = queue.get_nowait()
        except asyncio.QueueEmpty:
            break
        
        start_time = time.time()
        try:
            async with session.post(
                f"{BASE_URL}/analyze", 
                json={"event": payload}, 
                headers=headers
            ) as response:
                await response.read() # Consume response
                latency = time.time() - start_time
                results.append((response.status, latency))
        except Exception as e:
            results.append((500, time.time() - start_time))
        queue.task_done()

async def main():
    print(f"Starting Quantum Attack Simulation...")
    print(f"Target: {BASE_URL}")
    print(f"Total Requests: {NUM_REQUESTS}")
    print(f"Concurrency Level: {CONCURRENCY}")
    
    async with aiohttp.ClientSession() as session:
        token = await login(session)
        if not token:
            print("Failed to obtain auth token. Exiting.")
            return

        queue = asyncio.Queue()
        # Pre-fill queue
        for i in range(NUM_REQUESTS):
            queue.put_nowait(random.choice(PAYLOADS))
            
        results = []
        start_time = time.time()
        
        # Start workers
        tasks = []
        for i in range(CONCURRENCY):
            task = asyncio.create_task(attack_worker(f"Worker-{i}", session, token, queue, results))
            tasks.append(task)
            
        await asyncio.gather(*tasks)
        
        total_time = time.time() - start_time
        
        successes = sum(1 for r in results if r[0] == 200)
        failures = len(results) - successes
        latencies = [r[1] for r in results]
        avg_latency = sum(latencies) / len(latencies) if latencies else 0
        max_latency = max(latencies) if latencies else 0
        rps = NUM_REQUESTS / total_time if total_time > 0 else 0
        
        print("\n--- Simulation Results ---")
        print(f"Total Time: {total_time:.2f} seconds")
        print(f"Requests Per Second (RPS): {rps:.2f}")
        print(f"Average Latency: {avg_latency*1000:.2f} ms")
        print(f"Max Latency: {max_latency*1000:.2f} ms")
        print(f"Successful Requests: {successes}")
        print(f"Failed Requests: {failures}")
        print("--------------------------")

if __name__ == "__main__":
    asyncio.run(main())
