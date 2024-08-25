Image Processing with Recursive Bilateral Filter
This script applies a recursive bilateral filter to an image in the CIE-Lab color space, creating a smooth, cartoon-like effect while preserving the edges of the image.

Requirements:
Python 3.x
OpenCV
NumPy
Matplotlib
SciPy

How It Works:
Load Image: The script starts by loading the input image using OpenCV.

Convert to CIE-Lab Color Space: The image is converted from the default BGR color space to CIE-Lab, which better represents how humans perceive color.

Apply Recursive Bilateral Filter: A bilateral filter is applied multiple times to smooth the image while keeping edges sharp. The parameters for the filter, including the spatial and color standard deviations, can be adjusted in the cie_lab() function.

Save Output: The final filtered image is saved as cartoonfilter_result.jpg.

Customization:
You can customize the filter parameters by modifying the cie_lab() function:

d: Diameter of each pixel neighborhood.
sigma_color: Filter sigma in the color space.
sigma_space: Filter sigma in the coordinate space.
iterations: Number of times the filter is applied.