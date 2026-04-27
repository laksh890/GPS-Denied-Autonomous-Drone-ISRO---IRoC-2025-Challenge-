from dronekit import connect

def connect_vehicle(port):
    print(f"Connecting to vehicle on {port}")
    return connect(port, baud=921600, wait_ready=True)