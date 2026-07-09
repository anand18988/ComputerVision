## Questions

Why uint8 is UsedMemory efficiency: 
It uses exactly 1 byte per pixel channel.
Value matching: It perfectly fits the standard 0–255 digital pixel intensity range.
Hardware alignment: CPUs and GPUs process 8-bit blocks highly efficiently.

Why BGR Instead of RGB
Historical legacy: Early camera developers and OpenCV creators chose BGR as their internal standard.
Windows compatibility: Early Windows operating systems used BGR for device-independent bitmaps (DIB).
Consistency: The order stuck to avoid breaking backward compatibility in legacy computer vision libraries.

Does Slicing Copy Memory?NumPy arrays: No, slicing creates a "view," meaning it references the original memory.

Python lists: Yes, slicing a standard list creates a shallow copy of the data.

Modification risk: Changing a sliced NumPy image alters the original image unless you explicitly use .copy().

Can Images Have More Than 3 Channels?Alpha channel: 4-channel images (RGBA) add transparency data for graphics and UI elements.
Satellite imagery: Multispectral images capture infrared, ultraviolet, and thermal bands.
Medical scans: Channels can store depth, tissue density, or time-series data.
