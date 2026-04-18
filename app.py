from flask import Flask, render_template, request, jsonify
from config import Endpoints, Templates
from typing import Callable
from formula_map import formulas_map

app: Flask = Flask(__name__)

@app.route(Endpoints.INDEX.value)
def index() -> str:
    return render_template(Templates.INDEX.value)

@app.route(Endpoints.ELECTRICITY.value)
def electricity() -> str:
    return render_template(Templates.ELECTRICITY.value)

@app.route(Endpoints.MECHANIC.value)
def mechanic() -> str:
    return render_template(Templates.MECHANIC.value)

@app.route(Endpoints.THERMODYNAMIC.value)
def thermodynamic() -> str:
    return render_template(Templates.THERMODYNAMIC.value)

@app.route(Endpoints.CALCULATE.value, methods=["POST"])
def calculate_formula():
    incoming_data = request.get_json()

    formula_type: str = incoming_data.get("formula_type")
    data: dict = incoming_data.get("data")

    formula_function: Callable = formulas_map[formula_type]
    result: str = formula_function(**data)

    print(result)

    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(debug=True)