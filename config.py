from enum import Enum

class Endpoints(Enum):
    INDEX = "/"
    ELECTRICITY = "/electricity"
    MECHANIC = "/mechanic"
    THERMODYNAMIC = "/thermodynamic"

    CALCULATE = "/calculate"

class Templates(Enum):
    INDEX = "index.html"
    ELECTRICITY = "electricity.html"
    MECHANIC = "mechanic.html"
    THERMODYNAMIC = "thermodynamic.html"