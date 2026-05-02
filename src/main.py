import argparse
from drone.logger import setup_logger
from drone.connection import connect_vehicle
from drone.controller import DroneController
from drone.mission import takeoff, hover, land
from config import *

logger = setup_logger()
logger.info("Mission Started")

parser = argparse.ArgumentParser()
parser.add_argument('--connect', default='/dev/ttyACM0')
args = parser.parse_args()

# Connect to the vehicle
vehicle = connect_vehicle(args.connect)

# Initialize the High-Level Controller
drone = DroneController(vehicle)

try:
    takeoff(drone, TARGET_ALTITUDE)
    hover(drone, TARGET_ALTITUDE, HOVER_TIME)
    land(drone)

except KeyboardInterrupt:
    logger.warning("Mission interrupted by user.")
    land(drone)
except Exception as e:
    logger.error(f"Critical error: {e}")
    land(drone)