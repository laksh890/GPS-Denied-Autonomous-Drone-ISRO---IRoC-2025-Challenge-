def constrain(value, low, high):
    return max(low, min(high, value))


def send_rc(vehicle, roll, pitch, throttle):
    vehicle.channels.overrides = {
        '1': roll,
        '2': pitch,
        '3': throttle
    }