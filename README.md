# Python Exercise App

A desktop fitness application that uses real-time computer vision to track squats and deadlifts, count repetitions, and give live form feedback — built with MediaPipe pose estimation, OpenCV, and a Tkinter/CustomTkinter GUI.

<img width="1280" height="763" alt="image" src="https://github.com/user-attachments/assets/f3b4cc18-b4bf-4da2-9a2e-14d063ed4088" />
<img width="446" height="322" alt="image" src="https://github.com/user-attachments/assets/aded3e03-128b-4a42-a11a-73a5ad45dc07" />
<img width="599" height="468" alt="image" src="https://github.com/user-attachments/assets/fabbce2b-31e1-4fc2-8d0b-bd5fe322b3fd" />
<img width="598" height="470" alt="image" src="https://github.com/user-attachments/assets/074054e5-f387-4376-bdf8-782e56807614" />
<img width="595" height="470" alt="image" src="https://github.com/user-attachments/assets/4bc0ca6d-9949-4edd-810a-8807af5e25db" />
<img width="599" height="471" alt="image" src="https://github.com/user-attachments/assets/f4159f10-1dff-497d-aa9c-69da56ee41ef" />
<img width="297" height="245" alt="image" src="https://github.com/user-attachments/assets/64870927-dbd2-4439-9650-b730ad642cf0" />


## Overview

The app opens with a login/signup screen, then launches into exercise-specific windows for squats and deadlifts. Each exercise window streams the webcam feed, detects body landmarks in real time, calculates the relevant joint angle, and uses that angle to determine the current stage of the movement (up/down), counting a rep each time a full cycle is completed.

## Features

- **User authentication** — login and signup screens, with credentials checked against a locally stored user list
- **Real-time pose detection** — uses MediaPipe Pose to detect 33 body landmarks from the live webcam feed
- **Angle-based rep counting** — calculates the relevant joint angle for each exercise (hip angle for deadlifts, knee angle for squats) using vector geometry, and classifies the current stage as "up" or "down" based on angle thresholds
- **Live rep counter and stage display** — shows the current stage and rep count on screen, updated in real time
- **Form feedback** — displays encouragement and form cues (e.g. "keep your back straight and hinge at the hips") after each completed rep, and a congratulatory message on hitting 10 reps
- **Reset control** — lets the user reset the rep counter without restarting the app
- **Onboarding instructions page** — shown after login, with usage tips (e.g. camera positioning, warm-up advice) before the user reaches the main menu
- **Settings page** — lets the user switch between light, dark and default themes, and switch the interface language between English, Spanish and French
- **In-app feedback form** — lets users report issues or leave comments (with an optional email), saved locally with a timestamp
- **Per-exercise windows** — squats and deadlifts run in their own dedicated Tkinter windows, launched from the main menu

## Tech Stack

- **Python**
- **MediaPipe** — pose estimation / landmark detection
- **OpenCV** — webcam capture and image processing
- **NumPy** — angle calculation via vector geometry
- **Tkinter / CustomTkinter** — desktop GUI
- **Pillow (PIL)** — converting OpenCV frames for display in Tkinter

## Project Structure

```
├── main.py                        # Entry point: launches login, then the exercise apps
├── Login registration system.py   # Login/signup, onboarding, settings and feedback
├── deadlift.py                    # Deadlift tracking window (hip-angle based rep counting)
├── squats.py                      # Squat tracking window (knee-angle based rep counting)
├── logi.png                       # Login screen image asset
├── requirements.txt                # Python dependencies
├── Datasheet.sample.txt            # Sample login credentials (copy to Datasheet.txt to run)
```

## How It Works

1. `main.py` launches the login/registration system.
2. On successful login, an onboarding instructions page is shown, followed by the main menu.
3. From the main menu, the user can open Settings (theme/language, feedback form) or launch the squat or deadlift tracker.
4. Each frame from the webcam is processed by MediaPipe Pose to extract body landmarks.
5. The relevant joint angle is calculated from three landmarks (e.g. shoulder–hip–knee for deadlifts) using the dot-product-based `calculate_angle()` function.
6. Crossing a defined angle threshold moves the exercise between "up" and "down" stages; a full up-to-down cycle increments the rep counter.
7. Feedback and rep/stage information are displayed live on the GUI alongside the camera preview.

## Setup

Requires **Python 3.11**. This is a hard requirement, not just a recommendation: MediaPipe does not currently provide installable packages for newer Python versions (e.g. 3.12+), since it relies on pre-built wheels that lag behind the latest CPython releases. If you have multiple Python versions installed, make sure you're using 3.11 specifically when installing dependencies and running the app.

This project was developed and tested using the Anaconda `base` environment. If you're using a different distribution (e.g. python.org), just make sure it's version 3.11.

This app expects a `Datasheet.txt` file (excluded from the repo via `.gitignore`, since it stores login credentials) in the same directory as the login script, formatted as a Python dictionary of `{username: password}` pairs.

To run the app locally:
```bash
pip install -r requirements.txt

python main.py
```

You can then log in with either of the sample accounts (`demo` / `DemoPass123`, `testuser` / `TestPass456`), or add your own by signing up through the app.

## Notes

- User credentials are stored locally rather than in a database, and this repository excludes any real user data — see `.gitignore`.
- This version tracks reps using calculated joint angles directly, rather than a trained machine-learning classifier.

## About

Originally built as an A-Level Computer Science project, exploring real-time computer vision and pose estimation. Applies object-oriented and event-driven programming to a practical fitness use case, combining a Tkinter GUI with MediaPipe-based pose tracking.
