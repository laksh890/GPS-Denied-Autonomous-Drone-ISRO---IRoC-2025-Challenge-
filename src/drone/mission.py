import time
from config import *

def takeoff(controller, target_alt):
    print(f"Taking off to {target_alt}m...")
    controller.set_mode("ALT_HOLD")
    controller.arm()

    while True:
        if not controller.update_control(target_alt):
            break
        
        alt = controller.get_altitude()
        print(f"Alt: {alt:.2f}m")
        
        if alt >= target_alt - 0.05:
            print("Target altitude reached.")
            break
        time.sleep(0.1)

def hover(controller, target_alt, duration):
    print(f"Hovering for {duration} seconds...")
    start_time = time.time()
    while time.time() - start_time < duration:
        if not controller.update_control(target_alt):
            break
        time.sleep(0.1)

def land(controller):
    print("Initiating smart landing...")
    controller.set_mode("ALT_HOLD")
    
    current_throttle = BASE_THROTTLE
    while controller.get_altitude() > 0.15:
        # Gradually reduce throttle while maintaining horizontal stability
        current_throttle -= 2
        
        # Manually update control with decreasing throttle for soft landing
        # (This could be integrated into update_control if needed)
        x, y = controller.get_drift()
        roll = PWM_CENTER + controller.x_pid.compute(0, x, 0.1)
        pitch = PWM_CENTER + controller.y_pid.compute(0, y, 0.1)
        
        controller.vehicle.channels.overrides = {
            '1': int(roll),
            '2': int(pitch),
            '3': int(current_throttle)
        }
        time.sleep(0.1)

    controller.disarm()
    print("Landing complete.")