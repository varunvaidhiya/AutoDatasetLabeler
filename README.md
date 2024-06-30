# Autonomous Vehicle Data Labeling Application

This application processes video footage from autonomous vehicles and labels each frame using AI-powered image analysis.

## Features

- Extracts frames from input video
- Labels each frame using OpenAI's GPT-4 Vision API
- Saves labeled data to a text file
- Provides a simple graphical user interface for ease of use

## Requirements

- Python 3.7+
- OpenCV
- OpenAI Python library
- python-dotenv
- PyYAML
- Tkinter (usually comes pre-installed with Python)

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/autonomous-vehicle-labeling.git
   cd autonomous-vehicle-labeling
   ```

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
2. Run the main script with GUI:
   ```
   python ui.py
   ```
   Or run the main script without GUI:
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

## File Structure

- `main.py`: Core script for frame extraction and labeling
- `ui.py`: Graphical user interface script
- `config.yaml`: Configuration file
- `README.md`: This file
- `.env`: Environment file for storing API key (not included in repository)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
