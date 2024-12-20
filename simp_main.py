import numpy as np
from trafficSim import *
import csv

sim = Simulation()

# Play with these
n = 20      # Iterations for road turns
a = -2      # Indicates point a 
b = 12      # Indicates point b
l = 100     # Length of road

NUM_OF_ROADS = 24 # Number of roads

# VEHICLE_RATE = 16 # Vehicle spawn rate per minute
VEHICLE_RATE = 80 # Vehicle spawn rate per minute

STEPS_PER_UPDATE = 10   # Number of steps per update

# Nodes
WEST_RIGHT_START = (-b-l, a)
WEST_LEFT_START =	(-b-l, -a)

SOUTH_RIGHT_START = (a, b+l)
SOUTH_LEFT_START = (-a, b+l)

EAST_RIGHT_START = (b+l, -a)
EAST_LEFT_START = (b+l, a)

NORTH_RIGHT_START = (-a, -b-l)
NORTH_LEFT_START = (a, -b-l)

WEST_RIGHT = (-b, a)
WEST_LEFT =	(-b, -a)

SOUTH_RIGHT = (a, b)
SOUTH_LEFT = (-a, b)

EAST_RIGHT = (b, -a)
EAST_LEFT = (b, a)

NORTH_RIGHT = (-a, -b)
NORTH_LEFT = (a, -b)

# Create Nodes with offset to avoid overlapping
WEST_RIGHT_START2 = (WEST_RIGHT_START[0], WEST_RIGHT_START[1] - 4)
WEST_LEFT_START2 = (WEST_LEFT_START[0], WEST_LEFT_START[1] + 4)

SOUTH_RIGHT_START2 = (SOUTH_RIGHT_START[0] - 4, SOUTH_RIGHT_START[1])
SOUTH_LEFT_START2 = (SOUTH_LEFT_START[0] + 4, SOUTH_LEFT_START[1])

EAST_RIGHT_START2 = (EAST_RIGHT_START[0], EAST_RIGHT_START[1] + 4)
EAST_LEFT_START2 = (EAST_LEFT_START[0], EAST_LEFT_START[1] - 4)

NORTH_RIGHT_START2 = (NORTH_RIGHT_START[0] + 4, NORTH_RIGHT_START[1])
NORTH_LEFT_START2 = (NORTH_LEFT_START[0] - 4, NORTH_LEFT_START[1])

# Create Nodes with offset to avoid overlapping
# WEST_RIGHT_START3 = (WEST_RIGHT_START[0], WEST_RIGHT_START[1] - 8)
# WEST_LEFT_START3 = (WEST_LEFT_START[0], WEST_LEFT_START[1] + 8)

# SOUTH_RIGHT_START3 = (SOUTH_RIGHT_START[0] - 8, SOUTH_RIGHT_START[1])
# SOUTH_LEFT_START3 = (SOUTH_LEFT_START[0] + 8, SOUTH_LEFT_START[1])

# EAST_RIGHT_START3 = (EAST_RIGHT_START[0], EAST_RIGHT_START[1] + 8)
# EAST_LEFT_START3 = (EAST_LEFT_START[0], EAST_LEFT_START[1] - 8)

# NORTH_RIGHT_START3 = (NORTH_RIGHT_START[0] + 8, NORTH_RIGHT_START[1])
# NORTH_LEFT_START3 = (NORTH_LEFT_START[0] - 8, NORTH_LEFT_START[1])

# Create Nodes with offset to avoid overlapping
WEST_RIGHT2 = (WEST_RIGHT[0], WEST_RIGHT[1] - 4)
WEST_LEFT2 =	(WEST_LEFT[0], WEST_LEFT[1] + 4)

SOUTH_RIGHT2 = (SOUTH_RIGHT[0] - 4, SOUTH_RIGHT[1])
SOUTH_LEFT2 = (SOUTH_LEFT[0] + 4, SOUTH_LEFT[1])

EAST_RIGHT2 = (EAST_RIGHT[0], EAST_RIGHT[1] + 4)
EAST_LEFT2 = (EAST_LEFT[0], EAST_LEFT[1] - 4)

NORTH_RIGHT2 = (NORTH_RIGHT[0] + 4, NORTH_RIGHT[1])
NORTH_LEFT2 = (NORTH_LEFT[0] - 4, NORTH_LEFT[1])

# Create Nodes with offset to avoid overlapping
WEST_RIGHT3 = (WEST_RIGHT[0], WEST_RIGHT[1] - 8)
WEST_LEFT3 =	(WEST_LEFT[0], WEST_LEFT[1] + 8)

