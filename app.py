from flask import Flask, jsonify, request
from flask_cors import CORS
import random
import sudoko_validate

app = Flask(__name__)
CORS(app)


def is_valid_sudoku(sudoku):
    return sudoko_validate.check_solution(sudoku)


@app.route("/validate-sudoku", methods=["POST"])
def validate_sudoku():
    data = request.json
    sudoku = data.get("sudoku")
    if sudoku:
        if is_valid_sudoku(sudoku):
            return jsonify({"valid": True}), 200
        else:
            return jsonify({"valid": False}), 200
    else:
        return jsonify({"error": "Dados de Sudoku ausentes"}), 400


if __name__ == "__main__":
    app.run()
