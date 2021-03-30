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
filename=datetime.now().strftime('/home/pi/logfile_%Y%m%d_%H:%M:%s.log')
log = logging.getLogger()
log.setLevel(logging.INFO)
format = logging.Formatter('%(asctime)s : %(message)s')
file_handler = logging.FileHandler(filename)
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(format)
log.addHandler(file_handler)

def serial_logging():
    in_buffer=ser.readline()
    length=len(in_buffer)
    log.info(in_buffer[0:(length-2)].decode())
    print(in_buffer)

def main():
    while(1):
        while (ser.inWaiting==0):
            time.sleep(0.005)
        serial_logging()


if __name__ == "__main__":
    main()
