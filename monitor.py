import sys
import psutil


# ##### Operating system name ############################
def sysname():
    name = sys.platform
    if name == "win32":
        name_result = "Windows"
        return f"Your platform is {name_result}"
    elif name == "linux":
        name_result = "Linux"
        return f"Your platform is {name_result}"
    elif name == "cygwin":
        name_result = "Windows/Cygwin"
        return f"Your platform is {name_result}"
    elif name == "darwin":
        name_result = "Mac OS X"
        return f"Your platform is {name_result}"
    else:
        return "Unknown OS"


# ### Sensors ##########################################
def secs2hours(secs):
    mm, ss = divmod(secs, 60)
    hh, mm = divmod(mm, 60)
    return "%d:%02d:%02d" % (hh, mm, ss)


def temper():
    if not hasattr(psutil, "sensors_battery"):
        sysansw = "platform not supported"
        return sysansw

    batt = psutil.sensors_battery()
    if batt is None:
        sysansw = "no battery is installed"
        return sysansw

    if batt.power_plugged:
        batterystatus = str("Battery: is ok, ")
        batterycharge = str("charge: %s%%" % round(batt.percent, 2))
        batterystatus += str(" Status: %s" % (
            "charging" if batt.percent < 100 else "fully charged"))
        batteryplug = str("plugged in: yes")
    else:
        batterystatus = str("Battery: not charging")
        batterycharge = str("left: %s" % secs2hours(batt.secsleft))
        batterycharge += str("status: %s" % "discharging")
        batteryplug = str("plugged in: no")

    finstat = [batterystatus, batterycharge, batteryplug]

    return '\n'.join(finstat)

# Memory ##############################################################






