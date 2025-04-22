import uvicorn
from fastapi import FastAPI # need python-multipart
from app import views


app = FastAPI(title="AdviNow Interview Challenge", version="1.6")

app.include_router(views.router)


@app.get("/")
def read_root():
    return {"message": "Hello Anjali, FastAPI is working!"}


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8013)
