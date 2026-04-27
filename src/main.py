import argparse
from drone.logger import setup_logger
from controllers.pid import PIDController
from drone.connection import connect_vehicle
from drone.mission import takeoff, hover, land
from config import *

logger = setup_logger()
logger.info("Mission Started")
parser = argparse.ArgumentParser()
parser.add_argument('--connect', default='/dev/ttyACM0')
args = parser.parse_args()

vehicle = connect_vehicle(args.connect)

alt_pid = PIDController(ALT_KP, ALT_KI, ALT_KD)
x_pid = PIDController(XY_KP, XY_KI, XY_KD)
y_pid = PIDController(XY_KP, XY_KI, XY_KD)

try:
    takeoff(vehicle, alt_pid, x_pid, y_pid, TARGET_ALTITUDE)
    hover(vehicle, alt_pid, x_pid, y_pid, TARGET_ALTITUDE, HOVER_TIME)
    land(vehicle, x_pid, y_pid)

except KeyboardInterrupt:
    land(vehicle, x_pid, y_pid)