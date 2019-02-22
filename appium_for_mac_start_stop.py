
import subprocess
subprocess.call(['open', 'AppiumForMac.app']) # start
subprocess.call(['osascript', '-e', 'quit app "AppiumForMac.app"']) # stop