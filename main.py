# from uvicorn import uvicorn # for ASGI support
from fastapi import FastAPI
import pandas as pd
import cheap

df = pd.read_csv('1.csv')

# print(uvicorn)
# uvicorn
app = FastAPI()
@app.get("/")
async def root(lat: float = 0.0, lng: float= 0.0, t : int = 1):
	p1 = cheap.CheapRule(lat, df)
	filtered = p1.filter([lat, lng])
	return {"message": "Hello World", "lat": lat, "S": filtered}