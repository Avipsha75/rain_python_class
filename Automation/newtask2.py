import os
import subprocess

# Function to gather system diagnostics
def generate_diagnostics_report():
    report = []

    # Current working directory
    cwd = os.getcwd()
    report.append(f"Current Working Directory: {cwd}")

    # Disk usage of the current directory using subprocess
    try:
        disk_usage = subprocess.check_output("dir", shell=True, text=True)
        report.append(f"Disk Usage (Current Directory):\n{disk_usage.strip()}")
    except subprocess.CalledProcessError as e:
        report.append(f"Error retrieving disk usage: {e}")

    # System information using subprocess
    try:
        os_version = subprocess.check_output("wmic os get caption", shell=True, text=True).strip().split("\n")[1]
        processor_info = subprocess.check_output("wmic cpu get name", shell=True, text=True).strip().split("\n")[1]
        memory_info_raw = subprocess.check_output("wmic memorychip get capacity", shell=True, text=True).strip().split("\n")[1:]

        # Filter out empty or invalid lines
        memory_info = [line.strip() for line in memory_info_raw if line.strip().isdigit()]
        total_memory = sum(int(mem) for mem in memory_info) / (1024**3)  # Convert bytes to GB

        report.append(f"System Information:\n"
                      f"OS: {os_version}\n"
                      f"Processor: {processor_info}\n"
                      f"Total Memory: {total_memory:.2f} GB")
    except subprocess.CalledProcessError as e:
        report.append(f"Error retrieving system information: {e}")

    return "\n\n".join(report)

# Save the report to a text file
def save_report_to_file(report, filename="system_diagnostics_report.txt"):
    with open(filename, 'w') as file:
        file.write(report)
    print(f"Report saved to {filename}")

# Generate and save the report
report = generate_diagnostics_report()
save_report_to_file(report)

