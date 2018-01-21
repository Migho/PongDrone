# PongDrone

PongDrone is a program which purpose is to be the best beer pong playing AI. The unit we control is Parrot AR Drone 2.0. Project is for Helsingin yliopisto course Robottiohjelmoinnin harjoitustyö (TKT21013)

## Documentation

* [Specification document (in finnish)](https://github.com/Migho/PongDrone/blob/master/documentation/specification.md)
* [Implementation document (in finnish)](https://github.com/Migho/PongDrone/blob/master/documentation/implementation.md)
* [Testing document (in finnish)](https://github.com/Migho/PongDrone/blob/master/documentation/testing.md)
* [Weekly reports (in finnish)](https://github.com/Migho/PongDrone/blob/master/documentation/weeklyReports.md)

## User guide

You can launch the system by writing
```
python src/PongDrone.py
```
on the command line. Be careful, the drone will takeoff without asking any questions! The drone will start in autopilot mode, meaning it will try to find circles (cups) using the ground camera and move above them. The program will launch two windows: the one showing live stream of the ground camera, and the second one called "computer" showing the moves and actions autopilot does.

Autipilot controls:
```
m   =   Turn manual control on
q   =   Land the drone and shut down the system
```

When enterning to the manual control, the controls are the following (note: numpad recommended):
```
/   =   Turn autopilot on         -----------
8   =   Move forward              | 7 8 9 / |
2   =   Move backward             | 4 5 6 * |
4   =   Move left                 | 1 2 3 - |
6   =   Move right                | 0     + |
7   =   Turn left                 -----------
9   =   Turn right
5   =   Hover in place (stop)
+   =   Fly higher
-   =   fly lower
q   =   Land the drone and shut down the system
```

When autopilot successfully hover above the cup, it will do a flip. After this it enters eternal wait mode, and by turning manual control on user can move the drone to safe landing spot and land the drone.
