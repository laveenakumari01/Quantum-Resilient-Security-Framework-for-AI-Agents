"""
Attack Simulation Report Generator
Professional Security Report
Generates a comprehensive JSON report of all attack simulations.
"""

import json
import os
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPORTS_DIR = os.path.join(BASE_DIR, "attack_simulation", "reports")

def cleanup_old_reports(days=30):
    """
    Delete reports older than specified days.
    Real world practice — keep only recent reports.
    Args:
        days: Number of days to keep reports
    """
    try:
        import time
        now = time.time()
        cutoff = now - (days * 86400)  # days to seconds

        if not os.path.exists(REPORTS_DIR):
            return

        deleted = 0
        for filename in os.listdir(REPORTS_DIR):
            filepath = os.path.join(REPORTS_DIR, filename)
            if os.path.isfile(filepath):
                if os.path.getmtime(filepath) < cutoff:
                    os.remove(filepath)
                    deleted += 1

        if deleted > 0:
            print(f"🗑️  Cleaned up {deleted} old reports (older than {days} days)")

    except Exception as e:
        print(f"❌ Cleanup error: {str(e)}")

# Clean up old reports first
cleanup_old_reports(days=30)

def generate_attack_report(results):
    """
    Generate comprehensive attack simulation report.
    Args:
        results: List of attack result dictionaries
    Returns:
        Report dictionary
    """
    try:
        os.makedirs(REPORTS_DIR, exist_ok=True)

        # Filter valid results
        valid_results = [r for r in results if r and "attack_type" in r]

        # Calculate stats
        individual = [r for r in valid_results if r["attack_type"] != "APT"]
        apt = next((r for r in valid_results if r["attack_type"] == "APT"), None)

        total_attacks = len(individual)
        detected = sum(1 for r in individual if r.get("detected"))
        detection_rate = (detected / total_attacks * 100) if total_attacks > 0 else 0

        # Build report
        report = {
            "report_title": "Attack Simulation Report",
            "sprint": "Simulation & System Integration",
            "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "executive_summary": {
                "total_attacks_simulated": total_attacks,
                "attacks_detected": detected,
                "attacks_missed": total_attacks - detected,
                "detection_rate": f"{detection_rate:.1f}%",
                "system_status": "🏆 FULLY SECURE" if detection_rate == 100 else "⚠️ NEEDS IMPROVEMENT"
            },
            "attack_results": [],
            "apt_simulation": None,
            "recommendations": []
        }

        # Add individual results
        for r in individual:
            report["attack_results"].append({
                "attack_type": r["attack_type"],
                "mitre_id": r.get("mitre_id", "N/A"),
                "severity": r.get("severity", "N/A"),
                "agent_id": r["agent_id"],
                "detected": r["detected"],
                "risk_level": r.get("risk_level", "N/A"),
                "confidence": f"{r.get('confidence', 0):.1f}%",
                "timestamp": r.get("timestamp", "N/A")
            })

        # Add APT result
        if apt:
            report["apt_simulation"] = {
                "total_stages": apt["total_stages"],
                "detected_stages": apt["detected_stages"],
                "fully_detected": apt["fully_detected"],
                "status": "✅ ALL STAGES DETECTED" if apt["fully_detected"] else "⚠️ SOME STAGES MISSED"
            }

        # Add recommendations
        if detection_rate == 100:
            report["recommendations"].append("✅ System is performing excellently — maintain current security posture")
        else:
            report["recommendations"].append("⚠️ Review missed attacks and retrain anomaly detection model")
            report["recommendations"].append("⚠️ Consider adding more training data for missed attack types")

        report["recommendations"].append("📌 Connect anomaly model to backend for real-time detection")
        report["recommendations"].append("📌 Schedule regular attack simulations to test system resilience")

        # Save report
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        report_file = os.path.join(REPORTS_DIR, f"attack_report_{timestamp}.json")

        with open(report_file, "w") as f:
            json.dump(report, f, indent=2)

        # Print summary
        print(f"\n📋 ATTACK REPORT GENERATED")
        print(f"   File: {report_file}")
        print(f"   Total Attacks: {total_attacks}")
        print(f"   Detection Rate: {detection_rate:.1f}%")
        print(f"   System Status: {report['executive_summary']['system_status']}")

        return report

    except Exception as e:
        print(f"❌ Error generating report: {str(e)}")
        return None