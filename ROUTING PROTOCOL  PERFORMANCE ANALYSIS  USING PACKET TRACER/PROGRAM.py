

# Title : Routing Protocol Performance Analysis using Packet Tracer
# Tool : Python 3.8+ with Matplotlib and Pandas

import pandas as pd
import matplotlib.pyplot as plt
import os

# Step 1: Define the filename for data storage
filename = "routing_performance.csv"

# Step 2: Check if CSV exists, else create it with default data
if not os.path.exists(filename):
    print("CSV file not found. Creating a new one with default data...\n")
    with open(filename, "w") as f:
        f.write("Protocol,Delay(ms),Throughput(kbps),PacketLoss(%)\n")
        f.write("RIP,20,180,2.0\n")
        f.write("OSPF,12,250,1.0\n")
        f.write("EIGRP,10,300,0.5\n")

# Step 3: Load the routing protocol performance data
data = pd.read_csv(filename)
print("Routing Protocol Performance Data:\n")
print(data, "\n")

# Step 4: Print summary results
best_throughput = data.loc[data["Throughput(kbps)"].idxmax(), "Protocol"]
lowest_delay = data.loc[data["Delay(ms)"].idxmin(), "Protocol"]
lowest_loss = data.loc[data["PacketLoss(%)"].idxmin(), "Protocol"]

print("Highest Throughput :", best_throughput)
print("Lowest Delay :", lowest_delay)
print("Minimum Packet Loss:", lowest_loss, "\n")

# Step 5: Visualize performance metrics using bar charts
plt.figure(figsize=(12, 5))

plt.subplot(1, 3, 1)
plt.bar(data["Protocol"], data["Delay(ms)"], color="skyblue", edgecolor="black")
plt.title("Average Delay (ms)")
plt.xlabel("Routing Protocol")
plt.ylabel("Delay (ms)")

plt.subplot(1, 3, 2)
plt.bar(data["Protocol"], data["Throughput(kbps)"], color="lightgreen", edgecolor="black")
plt.title("Throughput (kbps)")
plt.xlabel("Routing Protocol")
plt.ylabel("Throughput (kbps)")

plt.subplot(1, 3, 3)
plt.bar(data["Protocol"], data["PacketLoss(%)"], color="salmon", edgecolor="black")
plt.title("Packet Loss (%)")
plt.xlabel("Routing Protocol")
plt.ylabel("Packet Loss (%)")

plt.suptitle("Routing Protocol Performance Comparison", fontsize=14, fontweight='bold')
plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()

# Step 6: Display overall performance observation
print("Performance Observation Summary")
print(f"RIP : Simple configuration, slower convergence, higher delay.")
print(f"OSPF : Balanced performance with moderate delay and high stability.")
print(f"EIGRP : Fastest convergence, least delay, and highest throughput.\n")
print("Conclusion: EIGRP provides the best overall performance among the three.")

