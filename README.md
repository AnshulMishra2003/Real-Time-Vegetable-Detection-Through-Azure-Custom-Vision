Real-Time-Vegetable-Detection-Through-Azure-Custom-Vision

## Overview

The Vegetable Detection project is a web application that utilizes machine learning to detect and identify different types of vegetables from images. This project leverages Azure's Custom Vision Service for prediction and Azure Blob Storage for storing images. The application is deployed as an Azure Web App.

## Features

- Upload images of vegetables and receive predictions on the type of vegetable.
- View prediction results with confidence scores.
- Simple and intuitive web interface.
- Pre-trained model for quick and accurate predictions.

## Project Structure

- `Vegetable Detection/`
  - `.git/` - Git repository files.
  - `images/`
    - `Test/` - Directory containing test images.
    - `Train/` - Directory containing training images.
  - `models/` - Directory containing machine learning models.
  - `static/css/` - Directory containing CSS files for styling the web pages.
  - `templates/` - Directory containing HTML templates.
    - `index.html` - Home page template.
    - `result.html` - Result page template.
  - `app.py` - Main application script for running the web server.
  - `requirements.txt` - List of Python dependencies.
  - `README.md` - Project overview and instructions (this file).

## Installation

1. Clone the repository:

   git clone https://github.com/yourusername/vegetable-detection.git
   cd vegetable-detection


2. Create and activate a virtual environment:

   python3 -m venv venv
   source venv/bin/activate


3. Install the required dependencies:
   
   pip install -r requirements.txt

## Usage

1. Run the application:

   python app.py

2. Open your web browser and navigate to `object-detection-web-app.azurewebsites.net`.

3. Upload an image of a vegetable to receive a prediction.

## Azure Custom Vision API

This project uses Azure Custom Vision Service for image prediction. Below are the details on how to set up and use the Custom Vision API:

1. **Custom Vision Training API:**
   - Endpoint: `https://<your-custom-vision-endpoint>.cognitiveservices.azure.com/customvision/v3.0/Training`
   - Key: `<your-training-key>`

2. **Custom Vision Prediction API:**
   - Endpoint: `https://<your-custom-vision-endpoint>.cognitiveservices.azure.com/customvision/v3.0/Prediction/<your-project-id>/classify/iterations/<your-iteration-name>/image`
   - Key: `<your-prediction-key>`

3. **Usage:**
   ```python
   import requests

   headers = {
       'Prediction-Key': '<your-prediction-key>',
       'Content-Type': 'application/octet-stream',
   }

   image_path = 'path_to_your_image.jpg'
   with open(image_path, 'rb') as image_file:
       response = requests.post(prediction_endpoint, headers=headers, data=image_file)
   
   predictions = response.json()
   ```

## Azure Blob Storage

Images uploaded to the application are stored in Azure Blob Storage. Below are the details for setting up and using Blob Storage:

1. **Blob Storage Account:**
   - Account Name: `<your-storage-account-name>`
   - Account Key: `<your-storage-account-key>`
   - Container Name: `<your-container-name>`

2. **Usage:**
   python
   from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

   blob_service_client = BlobServiceClient(account_url="<your-blob-url>", credential="<your-storage-account-key>")
   container_client = blob_service_client.get_container_client("<your-container-name>")

   blob_client = container_client.get_blob_client("image_name.jpg")
   with open("path_to_your_image.jpg", "rb") as data:
       blob_client.upload_blob(data)

## Deployment

This application is deployed as an Azure Web App. Follow these steps to deploy your application:

1. Create a new Azure Web App through the Azure Portal.
2. Configure the Web App to pull from your GitHub repository.
3. Set up the necessary environment variables for your Azure services (Custom Vision and Blob Storage) in the Web App settings.
4. Deploy the application through the Azure Portal.

Access the deployed application at: https://object-detection-web-app.azurewebsites.net/


![Screenshot 2024-06-13 125348](https://github.com/AnshulMishra2003/Real-Time-Vegetable-Detection-Through-Azure-Custom-Vision/assets/105056686/b1ccda53-8a85-4291-8adf-5832813cd1e2)

## Output


![image](https://github.com/AnshulMishra2003/Real-Time-Vegetable-Detection-Through-Azure-Custom-Vision/assets/105056686/ad25993b-93a5-4ea0-b476-b0012895ca00)


## Contributing

Contributions are welcome! Please open an issue or submit a pull request if you have any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgements

- This project was inspired by the need for quick and accurate vegetable identification.
- Thanks to the contributors and the open-source community for their support and contributions.

## Screenshot Related To Project

![Screenshot 2024-06-13 124239](https://github.com/AnshulMishra2003/Real-Time-Vegetable-Detection-Through-Azure-Custom-Vision/assets/105056686/4c719af7-ea87-48d5-ba40-5b9f4c8bf80c)


![Screenshot 2024-06-13 124428](https://github.com/AnshulMishra2003/Real-Time-Vegetable-Detection-Through-Azure-Custom-Vision/assets/105056686/26638ac5-2cdc-4c3c-8950-7c44a4fa66e0)


![Screenshot 2024-06-13 124509](https://github.com/AnshulMishra2003/Real-Time-Vegetable-Detection-Through-Azure-Custom-Vision/assets/105056686/ae066f12-69ac-4ea2-a47c-2cd1fc6dc27e)


![Screenshot 2024-06-13 124641](https://github.com/AnshulMishra2003/Real-Time-Vegetable-Detection-Through-Azure-Custom-Vision/assets/105056686/aa63d35a-4111-42c8-a1e3-7b516a751e75)


![Screenshot 2024-06-13 124608](https://github.com/AnshulMishra2003/Real-Time-Vegetable-Detection-Through-Azure-Custom-Vision/assets/105056686/1dacad78-3aae-4b22-85f1-fa5bd86af9c8)


![Screenshot 2024-06-13 124719](https://github.com/AnshulMishra2003/Real-Time-Vegetable-Detection-Through-Azure-Custom-Vision/assets/105056686/33050ec6-8be7-439d-8a9a-141aa24daa69)


![Screenshot 2024-06-13 124719](https://github.com/AnshulMishra2003/Real-Time-Vegetable-Detection-Through-Azure-Custom-Vision/assets/105056686/f5bd1369-3a94-4782-9c09-5bfa7dee4489)


![Screenshot 2024-06-13 124908](https://github.com/AnshulMishra2003/Real-Time-Vegetable-Detection-Through-Azure-Custom-Vision/assets/105056686/b6f6c97b-ef61-4cc1-b6ab-9a83e92cef61)



![Screenshot 2024-06-13 124951](https://github.com/AnshulMishra2003/Real-Time-Vegetable-Detection-Through-Azure-Custom-Vision/assets/105056686/3808a390-5361-43d4-8909-6c55b4b49801)


![Screenshot 2024-06-13 125025](https://github.com/AnshulMishra2003/Real-Time-Vegetable-Detection-Through-Azure-Custom-Vision/assets/105056686/d0df60fc-7d36-41c5-b327-02b248fe21ca)


![Screenshot 2024-06-13 125211](https://github.com/AnshulMishra2003/Real-Time-Vegetable-Detection-Through-Azure-Custom-Vision/assets/105056686/3009324e-e092-4e7f-8e88-f72d5b5301a5)


![Screenshot 2024-06-13 125122](https://github.com/AnshulMishra2003/Real-Time-Vegetable-Detection-Through-Azure-Custom-Vision/assets/105056686/9046ce6e-dedb-4559-8c3e-31d1b645a02a)


