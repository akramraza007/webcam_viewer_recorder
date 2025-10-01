📸 Webcam Viewer & Recorder
This Python script allows users to either view their webcam feed live or record it to a video file with a timestamp overlay. Built using OpenCV, it's a simple and interactive way to explore camera functionality.
🚀 Features
- Live webcam feed display
- Option to record and save video
- Timestamp overlay on recorded footage
- Input validation for user-friendly interaction
- Graceful error handling if camera fails to open
🛠 Requirements
- Python 3.x
- OpenCV (cv2) library
Install with:
`pip install opencv-python`


📂 How to Use
Run the script and choose an option:
`python webcam_viewer_recorder.py`


You'll be prompted:
Choose an option:
1. Only open the camera.
2. Open the camera and save the video
Enter:


- Press 1 to view the webcam feed.
- Press 2 to record video. You'll be asked to enter a filename (e.g., output.avi).
- Press q anytime to quit the feed or stop recording.
📁 Output
- Recorded videos are saved in .avi format using the XVID codec.
- Timestamp is embedded in the bottom-left corner of each frame.
🧠 Notes
- Make sure your webcam is connected and accessible.
- The script uses cv2.VideoCapture(0) — change the index if you have multiple cameras.
