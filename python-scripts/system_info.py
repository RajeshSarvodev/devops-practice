import platform
import psutil
import datetime

log_file = "system_info.log"

with open(log_file, "a") as f:
    f.write(f"\n---- System Info Logged at {datetime.datetime.now()} -----\n")
    f.write(f"Platform: {platform.system()}\n")
    f.write(f"Platform Release: {platform.release()}\n")
    f.write(f"Platform Version: {platform.version()}\n")
    f.write(f"Processor Cores: {psutil.cpu_count(logical=True)}\n")
    f.write(f"Total RAM: {psutil.virtual_memory().total / (1024 ** 3):.2f} GB\n")
