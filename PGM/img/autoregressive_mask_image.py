import sys
import cv2
import numpy as np

# parameters: input image, output image, %image to be masked, block_size for masking
# Load the original image
image = cv2.imread(sys.argv[1])

# Create a mask with the same dimensions as the original image
mask = np.ones_like(image)

# Draw a filled rectangle on the mask
block_size = int(sys.argv[4])
print("image size = " + str(image.shape[0]) + " x " + str(image.shape[1]))
print("block size = " + str(block_size))
print("unmasked blocks = " + str(0.01 * float(sys.argv[3])))
c = 0
for x in range(0, image.shape[0], block_size):
    for y in range(0, image.shape[1], block_size):
        if c >= int(sys.argv[3]):
            image[x:x+block_size,y:y+block_size,:] = 0
        c += 1

# Apply the mask to the original image using bitwise AND operation
cv2.imwrite(sys.argv[2], image)