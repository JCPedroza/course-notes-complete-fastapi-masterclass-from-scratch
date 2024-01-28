from fastapi import FastAPI

app = FastAPI()


# Decorators are used to route a function to a verb-path.
@app.get("/")
def get_root():
    return {"message": "Hello world!"}
