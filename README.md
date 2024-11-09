# hugging-face-stable-video-diffusion
# Image-to-Video Generator
This project uses Stable Video Diffusion to generate videos from uploaded images. The backend is built with Flask and leverages Hugging Face’s diffusers library to transform images into video frames. Users can upload an image via a simple web interface and download the generated video.

# Features
Image Upload: Users can upload any image file.
Video Generation: Transforms the uploaded image into a video using the Stable Video Diffusion model.
Downloadable Output: The generated video can be downloaded in MP4 format.
Prerequisites
Python 3.8+
Pip (Python package installer)
Installation
Clone the Repository:

bash
Copy code
git clone https://github.com/your-username/image-to-video-generator.git
cd image-to-video-generator
Install Dependencies:

bash
Copy code
pip install flask torch diffusers pillow
Set up Hugging Face Diffusers Model:

The project uses the StableVideoDiffusionPipeline from Hugging Face’s diffusers library. The model is loaded within the Flask app and requires internet access to download initially.