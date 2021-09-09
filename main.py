# from uvicorn import uvicorn # for ASGI support
from fastapi import FastAPI

# print(uvicorn)
# uvicorn
app = FastAPI()

@app.get("/")
async def root():
	return {"message": "Hello World"}