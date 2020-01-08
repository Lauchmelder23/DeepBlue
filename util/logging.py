'''
Provides some simple logging utility
'''
import datetime

path = "logs/log.txt"
cleanup = open(path, "w+") 
cleanup.close()

# Format: [DD.MM.YYYY HH:MM:SS] [<TYPE>] MESSAGE
def log(msg: str, log_type: str, mute: bool):
    log = f"[{datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S')}] [{log_type.upper()}] {msg}"
    log_file = open(path, "a")
    log_file.write(log + "\n")
    log_file.close()
    if mute == False:
        print(log)

def info(msg: str, mute: bool=False):
    log(msg, "info", mute)

def warning(msg: str, mute: bool=False):
    log(msg, "warning", mute)

def error(msg: str, mute: bool=False):
    log(msg, "error", mute)
