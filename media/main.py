from fastapi import FastAPI, UploadFile
import crud


app = FastAPI(title="Upload Service")


@app.post("/upload/", status_code=201)
async def upload_photo(file: UploadFile):
    url = crud.upload_image(file)

    return {"image_url": url}
