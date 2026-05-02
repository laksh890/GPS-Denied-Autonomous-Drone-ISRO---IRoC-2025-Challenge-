# Contributing to GPS-Denied Drone Control System

Thank you for your interest in contributing to this project! We welcome contributions from the community to help make autonomous drone flight more accessible and robust.

## How to Contribute

### 1. Reporting Bugs
- Use the GitHub Issue Tracker.
- Provide a clear description of the bug and steps to reproduce it.
- Include hardware details (Flight Controller, Sensors).

### 2. Suggesting Enhancements
- Open an issue with the "enhancement" label.
- Explain the use case and how it benefits the project.

### 3. Pull Requests
1. Fork the repository.
2. Create a new branch for your feature or fix.
3. Follow the existing code style (PEP 8 for Python).
4. Ensure your code is well-commented.
5. Submit a pull request with a detailed description of your changes.

## Development Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Setup SITL (Software In The Loop) for testing without hardware.
3. Run the controller:
   ```bash
   python src/main.py --connect <connection_string>
   ```

## Code of Conduct
Please be respectful and professional in all interactions.

## Contact
For specific inquiries related to the ISRO IRoC-2025 Challenge, please open an issue.