SOUTH_RIGHT3 = (SOUTH_RIGHT[0] - 8, SOUTH_RIGHT[1])
SOUTH_LEFT3 = (SOUTH_LEFT[0] + 8, SOUTH_LEFT[1])

EAST_RIGHT3 = (EAST_RIGHT[0], EAST_RIGHT[1] + 8)
EAST_LEFT3 = (EAST_LEFT[0], EAST_LEFT[1] - 8)

NORTH_RIGHT3 = (NORTH_RIGHT[0] + 8, NORTH_RIGHT[1])
NORTH_LEFT3 = (NORTH_LEFT[0] - 8, NORTH_LEFT[1])

# Roads
WEST_INBOUND = (WEST_RIGHT_START, WEST_RIGHT)
SOUTH_INBOUND = (SOUTH_RIGHT_START, SOUTH_RIGHT)
EAST_INBOUND = (EAST_RIGHT_START, EAST_RIGHT)
NORTH_INBOUND = (NORTH_RIGHT_START, NORTH_RIGHT)

WEST_OUTBOUND = (WEST_LEFT, WEST_LEFT_START)
SOUTH_OUTBOUND = (SOUTH_LEFT, SOUTH_LEFT_START)
EAST_OUTBOUND = (EAST_LEFT, EAST_LEFT_START)
NORTH_OUTBOUND = (NORTH_LEFT, NORTH_LEFT_START)

WEST_STRAIGHT = (WEST_RIGHT, EAST_LEFT)
SOUTH_STRAIGHT = (SOUTH_RIGHT, NORTH_LEFT)
EAST_STRAIGHT = (EAST_RIGHT, WEST_LEFT)
NORTH_STRAIGHT = (NORTH_RIGHT, SOUTH_LEFT)

WEST_RIGHT_TURN = turn_road(WEST_RIGHT, SOUTH_LEFT, TURN_RIGHT, n)
WEST_LEFT_TURN = turn_road(WEST_RIGHT, NORTH_LEFT, TURN_LEFT, n)

SOUTH_RIGHT_TURN = turn_road(SOUTH_RIGHT, EAST_LEFT, TURN_RIGHT, n)
SOUTH_LEFT_TURN = turn_road(SOUTH_RIGHT, WEST_LEFT, TURN_LEFT, n)

EAST_RIGHT_TURN = turn_road(EAST_RIGHT, NORTH_LEFT, TURN_RIGHT, n)
EAST_LEFT_TURN = turn_road(EAST_RIGHT, SOUTH_LEFT, TURN_LEFT, n)

NORTH_RIGHT_TURN = turn_road(NORTH_RIGHT, WEST_LEFT, TURN_RIGHT, n)
NORTH_LEFT_TURN = turn_road(NORTH_RIGHT, EAST_LEFT, TURN_LEFT, n)

# Create Roads
WEST_INBOUND2 = (WEST_RIGHT_START2, WEST_RIGHT2)
SOUTH_INBOUND2 = (SOUTH_RIGHT_START2, SOUTH_RIGHT2)
EAST_INBOUND2 = (EAST_RIGHT_START2, EAST_RIGHT2)
NORTH_INBOUND2 = (NORTH_RIGHT_START2, NORTH_RIGHT2)

WEST_OUTBOUND2 = (WEST_LEFT2, WEST_LEFT_START2)
SOUTH_OUTBOUND2 = (SOUTH_LEFT2, SOUTH_LEFT_START2)
EAST_OUTBOUND2 = (EAST_LEFT2, EAST_LEFT_START2)
NORTH_OUTBOUND2 = (NORTH_LEFT2, NORTH_LEFT_START2)

WEST_STRAIGHT2 = (WEST_RIGHT2, EAST_LEFT2)
SOUTH_STRAIGHT2 = (SOUTH_RIGHT2, NORTH_LEFT2)
EAST_STRAIGHT2 = (EAST_RIGHT2, WEST_LEFT2)
NORTH_STRAIGHT2 = (NORTH_RIGHT2, SOUTH_LEFT2)

WEST_RIGHT_TURN2 = turn_road(WEST_RIGHT2, SOUTH_LEFT2, TURN_RIGHT, n)
WEST_LEFT_TURN2 = turn_road(WEST_RIGHT2, NORTH_LEFT2, TURN_LEFT, n)

SOUTH_RIGHT_TURN2 = turn_road(SOUTH_RIGHT2, EAST_LEFT2, TURN_RIGHT, n)
SOUTH_LEFT_TURN2 = turn_road(SOUTH_RIGHT2, WEST_LEFT2, TURN_LEFT, n)

