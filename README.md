# Custom GUI-Based Annotation Tool

## Overview

The Custom GUI-Based Annotation Tool is a desktop application developed for efficient image and video dataset annotation. It combines manual annotation with automatic object tracking to significantly reduce labeling effort.

The tool integrates DeepSORT tracking to automatically propagate bounding boxes across consecutive frames, making dataset preparation faster for computer vision projects.

A comprehensive object detection annotation tool with manual labeling, semi-automatic labeling using ML models, and feedback learning capabilities.


---

## Features

- **Input Support**: Load images and videos for annotation
- **Manual Labeling**: Draw bounding boxes and assign class labels
- **Semi-Automatic Labeling**: ML pipeline with YOLOv5 + DeepSORT + LSTM
- **Editable Predictions**: Edit auto-generated annotations
- **Feedback Learning**: Model learns from user corrections
- **Export Functionality**: Multiple formats (YOLO, PascalVOC, COCO, CSV)

---
### Navigation Features

- **Previous/Next**: Use the navigation toolbar buttons or Left/Right arrow keys
- **Load Directory**: File → Open Directory to load all files from a folder
- **Auto-advance**: Check "Auto-advance after annotation" to automatically move to next file
- **File Counter**: Shows current position (e.g., "File 3 of 15")

---
## Tech Stack

- Python
- PyQt5
- OpenCV
- YOLOv5
- DeepSORT
- NumPy

---

## Project Structure

```
tool_project/
├── main.py                 # Main application entry point
├── gui/                    # GUI components
│   ├── __init__.py
│   ├── main_window.py      # Main application window
│   ├── image_viewer.py     # Image/video viewer widget
│   └── annotation_panel.py # Annotation controls panel
├── core/                   # Core functionality
│   ├── __init__.py
│   ├── annotation.py       # Annotation data structures
│   ├── video_processor.py  # Video processing utilities
│   └── export_manager.py   # Export functionality
├── ml/                     # Machine learning components
│   ├── __init__.py
│   ├── yolo_detector.py    # YOLOv5 integration
│   ├── tracker.py          # DeepSORT tracking
│   └── feedback_learner.py # Feedback learning system
├── utils/                  # Utility functions
│   ├── __init__.py
│   ├── file_utils.py       # File handling utilities
│   └── config.py           # Configuration management
└── models/                 # Pre-trained models storage
```


## Workflow

1. Load image or video
2. Create initial bounding boxes
3. Run DeepSORT tracker
4. Auto-propagate labels
5. Modify incorrect annotations
6. Export labels

---

## Installation

```bash
git clone https://github.com/nagarkar12/Semi--supervised-Annotation-Tool.git

cd Semi--supervised-Annotation-Tool

pip install -r requirements.txt
```

---

## Usage

```bash
python main.py
```

---

## Results

- Reduced manual annotation time by **90%**
- Faster dataset creation
- Improved annotation consistency
- YOLO-ready annotations

---

## Future Improvements

- Segmentation annotation
- Polygon labeling
- SAM integration
- Cloud synchronization
- Multi-user collaboration

---

## Author

Deeksha D. Nagarkar

