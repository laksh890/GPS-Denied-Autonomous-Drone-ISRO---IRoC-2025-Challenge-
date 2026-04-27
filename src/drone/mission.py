import time
from dronekit import VehicleMode
from config import *
from drone.rc import send_rc, constrain
from drone.failsafe import check_sensors, emergency_land
from controllers.pid import PIDController

def get_altitude(vehicle):
    return vehicle.rangefinder.distance


def get_drift(vehicle):
    x = getattr(vehicle, 'opt_m_x', 0.0)
    y = getattr(vehicle, 'opt_m_y', 0.0)
    return x, y


def takeoff(vehicle, alt_pid, x_pid, y_pid, target):
    print("Taking off...")

    vehicle.mode = VehicleMode("ALT_HOLD")
    vehicle.armed = True

    while not vehicle.armed:
        time.sleep(1)

    last = time.time()

    while True:
        if not check_sensors(vehicle):
            emergency_land(vehicle)
            return
        now = time.time()
        dt = now - last
        last = now

        alt = get_altitude(vehicle)
        x, y = get_drift(vehicle)

        throttle = BASE_THROTTLE + alt_pid.compute(target, alt, dt)
        roll = PWM_CENTER + x_pid.compute(0, x, dt)
        pitch = PWM_CENTER + y_pid.compute(0, y, dt)

        throttle = constrain(int(throttle), 1300, MAX_THROTTLE)
        roll = constrain(int(roll), PWM_MIN, PWM_MAX)
        pitch = constrain(int(pitch), PWM_MIN, PWM_MAX)

        send_rc(vehicle, roll, pitch, throttle)

        print(f"ALT={alt:.2f}")

        if alt >= target - 0.05:
            break

        time.sleep(0.1)


def hover(vehicle, alt_pid, x_pid, y_pid, target, duration):
    print("Hovering...")

    start = time.time()
    last = start

    while time.time() - start < duration:
        if not check_sensors(vehicle):
            emergency_land(vehicle)
            return
        now = time.time()
        dt = now - last
        last = now

        alt = get_altitude(vehicle)
        x, y = get_drift(vehicle)

        throttle = BASE_THROTTLE + alt_pid.compute(target, alt, dt)
        roll = PWM_CENTER + x_pid.compute(0, x, dt)
        pitch = PWM_CENTER + y_pid.compute(0, y, dt)

        send_rc(vehicle, int(roll), int(pitch), int(throttle))
        time.sleep(0.1)


# def land(vehicle, x_pid, y_pid):
#     print("Landing...")
#     vehicle.mode = VehicleMode("LAND")

def land(vehicle, x_pid, y_pid):
    print("Smart Landing Started")

    vehicle.mode = VehicleMode("ALT_HOLD")

    throttle = 1450

    while vehicle.rangefinder.distance > 0.15:
        if not check_sensors(vehicle):
            emergency_land(vehicle)
            return

        x = getattr(vehicle, 'opt_m_x', 0)
        y = getattr(vehicle, 'opt_m_y', 0)

        roll = 1500 + x_pid.compute(0, x, 0.1)
        pitch = 1500 + y_pid.compute(0, y, 0.1)

        throttle -= 3

        vehicle.channels.overrides = {
            '1': int(roll),
            '2': int(pitch),
            '3': int(throttle)
        }

        time.sleep(0.1)

    vehicle.armed = False
    vehicle.channels.overrides = {}
    print("Touchdown Complete")