EAST_RIGHT_TURN2 = turn_road(EAST_RIGHT2, NORTH_LEFT2, TURN_RIGHT, n)
EAST_LEFT_TURN2 = turn_road(EAST_RIGHT2, SOUTH_LEFT2, TURN_LEFT, n)

NORTH_RIGHT_TURN2 = turn_road(NORTH_RIGHT2, WEST_LEFT2, TURN_RIGHT, n)
NORTH_LEFT_TURN2 = turn_road(NORTH_RIGHT2, EAST_LEFT2, TURN_LEFT, n)

# Create Roads
# WEST_INBOUND3 = (WEST_RIGHT_START3, WEST_RIGHT3)
# SOUTH_INBOUND3 = (SOUTH_RIGHT_START3, SOUTH_RIGHT3)
# EAST_INBOUND3 = (EAST_RIGHT_START3, EAST_RIGHT3)
# NORTH_INBOUND3 = (NORTH_RIGHT_START3, NORTH_RIGHT3)

# WEST_OUTBOUND3 = (WEST_LEFT3, WEST_LEFT_START3)
# SOUTH_OUTBOUND3 = (SOUTH_LEFT3, SOUTH_LEFT_START3)
# EAST_OUTBOUND3 = (EAST_LEFT3, EAST_LEFT_START3)
# NORTH_OUTBOUND3 = (NORTH_LEFT3, NORTH_LEFT_START3)

# WEST_STRAIGHT3 = (WEST_RIGHT3, EAST_LEFT3)
# SOUTH_STRAIGHT3 = (SOUTH_RIGHT3, NORTH_LEFT3)
# EAST_STRAIGHT3 = (EAST_RIGHT3, WEST_LEFT3)
# NORTH_STRAIGHT3 = (NORTH_RIGHT3, SOUTH_LEFT3)

# WEST_RIGHT_TURN3 = turn_road(WEST_RIGHT3, SOUTH_LEFT3, TURN_RIGHT, n)
# WEST_LEFT_TURN3 = turn_road(WEST_RIGHT3, NORTH_LEFT3, TURN_LEFT, n)

# SOUTH_RIGHT_TURN3 = turn_road(SOUTH_RIGHT3, EAST_LEFT3, TURN_RIGHT, n)
# SOUTH_LEFT_TURN3 = turn_road(SOUTH_RIGHT3, WEST_LEFT3, TURN_LEFT, n)

# EAST_RIGHT_TURN3 = turn_road(EAST_RIGHT3, NORTH_LEFT3, TURN_RIGHT, n)
# EAST_LEFT_TURN3 = turn_road(EAST_RIGHT3, SOUTH_LEFT3, TURN_LEFT, n)

# NORTH_RIGHT_TURN3 = turn_road(NORTH_RIGHT3, WEST_LEFT3, TURN_RIGHT, n)
# NORTH_LEFT_TURN3 = turn_road(NORTH_RIGHT3, EAST_LEFT3, TURN_LEFT, n)

sim.create_roads([
    WEST_INBOUND,   #0
    SOUTH_INBOUND,  #1
    EAST_INBOUND,   #2
    NORTH_INBOUND,  #3

    WEST_OUTBOUND,  #4
    SOUTH_OUTBOUND, #5
    EAST_OUTBOUND,  #6
    NORTH_OUTBOUND, #7

    WEST_STRAIGHT,  #8
    SOUTH_STRAIGHT, #9
    EAST_STRAIGHT,  #10
    NORTH_STRAIGHT, #11

    # NEW ROADS ----------------------------------------------
    WEST_INBOUND2,  #12
    SOUTH_INBOUND2, #13
    EAST_INBOUND2,  #14
    NORTH_INBOUND2, #15

    WEST_OUTBOUND2, #16
    SOUTH_OUTBOUND2, #17
    EAST_OUTBOUND2, #18
    NORTH_OUTBOUND2, #19

    WEST_STRAIGHT2, #20
    SOUTH_STRAIGHT2, #21
    EAST_STRAIGHT2, #22
    NORTH_STRAIGHT2, #23
    #----------------------------------------------------------------

    # WEST_INBOUND3,  #24
    # SOUTH_INBOUND3, #25
    # EAST_INBOUND3,  #26
    # NORTH_INBOUND3, #27

    # WEST_OUTBOUND3, #28
    # SOUTH_OUTBOUND3, #29
    # EAST_OUTBOUND3, #30
    # NORTH_OUTBOUND3, #31

    # WEST_STRAIGHT3, #32
    # SOUTH_STRAIGHT3, #33
    # EAST_STRAIGHT3, #34
    # NORTH_STRAIGHT3, #35

    *WEST_RIGHT_TURN,
    *WEST_LEFT_TURN,

    *SOUTH_RIGHT_TURN,
    *SOUTH_LEFT_TURN,

    *EAST_RIGHT_TURN,
    *EAST_LEFT_TURN,

    *NORTH_RIGHT_TURN,
    *NORTH_LEFT_TURN,

    *WEST_RIGHT_TURN2,
    *WEST_LEFT_TURN2,
    
    *SOUTH_RIGHT_TURN2,
    *SOUTH_LEFT_TURN2,

    *EAST_RIGHT_TURN2,
    *EAST_LEFT_TURN2,

    *NORTH_RIGHT_TURN2,
    *NORTH_LEFT_TURN2,

    # *WEST_RIGHT_TURN3,
    # *WEST_LEFT_TURN3,

    # *SOUTH_RIGHT_TURN3,
    # *SOUTH_LEFT_TURN3,

    # *EAST_RIGHT_TURN3,
    # *EAST_LEFT_TURN3,

    # *NORTH_RIGHT_TURN3,
    # *NORTH_LEFT_TURN3
])

