import cv2
import numpy as np

# Load the image
image = cv2.imread('Foto 1.jpg')

# Define the kernel size for the filter
kernel_size = 5

# Create the kernel
kernel = np.ones((kernel_size, kernel_size), np.float32) / kernel_size**2

# Apply the filter to the image
filtered_image = cv2.filter2D(image, -1, kernel)

# Display the original image and the filtered image
cv2.imshow('Original Image', image)
cv2.imshow('Filtered Image', filtered_image)

# Wait for any key press and then exit
cv2.waitKey(0)
cv2.destroyAllWindows()