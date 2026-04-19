import subprocess


def eww_open(barName):
    subprocess.call(["eww", "open", barName])


def battery_info(info):
    batery_info_path = "/sys/class/power_supply/BAT1/"

    output = subprocess.check_output(["cat", batery_info_path + info])

    output_str = output.decode()

    return output_str.strip()


def battery_icon():
    icon = " "
    status = battery_info("status")
    if status == "Charging":
        icon += " "

    charge = int(battery_info("capacity"))

    if charge > 80:
        icon += "  "
    elif charge > 70:
        icon += "  "
    elif charge > 50:
        icon += "  "
    elif charge > 20:
        icon += "  "
    else:
        icon += "  "

    return icon


def execute_command(command):
    output = subprocess.check_output(command, shell=True)
    return output.decode().strip()


def get_graphics_mode():
    """Get current graphics mode from envycontrol"""
    try:
        output = subprocess.check_output(
            ["envycontrol", "-q"], stderr=subprocess.STDOUT
        )
        mode = output.decode().strip()

        return mode.capitalize() if mode else "Unknown"
        # Return a shortened version for display
        # if mode == "integrated":
        #     return "Integrated"
        # elif mode == "hybrid":
        #     return "Hybrid"
        # elif mode == "nvidia":
        #     return "NVIDIA"
        # else:
        #     return mode.capitalize() if mode else "Unknown"
    except subprocess.CalledProcessError as e:
        return f"Error: {e.returncode}"
    except FileNotFoundError:
        return "Not Installed"
    except Exception as e:
        return f"Exception: {str(e)}"


def debug_widget():
    """Debug widget function"""
    try:
        result = get_graphics_mode()
        print(
            f"DEBUG: get_graphics_mode returned: {repr(result)}"
        )  # This won't be visible but helps us know it's called
        return f"[{result}]"
    except Exception as e:
        return f"ERR: {str(e)}"
