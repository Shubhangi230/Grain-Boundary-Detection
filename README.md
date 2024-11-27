# Grain Boundary Detection Project

A computer vision application for detecting and analyzing grain boundaries in geological images using various image processing techniques including graph cut segmentation and morphological operations.

## Project Structure

```
.
├── 0.jpeg                           # Sample input image
├── utils/
│   └── graph_cut_segmentation.py    # Core segmentation algorithms
├── app.py                           # Streamlit web interface
├── main.py                          # Command-line interface
└── requirements.txt                 # Project dependencies
```

## Features

### Image Processing Methods

1. **Morphological Operations with Gaussian Blur**
   - Pre-processes image with Gaussian blur for noise reduction
   - Applies morphological operations (erosion and dilation)
   - Customizable iterations for both operations
   - Best for noisy images requiring smoothing

2. **Morphological Operations without Gaussian Blur**
   - Direct application of morphological operations
   - Preserves more original image details
   - Suitable for clean, high-quality images
   - Maintains sharp edges and fine details

3. **Graph Cut Segmentation with Gaussian Blur**
   - Combines Gaussian blur with Felzenszwalb segmentation
   - Enhanced edge detection and overlay
   - Scale, sigma, and minimum size parameters
   - Optimal for complex grain boundaries

4. **Graph Cut Segmentation without Gaussian Blur**
   - Pure graph-cut based segmentation
   - Maintains original image sharpness
   - Uses Felzenszwalb algorithm
   - Best for high-contrast images

5. **XImgProc Graph Cut**
   - Implements OpenCV's ximgproc segmentation
   - Advanced graph-based segmentation
   - Colored region visualization
   - High-precision boundary detection

## Installation

1. Clone the repository:
```bash
git clone [repository-url]
cd grain-boundary-detection
```

2. Create and activate a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Web Interface (Recommended)

The Streamlit-based web interface offers an intuitive way to process images:

1. Start the web application:
```bash
streamlit run app.py
```

2. Features:
   - Upload images through drag-and-drop or file selection
   - Adjust erosion and dilation iterations with sliders
   - Real-time preview of processing results
   - Side-by-side comparison of different methods
   - Download processed images in PNG format
   - Interactive parameter adjustment

### Command-line Interface

For batch processing or automation, use the command-line interface:

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
- Erosion and dilation kernel sizes
- Number of iterations for morphological operations

## Dependencies

Core requirements:
- OpenCV (cv2) >= 4.8.0
- NumPy >= 1.24.0
- scikit-image >= 0.21.0
- Streamlit >= 1.26.0

## Output

The processed images are:
- Displayed in real-time during processing
- Automatically saved with timestamps
- Available for download through the web interface
- Accompanied by processing parameters in text files

## Online Demo

Try the hosted version at: [Grain-Boundary-Detection](https://grain-boundary-detection.streamlit.app/)

## Technical Details

### Image Processing Parameters

- **Gaussian Blur**:
  - Kernel size: 5x5 (default)
  - Sigma: Adjustable via interface
  
- **Morphological Operations**:
  - Kernel shape: Elliptical
  - Kernel size: 7x7 (default)
  - Iterations: User-configurable (1-10)

- **Graph Cut Segmentation**:
  - Scale: 100
  - Sigma: 0.5
  - Minimum size: 50 pixels


