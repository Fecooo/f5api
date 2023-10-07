import requests
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/primegaming")
async def primegaming():
    url = 'https://api.jsonbin.io/v3/b/650492c1e4033326cbd84a76?meta=false'
    headers = {
        'Content-Type': 'application/json',
        'X-Master-Key': '$2b$10$gYROSzNjPIm2xEGH57nDVeNvuWgUgShTqeAFrtrotuy8LoGyyGeBK'
    }
    data = requests.get(url=url, headers=headers).json()
    print(data)

    return data