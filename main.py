import cv2
import numpy as np
import os
from datetime import datetime


# Load the image
image = cv2.imread('0.jpeg')

# Print instructions on the CLI
print("Controls:")
print("'e' - Apply erosion")
print("'d' - Apply dilation")
print("'r' - Reset to blurred image")
print("'q' - Save and quit")

def convert_to_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#Create a window to control the Gaussian Blur
cv2.namedWindow('Gaussian Blur')
cv2.namedWindow('Morphological Operations')
cv2.createTrackbar('Kernel Size', 'Gaussian Blur', 5, 25, lambda x: None)
cv2.createTrackbar('Sigma', 'Gaussian Blur', 0, 1000, lambda x: None)
cv2.createTrackbar('Kernel for Erosion Operation', 'Morphological Operations', 5, 25, lambda x: None)
cv2.createTrackbar('Iterations for Erosion Operation', 'Morphological Operations', 1, 10, lambda x: None)
cv2.createTrackbar('Kernel for Dilation Operation', 'Morphological Operations', 5, 25, lambda x: None)
cv2.createTrackbar('Iterations for Dilation Operation', 'Morphological Operations', 1, 10, lambda x: None)

#Image already in grayscale
gray_image = convert_to_grayscale(image)

def apply_gaussian_blur(image):
    
    kernel_size = cv2.getTrackbarPos('Kernel Size', 'Gaussian Blur')
    sigma = cv2.getTrackbarPos('Sigma', 'Gaussian Blur')
    
    # Ensure kernel size is odd and at least 1
    kernel_size = max(1, kernel_size)
    if kernel_size % 2 == 0:
        kernel_size += 1
    
    # Create a tuple for kernel size
    kernel_size = (kernel_size, kernel_size)
    sigma = max(0, sigma)
    
    return cv2.GaussianBlur(image, kernel_size, sigma)


#Morphological Operations
# Type of kernel : Rectangular (can be changed to elliptical or cross shaped)
def apply_erosion(image):
    # Kernel type
    # kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5)) // Using default kernel
    kernel_size = cv2.getTrackbarPos('Kernel for Erosion Operation', 'Morphological Operations')
    iterations = cv2.getTrackbarPos('Iterations for Erosion Operation', 'Morphological Operations')
    
    kernel_size = max(1, kernel_size)
    if kernel_size % 2 == 0:
        kernel_size += 1
    
    kernel = np.ones((kernel_size, kernel_size), np.uint8) # Using custom kernel
    return cv2.erode(image, kernel, iterations=iterations)

def apply_dilation(image):
    # Kernel type
    # kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
    kernel_size = cv2.getTrackbarPos('Kernel for Dilation Operation', 'Morphological Operations')
    iterations = cv2.getTrackbarPos('Iterations for Dilation Operation', 'Morphological Operations')
    
    kernel_size = max(1, kernel_size)
    if kernel_size % 2 == 0:
        kernel_size += 1
    
    kernel = np.ones((kernel_size, kernel_size), np.uint8)
    return cv2.dilate(image, kernel, iterations=iterations)
    


def edge_detection(image):
    edges = cv2.Canny(image, threshold1=50, threshold2=150)
    return edges

def overlay_edges(image, edges):
    edges_colored = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
    return cv2.addWeighted(image, 0.6, edges_colored, 0.4, 0)




while True:
    # Apply Gaussian blur with current trackbar settings
    if 'processed_image' not in locals():
        processed_image = apply_gaussian_blur(gray_image)
    
    # Check for key presses for morphological operations
    key = cv2.waitKey(1) & 0xFF
    if key == ord('e'):  # 'e' for erosion
        processed_image = apply_erosion(processed_image)
    elif key == ord('d'):  # 'd' for dilation
        processed_image = apply_dilation(processed_image)
    elif key == ord('r'):  # 'r' to reset
        processed_image = apply_gaussian_blur(gray_image)
        
    # Step 1: Edge Detection
    edges = edge_detection(processed_image)
    
    # Step 2: Overlaying the detected edges on the original image
    overlay_image = overlay_edges(image, edges)
    # Display results
    cv2.imshow('Processed Image', processed_image)
    cv2.imshow('Overlay Image', overlay_image)
    
    if key == ord('q'):

            
        # Create folders to store the images
        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        result_dir = f'results/results_{timestamp}'
        os.makedirs(result_dir, exist_ok=True)
        
        cv2.imwrite(os.path.join(result_dir, 'processed_image.png'), processed_image)
        cv2.imwrite(os.path.join(result_dir, 'blurred_image.png'), apply_gaussian_blur(gray_image))
        cv2.imwrite(os.path.join(result_dir, 'gray_image.png'), gray_image)
        cv2.imwrite(os.path.join(result_dir, 'original_image.png'), image)
        cv2.imwrite(os.path.join(result_dir, 'overlay_image.png'), overlay_image)
        cv2.imwrite(os.path.join(result_dir, 'edges.png'), edges)

        print("Images saved successfully.")
        # save the values of the trackbars in a text file with timestamp
        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        with open(os.path.join(result_dir, 'trackbar_values.txt'), 'w') as f:
            f.write(f"Kernel Size: {cv2.getTrackbarPos('Kernel Size', 'Gaussian Blur')}\n")
            f.write(f"Sigma: {cv2.getTrackbarPos('Sigma', 'Gaussian Blur')}\n")
            f.write(f"Kernel for Erosion Operation: {cv2.getTrackbarPos('Kernel for Erosion Operation', 'Morphological Operations')}\n")
            f.write(f"Iterations for Erosion Operation: {cv2.getTrackbarPos('Iterations for Erosion Operation', 'Morphological Operations')}\n")
            f.write(f"Kernel for Dilation Operation: {cv2.getTrackbarPos('Kernel for Dilation Operation', 'Morphological Operations')}\n")
            f.write(f"Iterations for Dilation Operation: {cv2.getTrackbarPos('Iterations for Dilation Operation', 'Morphological Operations')}\n")
            break

cv2.destroyAllWindows()



