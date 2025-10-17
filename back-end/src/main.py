from fastapi import FastAPI

app = FastAPI()

@app.get(path="/ping")
async def ping():
    return "123"

