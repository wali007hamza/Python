import wmi, sys

c = wmi.WMI()
# All the methods and properties that you want to access are here
# https://msdn.microsoft.com/en-us/library/aa394239(v=vs.85).aspx
value = c.Win32_OperatingSystem()[0].BuildNumber
print(value)
value = c.Win32_OperatingSystem()[0].Manufacturer
print(value)
value = c.Win32_OperatingSystem()[0].OSArchitecture
print(value)
value = c.Win32_OperatingSystem()[0].OSType
print(value)
