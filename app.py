from flask import Flask, request, send_file, jsonify
import torch
from diffusers import StableVideoDiffusionPipeline
from diffusers.utils import export_to_video
from PIL import Image
import io

app = Flask(__name__)

# Initialize the Stable Video Diffusion Pipeline
pipeline = StableVideoDiffusionPipeline.from_pretrained(
    "stabilityai/stable-video-diffusion-img2vid-xt", 
    torch_dtype=torch.float16, 
    variant="fp16"
)
pipeline.enable_model_cpu_offload()

@app.route('/generate', methods=['POST'])
def generate_video():
    # Check if image is included in the request
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400
    
    # Load the uploaded image
    file = request.files['image']
    image = Image.open(file.stream).convert("RGB")
    image = image.resize((1024, 576))

    # Generate video frames
    generator = torch.manual_seed(42)
    frames = pipeline(image, decode_chunk_size=8, generator=generator).frames[0]

    # Save to video and send back
    video_path = "generated.mp4"
    export_to_video(frames, video_path, fps=7)
    return send_file(video_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
