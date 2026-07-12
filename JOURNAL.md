# Autonomous Vehicle ROS 2 Project — Journal

## Day 1 — Saturday [date]

### What I did
- Set up dual-boot Ubuntu 22.04 on Dell Precision 7530
- Recovered from NVIDIA driver issue using recovery mode root shell
- Installed ROS 2 Humble using the modern apt-source .deb method
- Created ros2_ws workspace
- Practiced CLI commands: ros2 node, topic, interface, pkg
- Set up VS Code with ROS extensions
- First experience with rqt_graph

### What confused me
-

### What clicked
-

### Questions for next session

## Day 3 — 6/12/26

### What I did
- Created listener_node.py with a String subscriber on /mason_chat
- Registered second entry point in setup.py
- Debugged: module not found error → file location issue
- Debugged: AttributeError → method name mismatch (listener_callback vs message_callback)
- Got pub/sub working end-to-end

### What clicked
- Topics are just named channels. Publishers and subscribers don't know about each other directly.
- The build cycle: edit → colcon build → source install/setup.bash → run
- Python tracebacks are super helpful — read bottom-up

### Gotchas I want to remember
- Python silently concatenates adjacent strings (missing comma in lists = silent merge)
- ROS 2 module path = inner folder, not outer
- Callback names must match between create_subscription() and the method definition
- Linux is case-sensitive — listener_node.py ≠ Listener_node.py

### Questions for next session




- ## Week 2, Day 1 — [date]

### What I did
- Created new package: my_robot_description (ament_cmake)
- Wrote first URDF: a blue box chassis
- Validated with check_urdf
- Visualized in RViz via urdf_tutorial display.launch.py
- Experimented with cylinder, sphere, different sizes & colors

### Concepts learned
- URDF = XML tree of links + joints
- Each link has visual (RViz), collision (physics), inertial (mass)
- `origin xyz` positions the visual within the link's frame
- ROS convention: X forward, Y left, Z up
- robot_state_publisher reads URDF, publishes TF tree

### What clicked
-

### What confused me
-

### Questions
-
-## Week 2, Day 2 — [date]

### What I did
- Added left + right wheels as cylinder links
- Connected wheels with continuous joints (axis Y, so they rotate around left-right axis)
- Added fixed caster wheel (sphere) for stability
- Added fixed sensor mount box for future LiDAR
- Experimented with wheel size, wheelbase, sensor mount orientation
- Verified with check_urdf: root base_link has 4 children

### Concepts learned
- Joint types: continuous (infinite rotation), fixed (no motion), revolute (limited), prismatic (linear)
- Every joint has: parent, child, origin (xyz + rpy), and for moving joints — axis
- rpy = roll/pitch/yaw in RADIANS. 1.5708 = π/2 = 90°
- Cylinders default upright on Z; roll 90° around X to make wheels on Y axis
- Joint state publisher GUI provides sliders for testable joints (not fixed ones)
- The TF tree in RViz shows every frame — this becomes critical for sensor data later

### What clicked
-

### Gotchas to remember
- rpy values are RADIANS not degrees — π/2 ≈ 1.5708 for 90°
- Wheel Z offset must match wheel radius or wheels sink/float
- Wheel Y offset must exceed chassis half-width or wheels clip through the body
- `fixed` joints don't appear in the joint state publisher GUI (nothing to move)
- Root link (base_link) has no parent — every other link must have exactly one parent

### Questions
-what are joint and links 