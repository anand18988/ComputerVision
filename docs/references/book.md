Computer Vision: Algorithms and Applications
Richard Szeliski

Real World (3D)
       │
       ▼
Light reflects from objects
       │
       ▼
Camera lens collects light
       │
       ▼
Image projected on sensor
       │
       ▼
Sensor converts light → numbers
       │
       ▼
Digital Image (Pixels)

Computer Vision is the inverse of image formation.

Image formation: 3D world → 2D image
Computer vision: 2D image → infer the original 3D world

Image Formation
│
├── Geometric Image Formation
│     ├── Coordinates
│     ├── Transformations
│     ├── Rotations
│     ├── Camera Projection
│     └── Lens Distortion
│
├── Photometric Image Formation
│     ├── Lighting
│     ├── Reflection
│     ├── Shading
│     └── Optics
│
└── Digital Camera
      ├── Sensor
      ├── Sampling
      ├── Color
      └── Compression
      
Learning OpenCV

OpenCV Documentation

The **Open Source Computer Vision (OpenCV)** library is the world's most popular open-source library for building computer vision applications. Originally developed by Gary Bradski and his colleagues at Intel, it now contains more than **2,500 optimized algorithms** covering both classic and state-of-the-art techniques.

### **Core Documentation Structure**
The documentation is organized to guide users from basic setup to advanced AI deployment:
*   **Getting Started:** Includes a **Quickstart Guide** that covers installation via various package managers (like pip for Python or vcpkg for Windows) and the basics of loading, displaying, and processing your first image.
*   **Core Concepts:** Defines fundamental structures such as **Matrices (Mat)**, image basics, and memory management.
*   **Functional Modules:** The library is divided into specialized modules, including:
    *   **Image Processing:** Filtering, transformations, and color space conversions.
    *   **Video Analysis:** Tracking, motion detection, and background subtraction.
    *   **3D Reconstruction:** Camera calibration, pose estimation, and stereo vision.
    *   **Feature Detection:** Support for keypoint detectors like SIFT, SURF, and ORB.
    *   **DNN (Deep Neural Network):** Allows running neural networks from frameworks like **TensorFlow, PyTorch, and ONNX**.
    *   **Machine Learning:** Statistical classification and regression tools.

### **Language Bindings and Platforms**
OpenCV is designed for high performance across diverse environments:
*   **Languages:** Official support is provided for **C++, Python, Java, and JavaScript (opencv.js)**, with some documentation also noting MATLAB interfaces.
*   **Platforms:** The library can be built and run on **Linux, Windows, macOS, Android, and iOS**.

### **Practical Highlights for Users**
*   **Color Format:** A critical technical note in the documentation is that OpenCV uses **BGR color format** by default, rather than the standard RGB format.
*   **Learning Resources:** The documentation provides **step-by-step tutorials** for common tasks, a comprehensive **API Reference** detailing every function, and real-world **code examples** in Python and C++.
*   **Advanced Features:** Users can explore complex tasks such as face detection using cascade classifiers, intelligent photo editing, and large-scale feature matching.

For developer collaboration and source access, the documentation directs users to the official **GitHub repository**, where they can report issues and contribute to the codebase.


NumPy Documentation

The official **NumPy documentation** for the current stable version (v2.5) is the primary resource for scientific computing in Python, providing a multidimensional array object, derived objects like masked arrays, and various routines for fast array operations. 

The documentation is organized into several key sections to support users at different expertise levels:

### **1. Learning and Tutorials**
The documentation includes a curated "Learn" section with resources for both beginners and advanced users:
*   **Beginner Resources:** Includes "the absolute basics for beginners," a "Quickstart Tutorial," and visual guides. It covers fundamental concepts such as how to import NumPy, what an array is, and basic indexing and slicing.
*   **Advanced Resources:** Offers tutorials on advanced indexing, linear algebra, and performance-driven code. 
*   **Educational Materials:** Links to external books (e.g., *Guide to NumPy* by Travis E. Oliphant), videos, and community-vetted lectures.

### **2. User Guide**
The **User Guide** provides in-depth explanations of NumPy's key concepts and background information. Key areas include:
*   **Fundamentals:** Detailed guides on array creation, indexing, broadcasting, and universal functions (ufuncs).
*   **Advanced Usage:** Documentation on the **NumPy C-API**, which details how to extend NumPy or use Python as "glue" for other compiled libraries, and the **F2PY** user guide for Fortran interoperability.
*   **Specialized Topics:** Instructions on writing performant code with multi-core CPUs and internal memory organization (e.g., C-style vs. Fortran-style memory layout).

### **3. API Reference**
The **API Reference** details every function, module, and object included in the library, assuming the user already understands core concepts.
*   **Python API:** Covers the structure of the `ndarray` object, data type objects (`dtype`), and routines organized by topic, such as linear algebra (`linalg`), Fourier transforms (`fft`), and random sampling.
*   **C API:** Includes documentation on Python types, C-structures, system configuration, and memory management.

### **4. Core Object: The N-Dimensional Array (ndarray)**
A significant portion of the documentation is dedicated to the `ndarray`, a multidimensional container for homogeneous data. 
*   **Attributes:** It details intrinsic properties like `ndim` (number of dimensions), `shape` (size of each dimension), `size` (total elements), and `dtype` (data type).
*   **Methods:** Lists hundreds of methods for array conversion, shape manipulation (e.g., `reshape`, `transpose`, `flatten`), and calculations (e.g., `sum`, `mean`, `max`).
*   **Internal Layout:** Explains how NumPy uses **strided indexing** to map multidimensional indices to contiguous segments of computer memory.

### **5. Contributor and Supplementary Guides**
*   **Contributor’s Guide:** Provides guidelines for those wishing to add to the codebase, help with translations, or improve the documentation itself.
*   **Release Notes and License:** Tracks historical versions and provides the official NumPy license information.
*   **Community Support:** Includes links to the source repository on GitHub, issue trackers, and mailing lists for Q&A support.