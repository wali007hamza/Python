import re, sys
from win32api import HIWORD, LOWORD, GetFileVersionInfo

def get_version_number(filename):
    try:
        info = GetFileVersionInfo(filename, "\\")
        ms = info['FileVersionMS']
        ls = info['FileVersionMS']
        return HIWORD(ms), LOWORD(ms), HIWORD(ls), LOWORD(ms)
    except Exception as ex:
        print(ex)
        return "Unknow Version"

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        filePath = sys.argv[1]
        filePath = re.sub(r"\\", r"\\\\", filePath)
        result = get_version_number(filePath)
        version = ".".join([str(i) for i in result])
        print("Version for the file {filename} is {version}".format(filename=filePath, version=version))
