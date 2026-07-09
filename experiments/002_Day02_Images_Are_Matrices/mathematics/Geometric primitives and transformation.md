Chapter 2.1 introduces the geometric foundations of image formation, focusing on how objects in a 3D world are mathematically mapped onto a 2D image plane. To understand these concepts, it is best to start with the "mathematical language" of computer vision: **Homogeneous Coordinates**.

### **1. Homogeneous Coordinates: The Secret Sauce**
In standard 2D geometry, a point is $(x, y)$. However, computer vision often uses **homogeneous coordinates**, represented as a 3-vector 

*   **The Math:** To get the real-world pixel coordinates back, you simply divide by the last element:
*   **The Intuition:** Imagine a slide projector. A point on the 2D slide can be represented as a ray of light in 3D space. All points along that rayare mathematically the "same" point on the screen because they differ only by a scale factor. 
*   **Why use them?** They allow us to represent **points at infinity** (where $\tilde{w} = 0$) and turn complex movements like translation into simple matrix multiplications.

---

### **2. The Hierarchy of 2D Transformations**
The sources describe how shapes can be "warped" or moved using matrices. These transformations form a hierarchy, meaning each "higher" level includes all the powers of the "lower" ones.

*   **Translation:** Moves a shape without rotating or resizing it. 
    *   *Example:* Sliding a photograph across a table.
*   **Rigid (Euclidean):** Translation + Rotation. It preserves the distance between any two points (lengths) and the angles between lines. 
    *   *Example:* Rotating a photograph on the table.
*   **Similarity:** Rigid + Scaling. It preserves the "shape" (angles) but not the size. 
    *   *Example:* Zooming in on a picture while keeping its orientation.
*   **Affine:** Can shear or stretch the shape. It preserves **parallelism**—parallel lines in the world remain parallel in the image.
    *   *Example:* Looking at a square tile from an angle where it looks like a parallelogram.
*   **Projective (Homography):** The most general 2D transform. It only preserves **straight lines**. 
    *   *Example:* How a square floor tile looks in a perspective photo—it becomes a general four-sided shape (quadrilateral).

---

### **3. 3D to 2D Projections: How Cameras "See"**
This is the process of flattening the 3D world into a 2D image.

#### **Perspective Projection (The Pinhole Model)**
This is how most real cameras work.
*   **The Math:** To find where a 3D point $(X, Y, Z)$ lands on the image, you divide the $X$ and $Y$ coordinates by the depth $Z$.
*   **The Intuition:** Objects further away ($Z$ is large) result in smaller $x$ and $y$ values on the image. This is why a person far away looks tiny compared to someone standing right in front of the lens.

#### **The Intrinsic Matrix ($K$)**
The **intrinsic matrix** $K$ tells us the specific "internal" settings of the camera.
*   **Focal Length ($f$):** Acts as a scale factor. A higher $f$ (zoom lens) makes objects appear larger on the sensor.
*   **Principal Point ($c_x, c_y$):** This is where the camera's optical axis hits the image sensor, usually near the center.
*   **The Math:** Pixel coordinates are calculated by is the 3D point relative to the camera.

---

### **4. Lens Distortions: Real-World "Curves"**
Ideal math assumes straight lines in the world stay straight in images, but real lenses aren't perfect.

*   **Radial Distortion:** This is common in wide-angle lenses.
    *   **Barrel Distortion:** Points are pushed toward the center; straight lines near the edges look like they are bulging out like a barrel.
    *   **Pincushion Distortion:** Points are pushed away from the center; edges look like they are curving inward.
*   **The Intuition:** Think of looking through a glass fishbowl. The center looks mostly normal, but the edges are heavily warped. Computer vision uses math (low-order polynomials) to "undistort" these images so straight lines become straight again.