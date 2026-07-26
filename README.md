# Custom GUI-Based Annotation Tool

## Overview

The Custom GUI-Based Annotation Tool is a desktop application developed for efficient image and video dataset annotation. It combines manual annotation with automatic object tracking to significantly reduce labeling effort.

The tool integrates DeepSORT tracking to automatically propagate bounding boxes across consecutive frames, making dataset preparation faster for computer vision projects.

---

## Features

- Desktop GUI built with PyQt5
- Image annotation
- Video annotation
- Automatic object tracking
- DeepSORT integration
- YOLO-compatible annotation format
- Bounding box editing
- Label management
- Export annotations
- Keyboard shortcuts

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
Semi-supervised-Annotation-Tool/
│
├── gui/
├── tracker/
├── annotation/
├── utils/
├── screenshots/
├── main.py
├── requirements.txt
└── README.md
```

---

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

## Author

Deeksha D. Nagarkar
