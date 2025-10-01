import cv2
import datetime

def open_camera_only():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Could not read frame")
            break
        cv2.imshow("Webcam Feed", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("Quitting.....")
            break

    cap.release()
    cv2.destroyAllWindows()

def record_camera():
    camera = cv2.VideoCapture(0)
    if not camera.isOpened():
        print("Error: Could not open camera.")
        return

    frame_width = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))
    codec = cv2.VideoWriter_fourcc(*'XVID')

    filename = input("Enter filename to save (e.g., output.avi): ")
    recorded = cv2.VideoWriter(filename, codec, 20, (frame_width, frame_height))

    while True:
        success, image = camera.read()
        if not success:
            print("Could not read frame")
            break

        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cv2.putText(image, timestamp, (10, frame_height - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 1)

        recorded.write(image)
        cv2.imshow("Recording live", image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("Recording stopped.")
            break

    camera.release()
    recorded.release()
    cv2.destroyAllWindows()

while True:
    op = input("Choose an option:\n1. Only open the camera.\n2. Open the camera and save the video\nEnter: ")
    if op == "1":
        open_camera_only()
        break
    elif op == "2":
        record_camera()
        break
    else:
        print("Invalid input. Please enter 1 or 2.")
