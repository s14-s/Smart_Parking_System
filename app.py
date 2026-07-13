import streamlit as st
import cv2
import pickle
import numpy as np
import os

st.set_page_config(
    page_title="Smart Parking System",
    page_icon="🚗",
    layout="wide"
)

st.title("🚗 Smart Parking System")
st.markdown("### AI-powered Parking Space Detection using OpenCV")

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.header("Settings")

video_option = st.sidebar.selectbox(
    "Choose Parking Video",
    (
        "carPark[1].mp4",
        "carPark[2].mp4",
        "carPark[3].mp4",
        "carPark[4].mp4"
    )
)

video_index = video_option.split("[")[1].split("]")[0]
positions_file = f"CarParkPos_{video_index}.pkl"

threshold_factor = st.sidebar.slider(
    "Detection Threshold",
    0.05,
    0.50,
    0.15,
    0.01
)

FRAME_WINDOW = st.image([])

# -----------------------------
# Load Parking Positions
# -----------------------------
def load_positions():

    if os.path.exists(positions_file):
        with open(positions_file, "rb") as f:
            pos_list = pickle.load(f)

        if len(pos_list) > 0:

            if len(pos_list[0]) == 2:
                pos_list = [
                    (x, y, 107, 48, i + 1)
                    for i, (x, y) in enumerate(pos_list)
                ]

            elif len(pos_list[0]) == 3:
                pos_list = [
                    (x, y, 107, 48, slot)
                    for x, y, slot in pos_list
                ]

        return pos_list

    else:
        st.error(f"{positions_file} not found.")
        return []

pos_list = load_positions()

# -----------------------------
# Process Image
# -----------------------------
def process_frame(img):

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    blur = cv2.GaussianBlur(gray, (3,3), 1)

    thresh = cv2.adaptiveThreshold(
        blur,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY_INV,
        25,
        16
    )

    median = cv2.medianBlur(thresh,5)

    kernel = np.ones((3,3),np.uint8)

    dilate = cv2.dilate(median,kernel,iterations=1)

    return dilate
  # -----------------------------
# Parking Space Detection
# -----------------------------
def check_parking_spaces(processed_img, frame):

    free_spaces = 0

    for pos in pos_list:

        x, y, w, h, slot = pos

        crop = processed_img[y:y+h, x:x+w]

        count = cv2.countNonZero(crop)

        threshold = w * h * threshold_factor

        if count < threshold:

            color = (0,255,0)
            thickness = 4
            free_spaces += 1

        else:

            color = (0,0,255)
            thickness = 2

        cv2.rectangle(
            frame,
            (x,y),
            (x+w,y+h),
            color,
            thickness
        )

        cv2.putText(
            frame,
            f"Slot {slot}",
            (x,y-5),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            color,
            1
        )

    cv2.putText(
        frame,
        f"Free Spaces: {free_spaces}/{len(pos_list)}",
        (20,40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0,255,0),
        2
    )

    return frame


# -----------------------------
# Start Button
# -----------------------------
start = st.sidebar.button("▶ Start Detection")

if start:

    if not os.path.exists(video_option):

        st.error(f"{video_option} not found!")

    else:

        cap = cv2.VideoCapture(video_option)

        while True:

            success, frame = cap.read()

            if not success:

                cap.set(cv2.CAP_PROP_POS_FRAMES,0)
                continue

            processed = process_frame(frame)

            output = check_parking_spaces(
                processed,
                frame
            )

            FRAME_WINDOW.image(
                cv2.cvtColor(output,cv2.COLOR_BGR2RGB)
            )

        cap.release()
# -----------------------------
# Statistics
# -----------------------------
st.sidebar.markdown("---")
st.sidebar.subheader("Project Information")

st.sidebar.success("Smart Parking Detection")
st.sidebar.write("Developer: Siddhi Ambatkar")
st.sidebar.write("Technology: OpenCV + Streamlit")

st.markdown("---")

st.markdown("""
### 📌 About

This Smart Parking System uses **OpenCV image processing**
to detect whether parking spaces are occupied or vacant.

The system:

- 🚗 Detects parked vehicles
- 🟢 Marks free parking spaces
- 🔴 Marks occupied parking spaces
- 📊 Displays the total number of free spaces
""")

st.markdown("---")

st.info("Upload your parking videos and .pkl files to the repository before deployment.")
