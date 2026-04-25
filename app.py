from flask import Flask, render_template, request, jsonify
from config import Endpoints, Templates
from typing import Callable
from FormulasRegistry.physical_quantity_registry import physical_quantity_map

app: Flask = Flask(__name__)

@app.route(Endpoints.INDEX.value)
def index() -> str:
    return render_template(Templates.INDEX.value)

@app.route(Endpoints.ELECTRICITY.value)
def electricity() -> str:
    return render_template(Templates.ELECTRICITY.value)

@app.route(Endpoints.MECHANICS.value)
def mechanics() -> str:
    return render_template(Templates.MECHANICS.value)

@app.route(Endpoints.THERMODYNAMICS.value)
def thermodynamics() -> str:
    return render_template(Templates.THERMODYNAMICS.value)

@app.route(Endpoints.CALCULATE.value, methods=["POST"])
def calculate_formula():
    incoming_data = request.get_json()

    calculable_physical_quantity: str = incoming_data.get("calculable_physical_quantity")
    physical_quantity_data: dict = incoming_data.get("physical_quantity_data")

    formula_function: Callable = physical_quantity_map[calculable_physical_quantity]
    result: str = formula_function(**physical_quantity_data)

    print(result)

    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(debug=True)