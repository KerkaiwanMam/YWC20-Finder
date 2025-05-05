from flask import Flask, jsonify # type: ignore
from flask_cors import CORS # type: ignore
import requests

app = Flask(__name__)
CORS(app)  # เปิดใช้งาน CORS สำหรับ frontend

# ค่าคงที่
INTERVIEW_REF = "PG27"
CANDIDATES_API_URL = "https://api.ywc20.ywc.in.th/homework/candidates"

@app.route('/api/candidates', methods=['GET'])
def get_candidates():
    try:
        response = requests.get(
            CANDIDATES_API_URL,
            headers={"x-reference-id": INTERVIEW_REF}
        )
        response.raise_for_status()
        data = response.json()
        return jsonify(data)
    except requests.HTTPError as http_err:
        return jsonify({"error": f"เกิดข้อผิดพลาด HTTP: {http_err}"}), 500
    except Exception as err:
        return jsonify({"error": f"เกิดข้อผิดพลาดอื่น ๆ: {err}"}), 500

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
