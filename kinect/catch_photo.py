import os, subprocess, base64


def take_photo():
    try:
        if os.path.exists("screenshot.jpg"):
            os.remove('screenshot.jpg')

        filepath="run.bat"
        p = subprocess.Popen(filepath, shell=True, stdout = subprocess.PIPE)

        stdout, stderr = p.communicate()

        if p.returncode == 0:
            return True
        
        return False
    except:
        return False
