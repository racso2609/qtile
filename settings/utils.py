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
