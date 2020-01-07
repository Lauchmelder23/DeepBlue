import datetime

path = "logs/log.txt"
cleanup = open(path, "w+") 
cleanup.close()

def log(msg, log_type, mute):
    log = f"[{datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S')}] [{log_type.upper()}] {msg}"
    log_file = open(path, "a")
    log_file.write(log + "\n")
    log_file.close()
    if mute == False:
        print(log)

def info(msg, mute=False):
    log(msg, "info", mute)

def warning(msg, mute=False):
    log(msg, "warning", mute)

def error(msg, mute=False):
    log(msg, "error", mute)
