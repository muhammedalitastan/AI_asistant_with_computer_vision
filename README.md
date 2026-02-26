# AI Assistant with Computer Vision

An advanced artificial intelligence assistant system capable of understanding voice commands, performing computer vision tasks, and automating various operations through an intuitive graphical interface.

## Overview

This project implements a comprehensive AI assistant that combines natural language processing, computer vision, and automation capabilities. The system can process voice commands in multiple languages, recognize objects and faces through computer vision, and integrate with various applications and social media platforms.

## Features

### Voice Processing
- Multilingual voice command recognition (Turkish and English)
- Text-to-speech synthesis for natural responses
- Real-time audio processing and response generation

### Computer Vision
- YOLOv8-based object detection and classification
- Facial recognition system with trained models
- Real-time camera integration and processing

### User Interface
- PyQt5-based graphical user interface
- User authentication and registration system
- Chat-like interaction interface with history

### Automation & Integration
- Social media platform integration
- Application management and automation
- Task scheduling and reminder system
- Conditional command processing

## Installation

### Prerequisites
- Python 3.8 or higher
- TensorFlow 2.x
- PyQt5
- OpenCV
- YOLOv8
- Additional dependencies listed in requirements.txt

### Setup Instructions

1. Clone the repository:
```bash
git clone https://github.com/muhammedalitastan/AI_asistant_with_computer_vision.git
cd AI_asistant_with_computer_vision
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Verify model files:
The following pre-trained models are included:
- `chat_model.h5` - Natural language processing model
- `yolov8n.pt` - YOLOv8 object detection model
- `face_trained.yml` - Facial recognition data

## Usage

### Running the Application
```bash
python Main.py
```

### Voice Commands
The system responds to various voice commands including:
- "Hello" / "Merhaba" - Greeting and system initialization
- "Open camera" / "Kamerayı aç" - Activate camera module
- "Start object detection" - Begin object recognition mode
- "Face recognition" - Activate facial recognition
- "Social media" - Access social media functions
- "Open application [name]" - Launch specified application
- "Goodbye" / "Görüşürüz" - System shutdown

## Architecture

### Project Structure
```
AI_asistant_with_computer_vision/
├── Main.py                 # Application entry point
├── arayuz_gui.py          # Graphical user interface
├── initilize_engine.py    # Voice processing and TTS engine
├── condition.py           # Conditional logic processing
├── social_media.py        # Social media integration
├── open_close_app.py      # Application management
├── schedule.py            # Task scheduling system
├── wishMe.py              # Greeting and time-based responses
├── model_train.py         # Model training utilities
├── model_test.py          # Model testing framework
├── intents.json           # Command patterns and responses
├── requirements.txt       # Python dependencies
├── chat_model.h5          # Trained NLP model
├── yolov8n.pt            # YOLOv8 detection model
└── face_trained.yml      # Face recognition data
```

### Technology Stack
- **TensorFlow/Keras** - Deep learning and neural networks
- **PyQt5** - Cross-platform GUI framework
- **OpenCV** - Computer vision and image processing
- **YOLOv8** - Real-time object detection
- **TTS (Text-to-Speech)** - Speech synthesis
- **Speech Recognition** - Voice command processing
- **NumPy/Pickle** - Data processing and serialization

## Development

### Contributing
1. Fork the repository
2. Create a feature branch: `git checkout -b feature/new-feature`
3. Commit changes: `git commit -m 'Add new feature'`
4. Push to branch: `git push origin feature/new-feature`
5. Submit a pull request

### Code Standards
- Follow PEP 8 style guidelines
- Include docstrings for all functions and classes
- Add unit tests for new functionality
- Update documentation for API changes

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Author

**Muhammed Ali Tastan**
- GitHub: [muhammedalitastan](https://github.com/muhammedalitastan)
- LinkedIn: [muhammedalitastan](https://linkedin.com/in/muhammedalitastan)

## Acknowledgments

- TensorFlow and Keras development teams
- YOLOv8 contributors and maintainers
- PyQt5 community and developers
- Open source artificial intelligence community

## Support

For questions, bug reports, or contributions:
- Create an issue on GitHub: [Issues](https://github.com/muhammedalitastan/AI_asistant_with_computer_vision/issues)
- Contact via email: [email protected]

## Performance Notes

- System requirements: Minimum 4GB RAM, recommended 8GB+
- GPU acceleration supported for TensorFlow operations
- Model loading may require 30-60 seconds on initial startup
- Real-time processing performance depends on hardware capabilities