# Autonomous Vehicle — ROS 2

A 16-week project to build an autonomous outdoor ground vehicle using ROS 2 Humble.
The first stage of a longer journey toward an autonomous underwater vehicle for pond bathymetry.

## Project Goal

Build a 1/10-scale RC-car-based autonomous vehicle that:
- Navigates between GPS waypoints autonomously
- Avoids obstacles using LiDAR
- Uses sensor fusion (GPS + IMU + wheel odometry)
- Runs on ROS 2 Humble + Nav2 stack

## Status

🚧 **Week 1 — ROS 2 Foundations** (in progress)

## Tech Stack

- **OS:** Ubuntu 22.04
- **Framework:** ROS 2 Humble
- **Languages:** Python, C++
- **Compute (planned):** NVIDIA Jetson Orin Nano
- **Sensors (planned):** u-blox ZED-F9P RTK GPS, BNO055 IMU, RPLiDAR A2

## Repository Structure
─ ros2_ws/              # ROS 2 workspace
│   └── src/              # Source packages
│       └── my_first_pkg/ # Learning package
├── docs/                 # Design docs, diagrams
├── JOURNAL.md            # Daily development journal
└── README.md             # This file

## Roadmap

- [x] Week 1: ROS 2 fundamentals (pub/sub, launch files)
- [ ] Week 2-3: Simulation in Gazebo
- [ ] Week 4-6: Nav2 + autonomy in simulation
- [ ] Week 7-10: Physical vehicle build
- [ ] Week 11-14: Autonomous outdoor operation
- [ ] Week 15-16: Polish + portfolio

## Author

Mason Landrum — Mechatronics Engineer at SLAC