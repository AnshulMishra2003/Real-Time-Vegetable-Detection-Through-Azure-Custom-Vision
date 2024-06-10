from flask import Flask, request, render_template, send_file
import requests
from PIL import Image, ImageDraw, ImageFont
import io
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

app = Flask(__name__)

# Azure Blob Storage configuration
connection_string = "DefaultEndpointsProtocol=https;AccountName=obj0images;AccountKey=2bDeZnUqoUV0pApyvuIuASVBBkRnOsxLqZhMHRo/eVbOCPbqyGSrQVWVvkLaK3oom8ek8uZrktGw+AStIC4KPw==;EndpointSuffix=core.windows.net"
blob_service_client = BlobServiceClient.from_connection_string(connection_string)
container_name = "images"
blob_url = "https://obj0images.blob.core.windows.net/images"

# Endpoint URL for image file prediction
url = "https://object1detection-prediction.cognitiveservices.azure.com/customvision/v3.0/Prediction/eaae3c56-ed98-4210-9ecd-685ec9d8e6ed/detect/iterations/Iteration1/image"
headers = {
    "Prediction-Key": "45c6945ffe904fd5a1147e84c36e1251",
    "Content-Type": "application/octet-stream"
}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return "No file part"
        file = request.files['file']
        if file.filename == '':
            return "No selected file"
        if file:
            image_data = file.read()
            response = requests.post(url, headers=headers, data=image_data)
            response.raise_for_status()
            predictions = response.json()

            img = Image.open(io.BytesIO(image_data))
            draw = ImageDraw.Draw(img)
            img_width, img_height = img.size
            lineWidth = int(img_width / 100)
            object_colors = {
                "tomato": "red",
                "cucumber": "green",
                "pepper": "yellow",
            }

            try:
                font = ImageFont.truetype("arial.ttf", size=int(lineWidth*2))
            except IOError:
                font = ImageFont.load_default()

            for prediction in predictions['predictions']:
                if prediction['probability'] > 0.5:
                    color = object_colors.get(prediction['tagName'], 'white')
                    left = prediction['boundingBox']['left'] * img_width
                    top = prediction['boundingBox']['top'] * img_height
                    width = prediction['boundingBox']['width'] * img_width
                    height = prediction['boundingBox']['height'] * img_height
                    draw.rectangle([left, top, left + width, top + height], outline=color, width=lineWidth)
                    text = f"{prediction['tagName']}: {prediction['probability'] * 100:.2f}%"
                    text_bbox = draw.textbbox((left, top), text, font=font)
                    text_background = [left, top - (text_bbox[3] - text_bbox[1]), text_bbox[2], top]
                    draw.rectangle(text_background, fill=color)
                    draw.text((left, top - (text_bbox[3] - text_bbox[1])), text, fill="black", font=font)

            output = io.BytesIO()
            img.save(output, format='JPEG')
            output.seek(0)

            # Upload the image to Azure Blob Storage
            blob_name = file.filename
            blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
            blob_client.upload_blob(output.getvalue(), overwrite=True)
            
            blob_url_with_name = f"{blob_url}/{blob_name}"

            return render_template('result.html', image_url=blob_url_with_name)
    return render_template('index.html')
    
if __name__ == '__main__':
    app.run(debug=True)
