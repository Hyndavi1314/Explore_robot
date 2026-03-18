# Explore Robot (ROS2)

## Overview

Explore Robot is a ROS2-based autonomous mobile robot simulation built for environment exploration, mapping, and navigation using a depth camera. The system integrates SLAM and the Nav2 stack to operate in unknown indoor environments.

This project is currently developed and tested entirely in simulation (Gazebo + RViz). The long-term goal is to transition this setup to a real hardware robot.

---

## What This Project Does

* Generates a map of unknown environments using visual/depth data
* Navigates autonomously using ROS2 Nav2 stack
* Simulates a mobile robot with a depth camera sensor
* Provides a full pipeline from perception → mapping → planning → control

---

## Tech Stack

* ROS2
* Gazebo
* RViz2
* Nav2 (Navigation2 stack)
* SLAM Toolbox
* URDF / Xacro

---

## System Pipeline

Depth Camera → SLAM → Map → Localization → Path Planning → Motion Execution

---

## Why Depth Camera Instead of LiDAR

I chose a depth camera instead of LiDAR to:

* Reduce hardware cost for future real-world implementation
* Simulate RGB-D perception (closer to modern robotics stacks)
* Experiment with vision-based mapping instead of purely laser-based

Trade-offs:

* More sensitive to lighting conditions (in real-world use)
* Lower accuracy compared to LiDAR in large/open environments
* More processing required

---

## Simulation Setup

* Robot modeled using URDF/Xacro
* Depth camera simulated in Gazebo
* SLAM Toolbox used for real-time mapping
* Nav2 stack for autonomous navigation
* RViz used for visualization and debugging

---

## Project Structure

```
explore_robot_pkg/
├── config/
├── launch/
├── models/
├── rviz/
├── urdf/
├── worlds/
├── CMakeLists.txt
└── package.xml
```

---

## How to Run

### Build the workspace

```
cd ~/ros2_ws
colcon build
source install/setup.bash
```

### Launch simulation

```
ros2 launch explore_robot_pkg explore_robot_gazebo.launch.xml
```

### Run SLAM and Navigation

```
ros2 launch explore_robot_pkg nav2_slam.launch.py
```

---

## Where This Kind of Robot Is Used

This type of system is similar to robots used in:

* Warehouse automation (AMRs)
* Indoor mapping and digital twin creation
* Autonomous inspection in factories
* Service robots in offices and hospitals
* Surveillance and patrolling systems

---

## Challenges Faced

* Getting SLAM to stabilize with simulated sensor data
* TF tree alignment issues between base_link, odom, and map
* Tuning Nav2 parameters for smoother navigation
* Managing sensor data noise in simulation

---

## Current Limitations

* Fully simulation-based (no hardware testing yet)
* Depth camera performance not validated in real-world conditions
* Limited obstacle complexity in current environment
* No dynamic obstacle handling

---

## Future Work

* Deploy on real robot hardware
* Integrate actual depth camera (e.g., RealSense)
* Improve obstacle avoidance
* Add dynamic environment handling
* Optimize navigation performance

---

## Final Note

This project focuses on understanding the complete robotics pipeline in ROS2 rather than just individual components. It is intended as a foundation for building a real autonomous mobile robot system.

---

## Project Status

This project is currently a work in progress and not a fully completed system.

The current focus is on building a stable simulation pipeline for autonomous exploration using ROS2. Hardware implementation and real-world testing are planned as the next phase.

Ongoing work includes improving navigation performance, handling more complex environments, and preparing the system for deployment on a physical robot.

---


## Author

Hyndavi
