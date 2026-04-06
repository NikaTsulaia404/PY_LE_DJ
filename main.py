import  pyautogui
import  cv2
import numpy as np
import pyscreeze

resolution = (1920, 1080) #Specify resolution

codec = cv2.VideoWriter_fourcc(*"XVID") # Specify video codec

filename = "Recording.avi" # Specify name of Output file

fps = 75.0 # Specify frames rate

out = cv2.VideoWriter(filename, codec, fps, resolution) # Creating a VideoWriter object

cv2.namedWindow("Live", cv2.WINDOW_NORMAL) # Create an Empty window

cv2.resizeWindow("Live", 480, 270) # Resize this window

while True:
    # Take screenshot using PyAutoGUI
    img = pyautogui.screenshot()

    # Convert the screenshot to a numpy array
    frame = np.array(img)

    # Convert it from BGR(Blue, Green, Red) to
    # RGB(Red, Green, Blue)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Write it to the output file
    out.write(frame)

    # Optional: Display the recording screen
    cv2.imshow('Live', frame)

    # Stop recording when we press 'q'
    if cv2.waitKey(1) == ord('q'):
        break

# Release the Video writer
out.release()

# Destroy all windows
cv2.destroyAllWindows()
