import serial
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

SERIAL_PORT = '/dev/cu.usbmodem111201'
BAUD_RATE = 115200

# Open serial and immediately clear old junk data
ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
ser.reset_input_buffer()

powers = []


def update(i):
    try:
        # Read the most recent line
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8', errors='ignore').strip()
            if line:
                p, c, alert = map(float, line.split(','))

                powers.append(p)
                if len(powers) > 50: powers.pop(0)

                plt.cla()
                plt.plot(powers, label='Load (Watts)', color='#0047AB', linewidth=2)

                # Theft Detection Styling
                if alert == 1:
                    plt.title("⚠️ THEFT DETECTED: UNUSUAL LOAD SPIKE! ⚠️", color='red', weight='bold')
                    plt.gca().set_facecolor('#FFE5E5')  # Light red alert
                else:
                    plt.title("Smart Meter: Normal Consumption", color='#2E7D32')
                    plt.gca().set_facecolor('#F1F8E9')  # Clean green

                plt.ylabel("Power (W)")
                plt.ylim(-100, 4000)  # Keep scale stable to avoid "jumping"
                plt.grid(True, alpha=0.3)
                plt.legend(loc='upper left')
    except Exception as e:
        print(f"Syncing... {e}")


# Run at a slightly slower interval to match the Arduino's 200ms
ani = FuncAnimation(plt.gcf(), update, interval=200, cache_frame_data=False)
plt.tight_layout()
plt.show()