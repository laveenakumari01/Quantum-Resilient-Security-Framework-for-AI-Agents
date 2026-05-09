"""
Simulated Training Data Generator
Updated with specific attack pattern data
Generates realistic data covering all 4 attack types.
"""

import pandas as pd
import numpy as np
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "anomaly_detection", "training_data.csv")

def generate_training_data():
    """
    Generate training data covering all attack types:
    - Normal behavior
    - Brute Force patterns
    - Data Exfiltration patterns
    - API Flooding patterns
    - Privilege Escalation patterns
    """
    try:
        if os.path.exists(DATA_PATH):
            os.remove(DATA_PATH)
            print("🔄 Old data removed — generating fresh data!")

        os.makedirs(os.path.dirname(DATA_PATH), exist_ok=True)
        np.random.seed(42)

        all_data = []

        # ================================
        # NORMAL BEHAVIOR - 400 records
        # ================================
        for i in range(400):
            all_data.append({
                "requests_per_minute": np.random.randint(1, 10),
                "failed_attempts": np.random.randint(0, 2),
                "data_accessed_mb": np.random.uniform(0.1, 5.0),
                "unique_endpoints": np.random.randint(1, 5),
                "login_time_seconds": np.random.uniform(0.5, 3.0),
                "is_anomaly": 0
            })

        # ================================
        # BRUTE FORCE PATTERNS - 100 records
        # High failed_attempts, fast login
        # ================================
        for i in range(100):
            all_data.append({
                "requests_per_minute": np.random.randint(30, 200),
                "failed_attempts": np.random.randint(8, 20),
                "data_accessed_mb": np.random.uniform(0.1, 2.0),
                "unique_endpoints": np.random.randint(1, 3),
                "login_time_seconds": np.random.uniform(0.01, 0.1),
                "is_anomaly": 1
            })

        # ================================
        # DATA EXFILTRATION PATTERNS - 100 records
        # High data_accessed_mb, many endpoints
        # ================================
        for i in range(100):
            all_data.append({
                "requests_per_minute": np.random.randint(5, 30),
                "failed_attempts": np.random.randint(0, 3),
                "data_accessed_mb": np.random.uniform(100.0, 500.0),
                "unique_endpoints": np.random.randint(4, 15),
                "login_time_seconds": np.random.uniform(0.05, 0.5),
                "is_anomaly": 1
            })

        # ================================
        # API FLOODING PATTERNS - 100 records
        # Very high requests_per_minute
        # ================================
        for i in range(100):
            all_data.append({
                "requests_per_minute": np.random.randint(100, 300),
                "failed_attempts": np.random.randint(5, 30),
                "data_accessed_mb": np.random.uniform(1.0, 10.0),
                "unique_endpoints": np.random.randint(1, 4),
                "login_time_seconds": np.random.uniform(0.01, 0.05),
                "is_anomaly": 1
            })

        # ================================
        # PRIVILEGE ESCALATION PATTERNS - 100 records
        # Many unique_endpoints, moderate failed_attempts
        # ================================
        for i in range(100):
            all_data.append({
                "requests_per_minute": np.random.randint(10, 50),
                "failed_attempts": np.random.randint(4, 12),
                "data_accessed_mb": np.random.uniform(5.0, 30.0),
                "unique_endpoints": np.random.randint(6, 20),
                "login_time_seconds": np.random.uniform(0.05, 0.3),
                "is_anomaly": 1
            })

        # Combine 
        df = pd.DataFrame(all_data)
        df = df.sample(frac=1).reset_index(drop=True)

        df.to_csv(DATA_PATH, index=False)

        normal = len([x for x in all_data if x["is_anomaly"] == 0])
        anomaly = len([x for x in all_data if x["is_anomaly"] == 1])

        print("="*50)
        print("   TRAINING DATA GENERATED")
        print("="*50)
        print(f"✅ Total records: {len(df)}")
        print(f"✅ Normal records: {normal}")
        print(f"✅ Anomaly records: {anomaly}")
        print(f"   - Brute Force patterns: 100")
        print(f"   - Data Exfiltration patterns: 100")
        print(f"   - API Flooding patterns: 100")
        print(f"   - Privilege Escalation patterns: 100")
        print(f"✅ Saved to: {DATA_PATH}")

        return df

    except Exception as e:
        print(f"❌ Error generating data: {str(e)}")
        return None

if __name__ == "__main__":
    generate_training_data()