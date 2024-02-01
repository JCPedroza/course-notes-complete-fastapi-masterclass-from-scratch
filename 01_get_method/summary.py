from fastapi import FastAPI

app = FastAPI()


# Use braces {} to declare path parameters in the path.
@app.get("/user/{idn}")
def get_user_idn(idn: int, view: str = "classic"):
    # Declare path parameter as function parameter to access it from the
    # path operation function. The query parameters are declared as function
    # parameters too, but they are not delcared in the path. Optional
    # parameters have default values.
    return {"message": f"User id is {idn}, view is {view}"}
