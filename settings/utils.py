import subprocess


def eww_open(barName):
    subprocess.call(["eww","open", barName])
