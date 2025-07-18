import subprocess
import datetime

log_file = "service_status.log"
services = ["wuauserv", "spooler", "BITS"]

with open(log_file, "a") as f:
    f.write(f"\n--- Service Status Logged at {datetime.datetime.now()} ----\n")
    for service in services:
        result = subprocess.run(["sc", "query", service], capture_output=True, text=True)
        if "RUNNING" in result.stdout:
            f.write(f"{service}: RUNNING\n")
        else:
            f.write(f"{service}: NOT RUNNING or NOT FOUND\n")

            print("service status logged to service_status.log")
    