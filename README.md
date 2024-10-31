# Backend Development - Image Processing API

## **Project Overview**
This project is a backend API service built using **FastAPI**. It allows users to upload an image, processes the image by rotating it 90 degrees, and provides the ability to download the processed image. The API handles image upload, processing, and retrieval, using **Pillow** for image manipulation.




## **Requirements**

- Python 3.8 or higher
- FastAPI
- Uvicorn
- Pillow
- python-multipart (for handling form data)


Navigate to the POST /upload/ endpoint in the Swagger UI.
Click "Try it out".
Upload an image by selecting a file from your local system.
Click "Execute" to upload the image.
You will receive a JSON response with the unique filename.
Download the Rotated Image

Navigate to the GET /download/{filename} endpoint in the Swagger UI.
Click "Try it out".
Enter the filename from the previous step.
Click "Execute" to download the rotated image.
2. Using cURL
a. Upload an Image

To upload an image using cURL, run the following command:

curl -X POST "http://127.0.0.1:8000/upload/" -F "file=@/path/to/your_image.jpg"
Replace /path/to/your_image.jpg with the path to an image file on your system.
Expected Response:

json
{
  "filename": "unique_filename.jpg",
  "message": "Image uploaded successfully"
}
b. Download the Rotated Image

To download the rotated image, use the following cURL command:

curl -X GET "http://127.0.0.1:8000/download/unique_filename.jpg" --output rotated_image.jpg
Replace unique_filename.jpg with the filename received from the upload response.
The image will be saved as rotated_image.jpg in your current directory.

