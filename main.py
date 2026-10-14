from fastapi import FastAPI, HTTPException

app = FastAPI(title="Calculator API")


@app.post("/add")
def add(a: float, b: float):
    return {"result": a + b}


@app.post("/subtract")
def subtract(a: float, b: float):
    return {"result": a - b}


@app.post("/multiply")
def multiply(a: float, b: float):
    return {"result": a * b}


@app.post("/divide")
def divide(a: float, b: float):
    if b == 0:
        raise HTTPException(status_code=400, detail="Cannot divide by zero")
    return {"result": a / b}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
