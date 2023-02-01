
# Rubik's Cube Robot

A program that uses 2 cameras to capture the sides of a Rubik's Cube and uses the ociemba algorithm to find a solution (will soon also control 6 motors to turn cube in a robot)

Includes CAD files for 3D printing of the structure

## Installation

```bash
  git clone https://github.com/fiifichristian/rubiksCubeRobot
```

## Usage/Examples

```bash
usage: py IP.py [-h] [-s | -S SOLVE | -p | -c]

options:
  -h, --help            show this help message and exit
  -s, --scramble        Gives a set of instructions for scrambling the cube
  -S SOLVE, --solve SOLVE
                        Uses camera to help solve the cube. Use argument 0 for 2D scanning and 1  
                        for 3D scanning
  -p, --caliCoord       Uses camera to calibrate positions of the colours on the cube
  -c, --caliColours     Uses camera to calibrate colours read
```

## Acknowledgements

[Kociemba Solving Algorithm](https://github.com/muodov/kociemba)
