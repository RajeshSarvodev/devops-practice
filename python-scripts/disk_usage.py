import shutil
import datetime

log_file = "disk_usage.log"

total, used, free = shutil.disk_usage("c:\\")

with open(log_file, "a") as f:
    f.write(f"\n--- Disk Info Logged at {datetime.datetime.now()}---\n")
    f.write(f"Total: {total // (2**30)} GB\n")
    f.write(f"Used: {used // (2**30)} GB\n")
    f.write(f"Free: {free // (2**30)} GB\n")

    print("Drink usage logged to disk_usage.log")