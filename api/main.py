from fastapi import FastAPI
from memes.memes import router as memes_router

app = FastAPI(title="Memes")
app.include_router(memes_router)


@app.get("/test/")
def test():
    return {"msg": "Hello World"}
