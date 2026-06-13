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
- 
-