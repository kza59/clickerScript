# clickerScript
a simple and useful script in python that clicks somewhere on the screen, waits a little, and then alt f4s. You can compile this script into an exe and then add it to task scheduler in order to log on for your daily rewards in a computer game automatically.

## Cloning the directory:
1. Make some directory in a place of your choosing
2. Navigate to the directory in the terminal
3. Copy the https : https://github.com/kza59/clickerScript.git
4. In terminal, git clone https://github.com/kza59/clickerScript.git
5. cd clickerScript


## How to Use
1. Install python
2. Install pipInstaller @ <https://pyinstaller.org/en/stable/>
3. Configure the config.py file to your liking, specify where on the screen to click, what process to run, etc. (There is a python program called positionFinder.py given to find where on the screen you want to click)
4. pyinstaller autoScript.py
5. The exe file should now be in dist.
6. Go to task scheduler, and schedule the exe as a daily task so that you can automatically log on to get your daily rewards
