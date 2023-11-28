import sys
import os
import platform
import psutil


class CODE:
    HEADER = "\033[95m"
    BLUE = "\033[94m"
    CYAN = "\033[96m"
    GREEN = "\033[92m"
    MAGENTA = "\033[35m"
    YELLOW = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


class SystemInformation:

    @classmethod
    def displaySystemInfo(cls):

        print(
            f"{CODE.YELLOW}################################### System Information #####################################################\n"
        )

        print(
            f"\t\t\t\t\tBy Salim Dason\n\t\t\t\tEmail: salimdason@outlook.com\n\n"
        )

        try:
            print(f"\t\tOS: {platform.system()}\t\t\t\t", end=" ")
            print(f"Machine Architecture: {platform.machine()}")
            print(f"\n\t\tPhysical Cores: {psutil.cpu_count(logical=False)}\t\t\t", end=" ")
            print(f"Logical Cores: {psutil.cpu_count(logical=True)}")
            print(f"\n\t\tUser: {os.getlogin()}\t\t\t\t", end=" ")
            print(f"Python Version: {platform.python_version()}\n{CODE.ENDC}")
        except:
            print(f"Could Not Retrieve System Information\n{CODE.ENDC}")

        print(f"{CODE.FAIL}\t\t\t\t\tDisclaimer:\n\n\tThis tool is provided as-is, without any warranty or guarantee of any kind.\n\tThe author is not responsible for any damage or loss resulting from the use of this script.")

        print(
            f"\n\n{CODE.YELLOW}################################### System Information #####################################################{CODE.ENDC}"
        )

        return " "
