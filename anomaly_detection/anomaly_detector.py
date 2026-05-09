"""
Anomaly Detection Model
Machine Learning Based Threat Detection
Uses Random Forest Classifier to detect suspicious agent behavior.
Trained on simulated normal and anomalous agent data.
"""

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
from sklearn.preprocessing import StandardScaler
import pickle
import os

# Base directory paths - works from any location
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "anomaly_detection", "training_data.csv")
MODEL_PATH = os.path.join(BASE_DIR, "anomaly_detection", "model", "detector.pkl")
SCALER_PATH = os.path.join(BASE_DIR, "anomaly_detection", "model", "scaler.pkl")
MODEL_DIR = os.path.join(BASE_DIR, "anomaly_detection", "model")

# Features used for detection
FEATURES = [
    "requests_per_minute",
    "failed_attempts",
    "data_accessed_mb",
    "unique_endpoints",
    "login_time_seconds"
]

def load_data():
    """
    Load training data from CSV file.
    Returns:
        DataFrame or None if file not found
    """
    try:
        df = pd.read_csv(DATA_PATH)
        print(f"✅ Training data loaded: {len(df)} records")
        return df
    except FileNotFoundError:
        print("❌ Training data not found! Run generate_data.py first!")
        return None
    except Exception as e:
        print(f"❌ Error loading data: {str(e)}")
        return None

def train_model():
    """
    Train Random Forest model on agent behavior data.
    Saves trained model and scaler to disk.
    Returns:
        Tuple of (model, scaler) or None if training fails
    """
    try:
        df = load_data()
        if df is None:
            return None

        # Separate features and target
        X = df[FEATURES]
        y = df["is_anomaly"]

        # Train/test split - 80% train, 20% test
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )

        # Scale features
        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)

        # Train Random Forest with class_weight to handle imbalance
        print("\n🤖 Model is training...")
        model = RandomForestClassifier(
            n_estimators=100,
            random_state=42,
            max_depth=10,
            class_weight='balanced'  # Handles 5:1 class imbalance
        )
        model.fit(X_train_scaled, y_train)

        # Check accuracy
        y_pred = model.predict(X_test_scaled)
        accuracy = accuracy_score(y_test, y_pred)

        print(f"✅ Model trained successfully!")
        print(f"   Accuracy: {accuracy * 100:.2f}%")
        print(f"\n📊 Classification Report:")
        print(classification_report(
            y_test, y_pred,
            target_names=["Normal", "Anomaly"]
        ))

        # Log feature importance after training
        importances = dict(zip(FEATURES, model.feature_importances_))
        sorted_features = sorted(importances.items(), key=lambda x: x[1], reverse=True)
        print("\n📊 Feature Importance:")
        for feat, imp in sorted_features:
            bar = "█" * int(imp * 50)
            print(f"   {feat:<25} {bar} {imp:.4f}")

        # Save model and scaler
        os.makedirs(MODEL_DIR, exist_ok=True)
        with open(MODEL_PATH, "wb") as f:
            pickle.dump(model, f)
        with open(SCALER_PATH, "wb") as f:
            pickle.dump(scaler, f)

        print(f"\n✅ Model saved: {MODEL_PATH}")
        return model, scaler

    except Exception as e:
        print(f"❌ Error training model: {str(e)}")
        return None

def predict(agent_data):
    """
    Predict if agent behavior is anomalous.
    Args:
        agent_data: dict with agent behavior metrics
    Returns:
        dict with prediction result, risk level and alert message
    """
    try:
        # Load model and scaler from disk
        with open(MODEL_PATH, "rb") as f:
            model = pickle.load(f)
        with open(SCALER_PATH, "rb") as f:
            scaler = pickle.load(f)

        # Prepare input features
        features = pd.DataFrame([{
            "requests_per_minute": agent_data.get("requests_per_minute", 1),
            "failed_attempts": agent_data.get("failed_attempts", 0),
            "data_accessed_mb": agent_data.get("data_accessed_mb", 0.1),
            "unique_endpoints": agent_data.get("unique_endpoints", 1),
            "login_time_seconds": agent_data.get("login_time_seconds", 1.0)
        }])

        # Scale and predict
        features_scaled = scaler.transform(features)
        prediction = model.predict(features_scaled)[0]
        probability = model.predict_proba(features_scaled)[0]

        # Calculate confidence-based risk score
        confidence = float(max(probability) * 100)

        if prediction == 1:
            if confidence >= 90:
                risk_level = "🔴 HIGH RISK"
            elif confidence >= 60:
                risk_level = "🟡 MEDIUM RISK"
            else:
                risk_level = "🟠 LOW RISK"
        else:
            risk_level = "🟢 SAFE"

        return {
            "agent_id": agent_data.get("agent_id", "Unknown"),
            "is_anomaly": bool(prediction),
            "confidence": confidence,
            "risk_level": risk_level,
            "alert": "🚨 ANOMALY DETECTED!" if prediction == 1 else "✅ Normal Behavior"
        }

    except FileNotFoundError:
        return {"error": "❌ Model not found! Run anomaly_detector.py first!"}
    except Exception as e:
        return {"error": f"❌ Prediction error: {str(e)}"}

if __name__ == "__main__":
    print("="*50)
    print("ANOMALY DETECTION MODEL")
    print("ML Training")
    print("="*50)

    result = train_model()

    if result:
        model, scaler = result

        print("\n" + "="*50)
        print("   TESTING PREDICTIONS")
        print("="*50)

        # Normal agent test
        normal_agent = {
            "agent_id": "AGENT-DR01",
            "requests_per_minute": 5,
            "failed_attempts": 0,
            "data_accessed_mb": 2.0,
            "unique_endpoints": 2,
            "login_time_seconds": 1.5
        }

        # Suspicious agent test
        suspicious_agent = {
            "agent_id": "AGENT-HACK01",
            "requests_per_minute": 150,
            "failed_attempts": 15,
            "data_accessed_mb": 250.0,
            "unique_endpoints": 30,
            "login_time_seconds": 0.05
        }

        print("\n--- Normal Agent ---")
        r1 = predict(normal_agent)
        print(f"Agent: {r1['agent_id']}")
        print(f"Result: {r1['alert']}")
        print(f"Risk Level: {r1['risk_level']}")
        print(f"Confidence: {r1['confidence']:.2f}%")

        print("\n--- Suspicious Agent ---")
        r2 = predict(suspicious_agent)
        print(f"Agent: {r2['agent_id']}")
        print(f"Result: {r2['alert']}")
        print(f"Risk Level: {r2['risk_level']}")
        print(f"Confidence: {r2['confidence']:.2f}%")

        print("\n" + "="*50)
        print("   TRAINING COMPLETE!")
        print("="*50)