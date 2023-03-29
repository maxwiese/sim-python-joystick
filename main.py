import vgamepad as vg
import serial


SERIAL_PORT = "COM1"
SERIAL_BAUD = 9600

gamepad = vg.VX360Gamepad()
connection = serial.Serial(SERIAL_PORT, SERIAL_BAUD, timeout=1)
try:
    while True:
        value = int(connection.readline().decode().strip())
        gamepad.right_trigger_float(value_float=value)
        gamepad.update()

except KeyboardInterrupt:
    gamepad.reset()
    connection.close()