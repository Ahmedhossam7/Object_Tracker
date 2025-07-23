# 🎯 Object_Tracker

Real-time object tracking using OpenCV.

This project implements a real-time object tracker using Python and OpenCV. It allows a user to select an object in the first frame of a webcam feed and then continuously tracks that object using the CSRT tracking algorithm. If tracking is lost, the user can press 'A' to reselect the object and continue tracking.

Features:
- Real-time webcam feed tracking
- ROI (Region of Interest) selection via mouse
- Re-selection option when tracking fails (press 'A')
- ESC key exits the program
- Uses OpenCV’s `cv2.TrackerCSRT_create()`

Installation:
1. Clone this repository:
   
   git clone https://github.com/YOUR_USERNAME/Object_Tracker.git
   cd Object_Tracker
   

2. Install required dependencies:
   
   pip install opencv-contrib-python
   

3. Run the tracking script:
   
   python Object_Tracker.py
   

Implementation Details:
- Language: Python
- Library: OpenCV (via `opencv-contrib-python`)
- Tracking Algorithm: CSRT (Discriminative Correlation Filter)
- The webcam feed starts and shows the first frame.
- The user selects a region of interest (ROI) with the mouse.
- Tracking continues in real time as the object moves.
- If tracking is lost, the program displays a message.
- The user can press 'A' to select a new object and resume tracking.


Requirements:
- Python 3.6 or newer
- OpenCV with contrib modules:
   ```
   pip install opencv-contrib-python
   ```

Controls:
- Press `ESC` → Exit the program
- Press `A` → Re-select object if tracking is lost

---

© 2025 Ahmed Hossam — Developed as part of the ML & Computer Vision Internship Task for Eyego
