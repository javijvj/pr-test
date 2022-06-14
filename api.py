from fastapi import FastAPI
from calc import Calc

app = FastAPI()
calc = Calc


@app.get("/")
async def root():
    return {"status": "running..."}

@app.get("/myname")
async def root():
    return {"name": "Francisco Vasquez"}

@app.get("/sumar")
async def root(num1: int = 0, num2: int = 0):
    return {"result": calc.sumar(num1, num2)}

@app.get("/restar")
async def root(num1: int = 0, num2: int = 0):
    return {"name": calc.restar(num1, num2)}