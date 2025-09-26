import uvicorn
from fastapi import FastAPI
from settings import settings

app = FastAPI()


@app.get('/')
def hello():
    return(f'привет ты попал на мой сайт')





if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.host,
        port=settings.port,
        reload=settings.reload
        )
