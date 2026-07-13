# Smart_Parking_System
An AI-powered smart parking detection system using OpenCV and image processing to identify vacant parking spaces from camera feeds.
# 🚗 Smart Parking System

An AI-powered Smart Parking System that detects available parking spaces using **OpenCV** and image processing. The system analyzes parking lot images or video, identifies vacant and occupied parking slots, and displays the number of available parking spaces in real time.

---

## 📖 Overview

Finding an available parking space can be time-consuming, especially in busy parking lots. This project automates parking space detection using computer vision techniques, making parking management more efficient.

---

## ✨ Features

- Detects occupied and vacant parking spaces
- Works with parking lot images and videos
- Displays the number of available parking slots
- Fast and lightweight implementation using OpenCV
- Easy to run in Google Colab or Jupyter Notebook

---

## 🛠️ Technologies Used

- Python
- OpenCV
- NumPy
- Pickle
- Google Colab

---

## 📂 Project Structure

```
Smart_Parking_System/
│── Smart_parking_detection.ipynb
│── parkingSpace.pkl
│── carPark.mp4
│── carParkImg.png
│── requirements.txt
│── README.md
└── screenshots/
```

---

## 🚀 Installation

### Clone the repository

```bash
git clone https://github.com/s14-s/Smart_Parking_System.git
```

### Move into the project directory

```bash
cd Smart_Parking_System
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the project

Open the notebook in **Google Colab** or **Jupyter Notebook** and execute all the cells.

---

## ⚙️ How It Works

1. Loads the parking lot image or video.
2. Reads predefined parking space coordinates from `parkingSpace.pkl`.
3. Processes each parking space using image processing techniques.
4. Determines whether each parking slot is occupied or vacant.
5. Displays the parking status and the total number of available spaces.

---

## 📸 Screenshots

Add screenshots of your project inside a folder named `screenshots`.

Example:

```
screenshots/
├── output1.png
├── output2.png
```

Then display them in the README:

```markdown
![Parking Detection](screenshots/output1.png)

![Available Spaces](screenshots/output2.png)
```

---

## 📌 Future Improvements

- Live CCTV camera integration
- YOLO-based vehicle detection
- Web dashboard using Streamlit
- Mobile application support
- IoT-based smart parking management

---

## 👩‍💻 Author

**Siddhi Ambatkar**

B.Tech – Computer Science and Business Systems

GitHub: https://github.com/s14-s

---

## 📄 License

This project is intended for educational and academic purposes.
