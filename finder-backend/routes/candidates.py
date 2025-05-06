from flask import Blueprint, jsonify, request
from services.candidates_service import fetch_candidates

candidates_bp = Blueprint('candidates', __name__, url_prefix='/api/candidates')

@candidates_bp.route('', methods=['GET'])
def get_candidates():
    query = request.args.get('q', '')
    try:
        data = fetch_candidates(query)
        if not any(data.values()):  # Check if all categories are empty
            return jsonify({"message": "ไม่พบข้อมูลที่ตรงกับคำค้นหา"}), 404
        return jsonify(data)  # Return the entire grouped data
    except Exception as err:
        return jsonify({"error": f"เกิดข้อผิดพลาด: {err}"}), 500
