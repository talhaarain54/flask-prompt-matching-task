from flask import Blueprint, request, jsonify
from services.prompt_service import match_prompt

prompt_blueprint = Blueprint('prompt_blueprint', __name__)

@prompt_blueprint.route('/match', methods=['POST'])
def match_view():
    try:
        data = request.get_json()

        # Check if all required fields are present
        required_fields = ['situation', 'level', 'file_type', 'data']
        if not all(field in data for field in required_fields):
            return jsonify({"error": "Missing Data"}), 400

        situation = data.get('situation')
        level = data.get('level')
        file_type = data.get('file_type')

        # Call service layer to find the matching prompt
        result = match_prompt(situation, level, file_type)

        if result:
            return jsonify({"prompt": result}), 200
        else:
            return jsonify({"error": "Invalid Prompt"}), 400

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "Something went wrong", "details": str(e)}), 500
