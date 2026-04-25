from enum import Enum

class Endpoints(Enum):
    INDEX = "/"
    ELECTRICITY = "/electricity"
    MECHANICS = "/mechanics"
    THERMODYNAMICS = "/thermodynamics"

    CALCULATE = "/calculate"

class Templates(Enum):
    INDEX = "index.html"
    ELECTRICITY = "Physics/electricity.html"
    MECHANICS = "Physics/mechanics.html"
    THERMODYNAMICS = "Physics/thermodynamics.html"