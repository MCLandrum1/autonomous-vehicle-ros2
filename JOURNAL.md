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

## Week 2, Day 3 — [date]

### What I did
- Wrote custom display.launch.py using robot_state_publisher + joint_state_publisher_gui + rviz2
- Updated CMakeLists.txt to install urdf/, launch/, rviz/ folders
- Saved RViz config to rviz/display.rviz
- Inspected /tf and /tf_static topics with ros2 topic echo
- Generated TF tree PDF with ros2 run tf2_tools view_frames
- Used tf2_echo to query live transforms between frames
- Broke the TF tree intentionally to understand failure modes

### Concepts learned
- TF2 tracks every coordinate frame in the robot
- Two flavors: /tf_static (once, from fixed joints) and /tf (continuous, from moving joints)
- robot_state_publisher: reads URDF + /joint_states → publishes /tf and /tf_static
- joint_state_publisher_gui is a "fake driver" — real robots use hardware/simulation
- Every sensor message has a frame_id in its header
- RViz Fixed Frame = the "camera anchor" for rendering
- If a frame doesn't exist or its parent chain is broken, downstream nodes fail

### What clicked
-

### Gotchas to remember
- `map` frame doesn't exist until we set up localization (Week 4+)
- Killing robot_state_publisher = TF tree collapses = RViz shows nothing
- Fixed Frame must be reachable via the TF tree from whatever you're rendering
- CMakeLists.txt install() block is required for launch files / URDF to be found after build

### Questions
-Kill didnt work 
what does TF stand for



## Week 2, Day 4 — [date]

### What I did
- Converted my_robot.urdf → my_robot.urdf.xacro
- Added xacro namespace to <robot> tag
- Extracted magic numbers into <xacro:property> variables
- Rewrote geometry using ${property_name} substitutions
- Wrote a <xacro:macro> for the wheel (parameterized by prefix + y_offset)
- Replaced two identical wheel blocks with two macro calls
- Updated display.launch.py to use xacro.process_file() at launch time
- Added xacro dependency to package.xml

### Concepts learned
- Xacro = XML macros for URDF
- xmlns:xacro namespace unlocks <xacro:...> tags
- <xacro:property name="X" value="Y"/> defines a variable
- ${expression} evaluates math + substitutes properties inline
- <xacro:macro name="X" params="a b"> ... </xacro:macro> defines reusable snippet
- <xacro:X a="..." b="..."/> instantiates it
- xacro.process_file() converts xacro → plain URDF at runtime
- The .urdf.xacro extension is convention

### What clicked
-

### The payoff
- Changing wheel_radius updated 4 places automatically (2 radii + 2 Z offsets)
- Chassis height changes auto-move sensor mount to stay on top
- Macros eliminated duplicate wheel code; DRY principle applied

### Gotchas
- Don't forget `$` before `{...}`
- Xacro won't catch typos in property names — you'll get literal strings in output
- Must add xac