from flask import Flask, jsonify
import prometheus_client
from prometheus_client import Counter, generate_latest

app = Flask(__name__)

# ✅ Fix: Ensure /health endpoint is properly defined
@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok", "message": "FPPR Member is running"}), 200

# ✅ Fix: Ensure /metrics endpoint for Prometheus
request_counter = Counter('http_requests_total', 'Total HTTP Requests')

@app.route("/metrics", methods=["GET"])
def metrics():
    request_counter.inc()
    return generate_latest(), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
