# Part 00 - Getting Started

Routing involves connecting together http verbs, paths, and handlers.

In FastAPI (and OpenAPI), http verbs are called operations, and handlers
are called path operation functions.

Decorators are used to connect an operation, path, and handler together. The
operation is a FastAPI method that takes a path pattern as argument, and
decorates the path operation function.

Remember that in Python decorators are synthatic sugar for higher-order
functions.

The general pettern is:

```text
@<FastAPI instance>.<operation>(<path pattern>)
<path operation function declaration>
```

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def get_root():
    return {"message": "Hello world!"}

```
