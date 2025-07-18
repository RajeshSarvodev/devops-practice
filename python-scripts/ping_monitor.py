import subprocess
import platform
import datetime

log_file = "ping_monitor.log"
hosts = ["8.8.8.8", "google.com", "github.com"]

# Determine the ping parameter for the platform
param = "-n" if platform.system().lower() == "windows" else "-c"

with open(log_file, "a") as f:
    f.write(f"\n--- Ping Status Logged at {datetime.datetime.now()} ---\n")
    for host in hosts:
        try:
            result = subprocess.run(["ping", param, "2", host], capture_output=True, text=True)
            if result.returncode == 0:
                f.write(f"{host}: REACHABLE\n")
            else:
                f.write(f"{host}: UNREACHABLE\n")
        except Exception as e:
            f.write(f"{host}: ERROR - {str(e)}\n")

print("Ping results written to ping_monitor.log")
