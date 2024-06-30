import cv2
import os
import openai
import yaml
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def load_config():
    with open('config.yaml', 'r') as f:
        return yaml.safe_load(f)

config = load_config()

# Set up OpenAI API key
openai.api_key = os.getenv(config['labeling']['api_key_env_var'])

def extract_frames(video_path, output_folder):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Open the video file
    video = cv2.VideoCapture(video_path)
    
    frame_count = 0
    while True:
        # Read a frame from the video
        success, frame = video.read()
        if not success:
            break
        
        # Save the frame as an image file
        frame_path = os.path.join(output_folder, f"frame_{frame_count:04d}.jpg")
        cv2.imwrite(frame_path, frame)
        frame_count += 1

    video.release()
    return frame_count

def label_frame(frame_path):
    # Read the image file
    with open(frame_path, "rb") as image_file:
        image_data = image_file.read()
    
    # Call OpenAI API to analyze the image
    response = openai.ChatCompletion.create(
        model=config['model']['name'],
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": config['model']['prompt']},
                    {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{image_data.encode('base64')}"}}
                ],
            }
        ],
    )
    
    return response.choices[0].message.content

def main():
    video_path = config['video']['input_path']
    output_folder = config['video']['output_folder']
    labeled_data_file = config['labeling']['output_file']

    # Extract frames from the video
    frame_count = extract_frames(video_path, output_folder)
    print(f"Extracted {frame_count} frames from the video.")

    # Label each frame
    with open(labeled_data_file, "w") as outfile:
        for i in range(frame_count):
            frame_path = os.path.join(output_folder, f"frame_{i:04d}.jpg")
            label = label_frame(frame_path)
            outfile.write(f"Frame {i}:\n{label}\n\n")
            print(f"Labeled frame {i}")

    print(f"Labeling complete. Results saved to {labeled_data_file}")

if __name__ == "__main__":
    main()
