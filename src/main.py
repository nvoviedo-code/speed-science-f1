from fastapi import FastAPI
from routers.fastf1_router import router as api_router

app = FastAPI()

app.include_router(api_router)


@app.get("/")
def read_root():
    return {"message": "Welcome to the Speed Science F1 application!"}
