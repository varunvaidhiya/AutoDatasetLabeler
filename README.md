# VLMbasedAutoDatasetLabeler

# Autonomous Vehicle Data Labeling Application

This application processes video footage from autonomous vehicles and labels each frame using AI-powered image analysis.

## Features

- Extracts frames from input video
- Labels each frame using OpenAI's GPT-4 Vision API
- Saves labeled data to a text file

## Requirements

- Python 3.7+
- OpenCV
- OpenAI Python library
- python-dotenv

## Installation

1. Clone this repository
2. Install required packages:
   ```
   pip install opencv-python openai python-dotenv pyyaml
   ```
3. Create a `.env` file in the project root and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

## Usage

1. Update the `config.yaml` file with your desired settings
2. Run the main script:
   ```
   python main.py
   ```

## Configuration

Edit `config.yaml` to customize:
- Input video path
- Output folder for frames
- Output file for labels
- API key environment variable name
- Model settings
- Batch processing size

