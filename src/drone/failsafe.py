from dronekit import VehicleMode

def check_sensors(vehicle):
    try:
        alt = vehicle.rangefinder.distance

        if alt is None:
            return False

        if alt < 0 or alt > 20:
            return False

        return True

    except:
        return False


def emergency_land(vehicle):
    print("FAILSAFE TRIGGERED → LANDING")
    vehicle.mode = VehicleMode("LAND")