# Backend Development - Image Processing API

## **Project Overview**
This project is a backend API service built using **FastAPI**. It allows users to upload an image, processes the image by rotating it 90 degrees, and provides the ability to download the processed image. The API handles image upload, processing, and retrieval, using **Pillow** for image manipulation.

## **File Structure**

Solution/
│
├── app.py or main.py                # FastAPI application
├── requirements.txt                 # Python dependencies
├── README.md                        # Project documentation
├── images/                          # Uploaded images
├── processed_images/                # Rotated images
└── other_files/                     # Additional files (optional)


## **Requirements**

- Python 3.8 or higher
- FastAPI
- Uvicorn
- Pillow
- python-multipart (for handling form data)

## **Installation**

### **1. Clone the Project**

If you have received the files in a zip, extract them to a directory of your choice. Alternatively, if using a version control system like Git:

```bash
git clone <repository-url>
cd Backend_Development_Project

Set Up a Virtual Environment
It's recommended to use a virtual environment to manage dependencies.


# Create a virtual environment
python -m venv env

# Activate the virtual environment
# On macOS/Linux:
source env/bin/activate

# On Windows:
.\env\Scripts\activate

3. Install Dependencies
Use the requirements.txt file to install all required Python packages:


pip install -r requirements.txt
Running the Application

To start the FastAPI server, run the following command from the project directory:

uvicorn main:app --reload
Once the server is running, you can access the API at http://127.0.0.1:8000.

Testing the API Endpoints

You can test the API endpoints using FastAPI's built-in Swagger UI or other tools like cURL or Postman.

1. Using Swagger UI
FastAPI automatically generates interactive API documentation at http://127.0.0.1:8000/docs.

Upload an Image

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

Error Handling

If an invalid file type is uploaded (i.e., not an image), the API will return a 400 Bad Request error with a message indicating the issue.
If a user attempts to download an image that doesn’t exist, the API will return a 404 Not Found error.
Future Enhancements

Additional Image Processing: Implement options for users to specify the degree of rotation, resizing, or other image transformations.
Authentication: Secure the API with authentication (e.g., OAuth2) to restrict access.
Cloud Integration: Store uploaded and processed images on cloud storage (e.g., AWS S3) for scalability.
Database Integration: Use a database like MongoDB or PostgreSQL to store metadata about uploaded images.
