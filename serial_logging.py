import time
import serial
import logging
import logging.handlers
from datetime import datetime


#                       #
#------Serial Setup-----#
#                       #
ser=serial.Serial(
    port='/dev/ttyACM0',
    baudrate=115200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
    )


#                       #
#-----Logging Setup-----#
#                       #
#filename = datetime.now().strftime('./log/AUV_%Y%m%d_%H:%M:%s.log')
filename=datetime.now().strftime('/home/pi/logfile_%Y%m%d_%H:%M:%s.log')        # Format for the logfile name
log = logging.getLogger()
log.setLevel(logging.INFO)
format = logging.Formatter('%(asctime)s : %(message)s')                         # Format for the timestamp for each line entry in the log
file_handler = logging.FileHandler(filename)
file_handler.setLevel(logging.INFO)                                             # Set INFO to be the level for recording to log file.
file_handler.setFormatter(format)
log.addHandler(file_handler)

# Reads one a line in the Serial Class, dumps it to a log file, and prints it.
def serial_logging():
    in_buffer=ser.readline()
    
    # gets the length of the serial string
    length=len(in_buffer)
    
    # chops off the last 2 characters, '\n' newline
    # sends to Logging class which writes to a logfile
    log.info(in_buffer[0:(length-2)].decode())
    print(in_buffer)

# infinite loop for main
def main():
    while(1):
        # Wait for something to show up in the Serial Class buffer.
        while (ser.inWaiting==0):
            time.sleep(0.005)
        # Once something has shown up in the Serial Class buffer, call serial_logging().
        serial_logging()


# If serial_logging is ran directly from the console, main() runs.
# Otherwise main is not called.
if __name__ == "__main__":
    main()
