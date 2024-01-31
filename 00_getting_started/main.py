from fastapi import FastAPI

app = FastAPI()


# Decorators are used to link together operations (http verbs), paths, and
# handlers (path operation functions).
# Operations are methods of the FastAPI instance, and the paths are arguments
# to those methods. The path operation function is the decorated function.
@app.get("/")  # Operation is GET, path is /.
def get_root():  # Path operation function is get_root.
    return {"message": "Hello world!"}  # JSON response
