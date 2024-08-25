import cv2 #converting to CIE lab
import matplotlib.pyplot as plt #displaying image
import numpy as np #gauss
from scipy.stats import norm #gauss

def display_images(filtered_image_bgr):
    # Display the original and recursively filtered images
    # cv2.imshow('Original Image', image)
    # cv2.imshow('Recursively Filtered Image', filtered_image_bgr)
    cv2.imwrite('cartoonfilter_result.jpg', filtered_image_bgr) # von Ede damit die GUI das Image laden kann
    cv2.waitKey(0)
    cv2.destroyAllWindows()
def recursive_biliteral_filter(lab_image, d, sigma_color, sigma_space, iterations): #als eingabe
    # Apply bilateral filter recursively
    for i in range(iterations):
        # Apply bilateral filter
        filtered_image = cv2.bilateralFilter(lab_image, d, sigma_color, sigma_space)

        # Convert the filtered image back to BGR color space
        filtered_image_bgr = cv2.cvtColor(filtered_image, cv2.COLOR_LAB2BGR)

        # Update the input image for the next iteration
        lab_image = cv2.cvtColor(filtered_image_bgr, cv2.COLOR_BGR2LAB)

    # ich (Ede) habe das original_image aus dem display_images() entfernt, um es in der GUI zu testen.
    # könnt ihr gerne wieder zurückändern, falls ihr das braucht ^^
    display_images(filtered_image_bgr)
def cie_lab(image, d=70, sigma_color=10, sigma_space=70, iterations=5):
    # Convert the image from BGR (default for OpenCV) to CIE-Lab color space
    lab_image = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    # Apply bilateral filter
    recursive_biliteral_filter(lab_image, d=d, sigma_color=sigma_color, sigma_space=sigma_space, iterations=iterations)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Load the input image
    image = cv2.imread('test_image.png')
    cie_lab(image)


# ich (Ede) habe das original_image aus dem display_images() entfernt, um zu testen


