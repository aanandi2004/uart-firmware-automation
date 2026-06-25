import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.figure(figsize=(8,5))

def animate(i):
    data = pd.read_csv("live_log.csv")

    plt.cla()

    plt.plot(data["Distance(cm)"], linewidth=2)

    plt.title("Live Distance Monitoring")
    plt.xlabel("Sample Number")
    plt.ylabel("Distance (cm)")
    plt.grid(True)

ani = FuncAnimation(plt.gcf(), animate, interval=1000)

plt.tight_layout()
plt.show()