from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import FileResponse
from PIL import Image
import os
import uuid

app = FastAPI()

# Here are the directories in which the orginal and processed images are saved.
IMAGE_DIR = "images"
PROCESSED_DIR = "processed_images"

# creating the directories if they don't exist
os.makedirs(IMAGE_DIR, exist_ok=True)
os.makedirs(PROCESSED_DIR, exist_ok=True)

@app.post("/upload/")
async def upload_image(file: UploadFile = File(...)):
    # This validates the file type
    if file.content_type.split('/')[0] != 'image':
        raise HTTPException(status_code=400, detail="Invalid image file")
    
    # This generates a unique filename to prevent conflicts
    file_extension = os.path.splitext(file.filename)[1]
    unique_filename = f"{uuid.uuid4()}{file_extension}"
    file_path = os.path.join(IMAGE_DIR, unique_filename)

    # This lines of code saves the uploaded image
    with open(file_path, "wb") as image_file:
        content = await file.read()
        image_file.write(content)

    return {"filename": unique_filename, "message": "Image uploaded successfully"}

@app.get("/download/{filename}")
async def download_image(filename: str):
    original_path = os.path.join(IMAGE_DIR, filename)
    
    # Here, it checks if the original image exists
    if not os.path.isfile(original_path):
        raise HTTPException(status_code=404, detail="Image not found")

    # Here I am defining the processed image path
    processed_filename = f"rotated_{filename}"
    processed_path = os.path.join(PROCESSED_DIR, processed_filename)

    # This creates the processed image, if it doesn't exist.
    if not os.path.isfile(processed_path):
        try:
            with Image.open(original_path) as img:
                rotated_img = img.rotate(90, expand=True)
                rotated_img.save(processed_path)
        except Exception as e:
            raise HTTPException(status_code=500, detail="Error processing image")

    return FileResponse(
        path=processed_path,
        media_type="image/png",
        filename=processed_filename
    )
