# GPS-Denied Autonomous Drone Control System

![Project Banner](C:/Users/hp/.gemini/antigravity/brain/f866ba42-d59e-4e1d-bf3b-495e6b12e845/drone_project_banner_1777738290520.png)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![ISRO Challenge](https://img.shields.io/badge/Competition-ISRO%20IRoC--2025-orange)](https://www.isro.gov.in/)

Autonomous drone navigation and stabilization system designed for environments where GPS is unavailable. Developed for the **ISRO IRoC-2025 Challenge**, this project leverages sensor fusion and PID control to achieve stable flight in GPS-denied scenarios.

---

## 🚀 Overview

This project enables a quadcopter to perform autonomous **takeoff, hover, drift correction, and smart landing** without relying on external positioning systems. 

The system uses onboard sensors (Optical Flow, IMU, Rangefinder) to estimate position and velocity, providing a robust solution for indoor inspections, warehouse automation, and extraterrestrial exploration analogs.

### Core Technologies
- **Control:** Custom PID Loops for Altitude, Roll, and Pitch.
- **Sensing:** Optical Flow (Drift), Rangefinder (Altitude), IMU (Attitude).
- **Platform:** Pixhawk Flight Controller + Raspberry Pi Companion Computer.
- **Software:** Python, DroneKit, MAVLink.

---

## ✨ Key Features

- ✅ **Autonomous State Management:** Modular `DroneController` class for scalable mission planning.
- ✅ **GPS-Denied Stability:** Real-time drift compensation using Optical Flow.
- ✅ **Smart Landing:** Controlled descent with horizontal stabilization for safe touchdown.
- ✅ **Safety First:** Integrated failsafes for sensor loss and emergency landing.
- ✅ **Telemetry Logging:** Detailed logging for post-flight analysis.

---

## 🛠 Hardware Requirements

- **Flight Controller:** Pixhawk 2.4.8 (or any ArduPilot compatible FC).
- **Companion Computer:** Raspberry Pi 4B / Jetson Nano.
- **Sensors:**
  - Optical Flow Sensor (e.g., PMW3901).
  - LiDAR / Ultrasonic Rangefinder (e.g., TF-Luna, VL53L1X).
- **Frame:** 450mm - 250mm Quadcopter.

---

## 💻 Getting Started

### Prerequisites
- Python 3.9 or higher.
- ArduPilot Firmware (Copter 4.0+) installed on the FC.

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/laksh890/GPS-Denied-Autonomous-Drone-ISRO---IRoC-2025-Challenge-.git
   cd GPS-Denied-Autonomous-Drone-ISRO---IRoC-2025-Challenge-
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the System
Connect your companion computer to the Pixhawk via UART/USB and run:
```bash
python src/main.py --connect /dev/ttyACM0
```

---

## 📈 Roadmap

- [ ] **ArUco Marker Precision Landing:** Visual docking for battery replacement.
- [ ] **Obstacle Avoidance:** Integration of 360-degree LiDAR.
- [ ] **SLAM Navigation:** Simultaneous Localization and Mapping for complex environments.
- [ ] **ROS2 Support:** Porting the core logic to a ROS2 workspace.

---

## 🤝 Contributing

We welcome contributions! Whether it's a bug fix, feature request, or documentation improvement, please check out our [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

---

## 📁 Project Structure

```text
gps-denied-drone/
├── src/
│   ├── controllers/
│   │   └── pid.py          # Core PID control logic
│   ├── drone/
│   │   ├── controller.py   # High-level Drone Class (NEW)
│   │   ├── connection.py   # MAVLink connection management
│   │   ├── mission.py      # Mission state logic
│   │   ├── failsafe.py     # Safety protocols
│   │   └── rc.py           # RC Override utilities
│   ├── config.py           # Tuning parameters & constants
│   └── main.py             # Entry point
├── docs/                   # Documentation & diagrams
├── LICENSE                 # MIT License
└── README.md               # You are here
```

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🏆 Acknowledgements

- **ISRO** for the IRoC-2025 Challenge opportunity.
- **ArduPilot & DroneKit** communities for the robust infrastructure.