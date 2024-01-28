from fastapi import FastAPI
from enum import Enum

app = FastAPI()


# Operation is GET, path is /.
@app.get("/")  # This line is the path operation decorator.
def get_root():  # This is the path operation function.
    return {"message": "welcome to root!"}


# Order of declaration matters. Only the first function that matches the path
# will be called. If get_api_static is declared after get_api_id, the former
# will never be called since the latter will match the path pattern first.
@app.get("/api/static")
def get_api_static():
    return {"message": "path is static: /api/static"}


# Path parameters are declared using {} and are arguments to the handler.
# Type annotations provide automatic type validation.
@app.get("/api/{id}")
def get_api_id(id: int):
    return {"message": f"path is dynamic: /api/{id}"}


# You can declare predefined path values by extending Enum and the type of
# the values.
class ValidColor(str, Enum):
    red = "red"
    green = "green"
    blue = "blue"
    white = "white"
    black = "black"


# Using your enum as type annotation enables automatic type validation.
@app.get("/color/{valid_color}")
def get_color_valid(valid_color: ValidColor):
    if valid_color is ValidColor.red:
        return {"valid_color": valid_color, "message": "roses are red"}

    if valid_color.value == ValidColor.green:
        return {"valid_color": valid_color, "message": "grass is green"}

    return {"valid_color": valid_color, "message": "color is valid"}
