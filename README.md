# Grain Boundary Detection Project

A computer vision application for detecting and analyzing grain boundaries in geological images using various image processing techniques including graph cut segmentation and morphological operations.

## Project Structure

```
.
├── 0.jpeg
├── utils/
│   └── graph_cut_segmentation.py    # Core segmentation algorithms
├── app.py                           # Streamlit web interface
├── main.py                          # Command-line interface
└── requirements.txt                 # Project dependencies
```

## Features

- Multiple image processing approaches:
  - Graph cut segmentation with Gaussian blur
  - Graph cut segmentation without Gaussian blur
  - Morphological operations with Gaussian blur
  - Morphological operations without Gaussian blur
- Interactive controls for:
  - Erosion iterations
  - Dilation iterations
  - Gaussian blur parameters
- Two interfaces:
  - Web interface (Streamlit)
  - Command-line interface with trackbars

## Installation

1. Clone the repository
2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Dependencies

- OpenCV (cv2) >= 4.8.0
- NumPy >= 1.24.0
- scikit-image >= 0.21.0
- Streamlit >= 1.26.0

## Usage

### Web Interface

Run the Streamlit app:
```bash
streamlit run app.py
```

Features:
- Upload images through the web interface
- Adjust erosion and dilation iterations
- View multiple processing results side by side
- Download processed images

### Command-line Interface

Run the command-line version:
```bash
python main.py
```

Controls:
- 'e' - Apply erosion
- 'd' - Apply dilation
- 'r' - Reset to blurred image
- 'q' - Save and quit

Trackbar controls for:
- Gaussian blur kernel size and sigma
- Erosion and dilation kernel sizes and iterations

## Hosting
The hosted version of the app is available at [Grain-Boundary-Detection](https://grain-boundary-detection.streamlit.app/)



## Image Processing Methods

### 1. Morphological Operations with Gaussian Blur
- Applies Gaussian blur for noise reduction
- Uses morphological operations (erosion and dilation) with customizable iterations
- Suitable for initial noise reduction and feature enhancement

### 2. Morphological Operations without Gaussian Blur
- Direct application of morphological operations
- Preserves more original image details
- Useful when blur-based smoothing is not desired

### 3. Graph Cut Segmentation with Gaussian Blur
- Combines Gaussian blur with Felzenszwalb segmentation
- Enhanced edge detection and overlay
- Best for clear grain boundary detection

### 4. Graph Cut Segmentation without Gaussian Blur
- Pure graph-cut based segmentation
- Maintains original image sharpness
- Suitable for high-quality input images

## Output

The processed images can be:
- Viewed in real-time
- Saved automatically with timestamps
- Downloaded through the web interface
- Saved with processing parameters in a separate text file

