from datetime import datetime


# Prints the log with the time inside the console and also writes the log inside the game's logging file.
def log(arg):
    arg = str(arg)
    time = datetime.utcnow().isoformat(sep=' ', timespec='milliseconds')
    print(f"{time} > {arg}")
    logging_file = open("files/assets/logs/logs.txt", "a")
    logging_file.write(f"{time} > {arg} \n")
    logging_file.close()

