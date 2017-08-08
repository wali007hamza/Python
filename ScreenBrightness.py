import wmi, sys

def GetScreenBrightness():
    c = wmi.WMI(namespace="wmi")
    brightness = c.WmiMonitorBrightness.CurrentBrightness
    return brightness.Value

if __name__ == "__main__":
    if (len(sys.argv) == 1) or (len(sys.argv) == 2 and sys.argv[1].lower() == "get"):
        print(GetScreenBrightness())
    if len(sys.argv) == 3 and sys.argv[1].lower() == "set":
        brightnessValue = int(sys.argv[2])
        print("Setting screen brightness to {}".format(brightnessValue))
