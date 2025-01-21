import subprocess

def list_processes():
    result = subprocess.run(["ps", "aux"], capture_output=True, text=True)  # Use "tasklist" for Windows
    with open("processes.txt", "w") as file:
        file.write(result.stdout)
    print("Processes saved to processes.txt")

def monitor_usage():
    result = subprocess.run(["top", "-b", "-n", "1"], capture_output=True, text=True)  # Use "wmic cpu get loadpercentage" for Windows
    with open("usage.txt", "w") as file:
        file.write(result.stdout)
    print("System usage saved to usage.txt")

list_processes()
monitor_usage()
