
import cv2
import numpy as np

# Read the image
image = cv2.imread(r"C:\Users\akfla\Documents\Programs\python\Python\IMG-20240528-WA0001.jpg")

# Convert the image from BGR to RGB (OpenCV loads images in BGR format)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Modify the RGB values (e.g., increase the red channel by 50)
image_rgb[:, :, 0] = np.clip(image_rgb[:, :, 0]  /(7/5), 0, 255)  # Modify red channel
image_rgb[:, :, 1] = np.clip(image_rgb[:, :, 1], 0, 255)  # Modify green channel
image_rgb[:, :, 2] = np.clip(image_rgb[:, :, 2] /(8/5) , 0, 255) # Modify blue channel

# Convert the modified image back to BGR format for OpenCV display
modified_image_bgr = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2BGR)

# Display the original and modified images using OpenCV

cv2.imshow('Modified Image', modified_image_bgr)

# Wait for a key press and close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()