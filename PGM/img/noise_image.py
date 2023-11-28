import sys
import cv2
import numpy as np

# arguments are input image, output image, noise level

# Load the original image
image = cv2.imread(sys.argv[1])

# Generate Gaussian noise
mean = 128
stddev = 500  # You can adjust the standard deviation to control the amount of noise
gaussian_noise = np.random.normal(mean, stddev, image.shape).astype('uint8')

# Add Gaussian noise to the image
#noisy_image = cv2.add(image, gaussian_noise)
noisy_image = cv2.addWeighted(image, 1 - 0.01*float(sys.argv[3]), gaussian_noise, 0.01*float(sys.argv[3]), 0)


# Save the noisy image
cv2.imwrite(sys.argv[2], noisy_image)