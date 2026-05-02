import time
from dronekit import VehicleMode
from controllers.pid import PIDController
from drone.rc import send_rc, constrain
from drone.failsafe import check_sensors, emergency_land
from config import *

class DroneController:
    """
    High-level controller for GPS-denied autonomous drone flight.
    Encapsulates vehicle connection, sensor data, and PID control loops.
    """
    def __init__(self, vehicle):
        self.vehicle = vehicle
        
        # Initialize PID Controllers
        self.alt_pid = PIDController(ALT_KP, ALT_KI, ALT_KD)
        self.x_pid = PIDController(XY_KP, XY_KI, XY_KD)
        self.y_pid = PIDController(XY_KP, XY_KI, XY_KD)
        
        self.last_time = time.time()

    def get_altitude(self):
        """Returns distance from rangefinder/LiDAR."""
        return self.vehicle.rangefinder.distance

    def get_drift(self):
        """Returns optical flow drift values."""
        x = getattr(self.vehicle, 'opt_m_x', 0.0)
        y = getattr(self.vehicle, 'opt_m_y', 0.0)
        return x, y

    def update_control(self, target_alt, target_x=0.0, target_y=0.0):
        """
        Computes and sends RC overrides based on PID output.
        """
        if not check_sensors(self.vehicle):
            emergency_land(self.vehicle)
            return False

        now = time.time()
        dt = now - self.last_time
        if dt <= 0:
            dt = 0.1
        self.last_time = now

        alt = self.get_altitude()
        x, y = self.get_drift()

        # PID Computations
        throttle_adj = self.alt_pid.compute(target_alt, alt, dt)
        roll_adj = self.x_pid.compute(target_x, x, dt)
        pitch_adj = self.y_pid.compute(target_y, y, dt)

        # Map to PWM
        throttle = BASE_THROTTLE + throttle_adj
        roll = PWM_CENTER + roll_adj
        pitch = PWM_CENTER + pitch_adj

        # Constrain and Send
        throttle = constrain(int(throttle), 1000, MAX_THROTTLE)
        roll = constrain(int(roll), PWM_MIN, PWM_MAX)
        pitch = constrain(int(pitch), PWM_MIN, PWM_MAX)

        send_rc(self.vehicle, roll, pitch, throttle)
        return True

    def set_mode(self, mode_name):
        """Sets the vehicle flight mode."""
        self.vehicle.mode = VehicleMode(mode_name)

    def arm(self):
        """Arms the vehicle and waits for confirmation."""
        print("Arming motors...")
        self.vehicle.armed = True
        while not self.vehicle.armed:
            time.sleep(1)
        print("Armed!")

    def disarm(self):
        """Disarms the vehicle."""
        print("Disarming...")
        self.vehicle.armed = False
        self.vehicle.channels.overrides = {}
