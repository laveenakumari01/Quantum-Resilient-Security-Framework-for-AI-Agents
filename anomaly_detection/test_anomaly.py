"""
Anomaly Detection Test Cases
Testing ML Model and Alert System
Tests normal and anomalous agent behavior detection.
"""

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from anomaly_detection.anomaly_detector import predict

def test_normal_agent():
    """Test normal agent behavior - should NOT be detected as anomaly."""
    print("\n--- Testing Normal Agent ---")
    try:
        result = predict({
            "agent_id": "AGENT-DR01",
            "requests_per_minute": 5,
            "failed_attempts": 0,
            "data_accessed_mb": 2.0,
            "unique_endpoints": 2,
            "login_time_seconds": 1.5
        })
        assert result["is_anomaly"] == False, "Normal agent should not be anomaly!"
        print(f"✅ Normal agent test passed!")
        print(f"   Result: {result['alert']}")
        print(f"   Confidence: {result['confidence']:.2f}%")
    except AssertionError as e:
        print(f"❌ Test failed: {str(e)}")
    except Exception as e:
        print(f"❌ Error: {str(e)}")

def test_anomalous_agent():
    """Test suspicious agent behavior - should BE detected as anomaly."""
    print("\n--- Testing Anomalous Agent ---")
    try:
        result = predict({
            "agent_id": "AGENT-HACK01",
            "requests_per_minute": 180,
            "failed_attempts": 18,
            "data_accessed_mb": 350.0,
            "unique_endpoints": 45,
            "login_time_seconds": 0.02
        })
        assert result["is_anomaly"] == True, "Suspicious agent should be anomaly!"
        print(f"✅ Anomalous agent test passed!")
        print(f"   Result: {result['alert']}")
        print(f"   Confidence: {result['confidence']:.2f}%")
    except AssertionError as e:
        print(f"❌ Test failed: {str(e)}")
    except Exception as e:
        print(f"❌ Error: {str(e)}")

def test_borderline_agent():
    """Test borderline agent - slightly suspicious behavior."""
    print("\n--- Testing Borderline Agent ---")
    try:
        result = predict({
            "agent_id": "AGENT-BORDER01",
            "requests_per_minute": 25,
            "failed_attempts": 3,
            "data_accessed_mb": 10.0,
            "unique_endpoints": 6,
            "login_time_seconds": 0.3
        })
        print(f"✅ Borderline agent test passed!")
        print(f"   Result: {result['alert']}")
        print(f"   Confidence: {result['confidence']:.2f}%")
    except Exception as e:
        print(f"❌ Error: {str(e)}")

def run_all_tests():
    """Run all anomaly detection test cases."""
    print("\n" + "="*50)
    print("ANOMALY DETECTION TEST CASES")
    print("ML Model Testing")
    print("="*50)

    test_normal_agent()
    test_anomalous_agent()
    test_borderline_agent()

    print("\n" + "="*50)
    print("   ALL TESTS COMPLETE!")
    print("="*50)

if __name__ == "__main__":
    run_all_tests()