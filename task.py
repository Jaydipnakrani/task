import os
import subprocess
import platform
import socket
import psutil

def run_command(command):
    result = subprocess.run(command, stdout=subprocess.PIPE, text=True, shell=True)
    return result.stdout.strip()

def get_installed_software():
    command = "wmic product get name"
    return run_command(command)

def get_internet_speed():
   
    try:
        speed_command = "speedtest-cli --simple"
        return run_command(speed_command)
    except Exception as e:
        return str(e)

def get_screen_resolution():
    command = "wmic desktopmonitor get screenheight, screenwidth"
    return run_command(command)

def get_cpu_info():
    cpu_info = platform.processor()
    cpu_cores = psutil.cpu_count(logical=False)
    cpu_threads = psutil.cpu_count(logical=True)
    return cpu_info, cpu_cores, cpu_threads

def get_gpu_info():
   
    try:
        gpu_info_command = "nvidia-smi --query-gpu=name --format=csv,noheader"
        return run_command(gpu_info_command)
    except Exception as e:
        return str(e)

def get_ram_size():
    ram_info = psutil.virtual_memory()
    return ram_info.total / (1024 ** 3)  

def get_screen_size():
    screen_size_command = "wmic desktopmonitor get screensize"
    return run_command(screen_size_command)

def get_mac_address():
    mac_address = ""
    for interface, addrs in psutil.net_if_addrs().items():
        for addr in addrs:
            if addr.family == socket.AF_INET:
                mac_address = addr.address
    return mac_address

def get_public_ip():
    try:
        ip_address = socket.gethostbyname(socket.gethostname())
        return ip_address
    except socket.gaierror:
        return "Not available"

def get_windows_version():
    return platform.system() + " " + platform.version()


def gather_system_info():
    installed_software = get_installed_software()
    internet_speed = get_internet_speed()
    screen_resolution = get_screen_resolution()
    cpu_model, cpu_cores, cpu_threads = get_cpu_info()
    gpu_model = get_gpu_info()
    ram_size = get_ram_size()
    screen_size = get_screen_size()
    mac_address = get_mac_address()
    public_ip = get_public_ip()
    windows_version = get_windows_version()

    return {
        "Installed Software": installed_software,
        "Internet Speed": internet_speed,
        "Screen Resolution": screen_resolution,
        "CPU Model": cpu_model,
        "CPU Cores": cpu_cores,
        "CPU Threads": cpu_threads,
        "GPU Model": gpu_model,
        "RAM Size (GB)": ram_size,
        "Screen Size": screen_size,
        "MAC Address": mac_address,
        "Public IP": public_ip,
        "Windows Version": windows_version
    }

if __name__ == "__main__":
    system_info = gather_system_info()

    for key, value in system_info.items():
        print(f"{key}: {value}")

