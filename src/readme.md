# GPS-Denied Autonomous Drone Control System

Autonomous drone navigation and stabilization in GPS-denied environments using PID control, Optical Flow, IMU, and Rangefinder sensors.

---

## 🚀 Overview

This project enables a drone to perform autonomous **takeoff, hover, drift correction, and landing** in environments where GPS is unavailable.

Instead of GPS, the system uses onboard sensors and control algorithms to maintain stable flight.

### Core Technologies Used

- PID Control
- Optical Flow Sensor
- IMU Data
- Rangefinder / LiDAR
- Pixhawk Flight Controller
- Python + DroneKit

---

## ✨ Features

- ✅ Autonomous Takeoff
- ✅ Stable Hover at Target Altitude
- ✅ GPS-Denied Drift Compensation
- ✅ Safe Autonomous Landing
- ✅ Real-Time RC PWM Control
- ✅ Modular Codebase for Future Expansion

---

## 🧠 Use Cases

- Indoor Autonomous Navigation
- Warehouse Inspection
- Search & Rescue Missions
- Mars Terrain Analog Challenges
- Defense Reconnaissance
- Research & Education

---

## 🛠 Hardware Requirements

- Pixhawk Flight Controller
- Optical Flow Sensor
- Rangefinder / LiDAR
- Raspberry Pi / Companion Computer
- Telemetry Link
- Quadcopter Frame

---

## 💻 Software Requirements

- Python 3.9+
- ArduPilot Firmware
- DroneKit
- pymavlink

--- 

## Run

python src/main.py --connect /dev/ttyACM0

---
## 🧭 Flight Mission Sequence
- Arm Drone
- Autonomous Takeoff to Target Altitude
- Stable Hover with Drift Correction
- Controlled Landing

---

## 📈 Future Roadmap
 - ArUco Marker Precision Landing
 - Obstacle Avoidance
 - SLAM Navigation
 - ROS2 Integration
 - Gazebo Simulation
 - AI Mission Planning
 - Telemetry Dashboard

---

## 📁 Project Structure

```text
gps-denied-drone/
│── src/
│   ├── controllers/
│   │   └── pid.py
│   │
│   ├── drone/
│   │   ├── connection.py
│   │   ├── rc.py
│   │   └── mission.py
│   │
│   ├── config.py
│   └── main.py
│
├── docs/
├── tests/
├── README.md
├── requirements.txt
└── LICENSE