def road(a): return range(a, a+n)

sim.create_gen({
'vehicle_rate': VEHICLE_RATE,
'vehicles':[
    # 1st Lane
    [2, {'path': [0, 8, 6]}],
    [2, {'path': [0, *road(NUM_OF_ROADS), 5]}],
    # [2, {'path': [0, *road(24+n), 7]}],

    [2, {'path': [1, 9, 7]}],
    [2, {'path': [1, *road(NUM_OF_ROADS+2*n), 6]}],
    # [1, {'path': [1, *road(24+3*n), 4]}],

    [3, {'path': [2, 10, 4]}],
    [3, {'path': [2, *road(NUM_OF_ROADS+4*n), 7]}],
    # [1, {'path': [2, *road(24+5*n), 5]}],

    [3, {'path': [3, 11, 5]}],
    [3, {'path': [3, *road(NUM_OF_ROADS+6*n), 4]}],
    # [2, {'path': [3, *road(24+7*n), 6]}],

    # 2nd Lane
    [2, {'path': [12, 20, 18]}],
    # [2, {'path': [12, *road(24+8*n), 17]}],
    [2, {'path': [12, *road(NUM_OF_ROADS+9*n), 19]}],

    [2, {'path': [13, 21, 19]}],
    # [2, {'path': [13, *road(24+10*n), 18]}],
    [2, {'path': [13, *road(NUM_OF_ROADS+11*n), 16]}],

    [3, {'path': [14, 22, 16]}],
    # [2, {'path': [14, *road(24+12*n), 19]}],
    [3, {'path': [14, *road(NUM_OF_ROADS+13*n), 17]}],

    [3, {'path': [15, 23, 17]}],
    # [2, {'path': [15, *road(24+14*n), 16]}],
    [3, {'path': [15, *road(NUM_OF_ROADS+15*n), 18]}],


    # # 3rd Lane (no red light/turn left only)
    # # [3, {'path': [24, 32, 30]}],
    # # [2, {'path': [24, *road(NUM_OF_ROADS+16*n), 29]}],
    # [3, {'path': [24, *road(NUM_OF_ROADS+17*n), 31]}],

    # # [3, {'path': [25, 33, 31]}],
    # # [2, {'path': [25, *road(NUM_OF_ROADS+18*n), 30]}],
    # [3, {'path': [25, *road(NUM_OF_ROADS+19*n), 28]}],

    # # [3, {'path': [26, 34, 28]}],
    # # [2, {'path': [26, *road(NUM_OF_ROADS+20*n), 31]}],
    # [4, {'path': [26, *road(NUM_OF_ROADS+21*n), 29]}],

    # # [3, {'path': [27, 35, 29]}],
    # # [2, {'path': [27, *road(NUM_OF_ROADS+22*n), 28]}],
    # [4, {'path': [27, *road(NUM_OF_ROADS+23*n), 30]}]

]})

sim.create_signal([[0], [1], [2], [3]])
sim.create_signal([[12], [13], [14], [15]])

# Create Green Light for 3rd Lane
# sim.create_signal([[24]])
# sim.create_signal([[25]])
# sim.create_signal([[26]])
# sim.create_signal([[27]])

# Start simulation
win = Window(sim)
win.zoom = 10
if(sim.isPaused == False):
    win.run(steps_per_update=STEPS_PER_UPDATE)
