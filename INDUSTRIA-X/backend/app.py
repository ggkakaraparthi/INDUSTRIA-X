from flask import Flask, jsonify
from pathlib import Path
import pandas as pd

app = Flask(__name__)

# Project paths
PROJECT_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_DIR = PROJECT_ROOT / "model3_outputs"

BOTTLENECK_FILE = OUTPUT_DIR / "bottleneck_report.csv"
QUEUE_FILE = OUTPUT_DIR / "queue_analysis.csv"


@app.route("/")
def home():
    return jsonify({
        "project": "INDUSTRIA-X",
        "status": "running",
        "message": "Manufacturing Decision Support Backend"
    })


@app.route("/api/health")
def health():
    return jsonify({
        "status": "healthy"
    })


@app.route("/api/summary")
def summary():

    model3_status = "analyzed"

    if not BOTTLENECK_FILE.exists():
        model3_status = "not_analyzed"

    return jsonify({
        "status": "success",
        "data": {
            "model_1": {
                "status": "not_analyzed"
            },
            "model_2": {
                "status": "not_analyzed"
            },
            "model_3": {
                "status": model3_status
            }
        }
    })


@app.route("/api/bottlenecks")
def bottlenecks():

    if not BOTTLENECK_FILE.exists():
        return jsonify({
            "status": "error",
            "message": "Bottleneck report not found"
        }), 404

    df = pd.read_csv(BOTTLENECK_FILE)

    # Convert NaN values to None so JSON serialization works
    records = df.where(pd.notnull(df), None).to_dict(orient="records")

    return jsonify({
        "status": "success",
        "bottlenecks": records
    })


@app.route("/api/recommendations")
def recommendations():

    return jsonify({
        "status": "success",
        "recommendations": [
            {
                "area": "Blanking",
                "action": "Investigate high utilization and queue buildup"
            },
            {
                "area": "Material Handling",
                "action": "Investigate warehouse and forklift queue congestion"
            }
        ]
    })


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )