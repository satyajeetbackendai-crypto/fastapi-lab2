# Calculator API (FastAPI)

A simple calculator REST API built with [FastAPI](https://fastapi.tiangolo.com/).
It provides four endpoints: add, subtract, multiply and divide.

## Project structure

```
fastAPI/
├── main.py      # The whole application
└── README.md    # This file
```

## Setup with a virtual environment

A virtual environment keeps this project's packages separate from the rest of your system.

### 1. Open a terminal in the project folder

```
cd C:\Users\Satyajeet\GenAIFastAPI\FastMCP\fastAPI
```

### 2. Create the virtual environment

```
python -m venv venv
```

This creates a `venv` folder that holds a private copy of Python and its packages.

### 3. Activate it

| Shell                 | Command                        |
|-----------------------|--------------------------------|
| PowerShell (Windows)  | `.\venv\Scripts\Activate.ps1`  |
| Command Prompt (Windows) | `venv\Scripts\activate.bat` |
| Git Bash (Windows)    | `source venv/Scripts/activate` |
| macOS / Linux         | `source venv/bin/activate`     |

Once it is active, your prompt starts with `(venv)`.

> **PowerShell error "running scripts is disabled"?** Run this once, then try again:
> `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`

### 4. Install the dependencies

```
pip install fastapi uvicorn
```

- **fastapi** is the web framework.
- **uvicorn** is the server that runs the app.

### 5. Run the app

```
python main.py
```

Or, to restart automatically whenever you edit the code:

```
uvicorn main:app --reload
```

The API is now running at http://127.0.0.1:8000.

### 6. Try it out

Open the interactive docs at **http://127.0.0.1:8000/docs**. Pick an endpoint, click **Try it out**, enter `a` and `b`, then click **Execute**.

You can also call it from the command line:

```
curl -X POST "http://127.0.0.1:8000/add?a=2&b=3"
```

### 7. Deactivate when you are done

```
deactivate
```

## Endpoints

All endpoints use `POST` and take `a` and `b` as query parameters.

| Endpoint    | Example                       | Response                              |
|-------------|-------------------------------|---------------------------------------|
| `/add`      | `/add?a=2&b=3`                | `{"result": 5.0}`                     |
| `/subtract` | `/subtract?a=5&b=3`           | `{"result": 2.0}`                     |
| `/multiply` | `/multiply?a=4&b=2.5`         | `{"result": 10.0}`                    |
| `/divide`   | `/divide?a=9&b=3`             | `{"result": 3.0}`                     |
| `/divide`   | `/divide?a=1&b=0`             | `400` — `{"detail": "Cannot divide by zero"}` |

If `a` or `b` is not a number (for example `a=abc`), FastAPI returns a `422` validation error.

## How the code works

### Imports and app setup

```python
from fastapi import FastAPI, HTTPException

app = FastAPI(title="Calculator API")
```

- `FastAPI` creates the application. The `title` appears in the `/docs` page.
- `HTTPException` is used to send an error response, such as when dividing by zero.

### Endpoints

```python
@app.post("/add")
def add(a: float, b: float):
    return {"result": a + b}
```

- `@app.post("/add")` registers the function to handle `POST` requests to `/add`.
- `a: float, b: float` are function parameters. FastAPI reads them from the URL query string (`?a=2&b=3`) and converts them to `float`.
  If a value can't be converted, FastAPI automatically rejects the request with a `422` error.
- The returned dictionary is sent back to the client as JSON.

`/subtract` and `/multiply` work the same way.

### Divide and error handling

```python
@app.post("/divide")
def divide(a: float, b: float):
    if b == 0:
        raise HTTPException(status_code=400, detail="Cannot divide by zero")
    return {"result": a / b}
```

- Dividing by zero would crash Python, so the function checks `b` first.
- `raise HTTPException(...)` stops the function and returns a `400 Bad Request` with the error message as JSON.

### Running the server

```python
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
```

- This block only runs when you start the file directly with `python main.py`.
- `uvicorn.run` starts the web server on `127.0.0.1` (your own machine), port `8000`.
