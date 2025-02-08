import cv2

def main():
    # Open the camera (index 0 = default camera)
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Could not open webcam.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame.")
            break

        # Show the current frame
        cv2.imshow("Live Feed", frame)

        # Wait briefly (1 ms), and if 'q' is pressed, exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Cleanup
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
