What is a digital image?

It is a visual representation of 2d picture converted into numerical format.



What is a pixel?

each digital image is made of grids or tiny dots(pixel) which is assigned specific values to determine precise color and brightness.



Why are images matrices?

Mathematical grid of the number which represents digital image.

Structure of an Image Matrix The structure depends entirely on whether the image is grayscale or color:



Grayscale Image (2D Matrix): Represented as a single 2D grid of rows and columns. 

Each cell in the matrix corresponds to one pixel, and the number inside represents the brightness (0 for black, 255 for white).



Color Image (3D Matrix/Tensor): Represented as a 3D grid. It consists of three stacked 2D matrices (often called channels), one each for Red, Green, and Blue.



What is an RGB image?

An RGB image is a digital color image created by mixing three primary colors of light: Red, Green, and Blue. 

It is an additive color model, meaning that colors are created by adding light wavelengths together. 

This is the exact method used by digital screens (monitors, smartphones, TVs) to display colored graphics.



1\. How the RGB System Works An RGB image is split into three separate layers called color channels. 

Each channel acts like a grayscale image that dictates the intensity of that specific light source: Red Channel: Controls the amount of red light. Green Channel: Controls the amount of green light. Blue Channel: Controls the amount of blue light. 



When your screen displays an RGB image, **it illuminates microscopic red, green, and blue sub-pixels at varying intensities.** Because these sub-pixels are packed tightly together, your e**ye blends them to perceive a single, cohesive color.**



What is a grayscale image?

A grayscale image is a digital image where the only color information is the intensity of light, ranging from absolute black to absolute white.



Why does OpenCV use BGR?

OpenCV uses the BGR (Blue, Green, Red) channel order instead of RGB purely due to historical engineering choices and legacy hardware compatibility. When Intel developers first created OpenCV in the late 1990s, BGR was the prevailing industry standard for many hardware and software systems.

----------------------------------------book-------------------------------------------------------------
### **Summary of Chapter 2.1: Geometric Primitives and Transformations**

Chapter 2.1 establishes the foundational geometric vocabulary and mathematical models used to describe the transition from 3D scenes to 2D images. This section is essential for a scientific, model-based approach to computer vision.

#### **1. Geometric Primitives**
The text introduces basic 2D and 3D primitives, including **points, lines, and planes**.
*   **Homogeneous Coordinates:** Primitives are primarily represented using homogeneous coordinates (projective space), where a 2D point is a 3-vector and a 3D point is a 4-vector. Vectors that differ only by a scale factor are considered equivalent.
*   **Coordinate Conversion:** Homogeneous coordinates can be converted to standard inhomogeneous coordinates by dividing all elements by the last element (e.g., $w$). Points where the last element is zero are "ideal points" or "points at infinity".
*   **2D Lines:** Represented by the equation $ax + by + c = 0$, or as a normalized vector $(\hat{n}, d)$ where $\hat{n}$ is the normal and $d$ is the distance to the origin.

#### **2. Transformations**
The section covers how these primitives are manipulated in space:
*   **2D Transformations:** Includes operations like **translation**, which can be written compactly using matrix multiplication. Chaining multiple transformations is achieved by multiplying their corresponding 3x3 matrices.
*   **3D Transformations and Rotations:** The chapter explores 3D transformations and complex 3D rotations, which are necessary to define the pose of a camera or object in space.

#### **3. 3D to 2D Projection Models**
The author describes several models for mapping 3D world points into 2D image features:
*   **Perspective Projection:** The most common model, mimicking how light passes through a pinhole. Mathematically, it involves dividing $x$ and $y$ coordinates by the $z$ (depth) component. This process makes it impossible to recover a point's original distance from a single 2D sensor.
*   **Alternative Models:** Other models include **orthography**, scaled orthography, and para-perspective. These models are often used as simplifications where parallel lines in the world remain parallel in the projection.

#### **4. Camera Intrinsics and Calibration**
*   **The Intrinsic Matrix ($K$):** This matrix maps 3D camera-centered points to 2D pixel coordinates. It accounts for physically measurable quantities like **focal length**, **principal point** (the image center), **aspect ratio**, and **skew**.
*   **Simplified Models:** In many practical applications, the model can be simplified by assuming square pixels (aspect ratio of 1) and a centered principal point, leaving focal length as the primary unknown.

#### **5. Real-World Distortions and Alignments**
*   **Radial Distortion:** Real-world lenses often introduce distortions where coordinates are displaced toward (**barrel distortion**) or away from (**pincushion distortion**) the image center. These are typically modeled using low-order polynomials to correct the image.
*   **Homographies:** Planar homographies (3x3 matrices) are used to relate two different views of the same planar scene, serving as a foundational tool for **image alignment and stitching**.