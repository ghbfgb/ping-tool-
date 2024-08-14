import subprocess
import pyfiglet
text = pyfiglet.figlet_format("sahan")
print(text)
print("enter an ip address")
i = input()
subprocess.call("ping "+ i,shell=True)

