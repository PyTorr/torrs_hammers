import smtplib
import os
from sys import platform
from tkinter import *

def show_message(file_name):
    '''Prints text message from txt file'''
    fl1 = open(file_name, 'r')
    f_str = fl1.read()
    fl1.close()
    # Output a message
    root = Tk()
    w = Label(root, text=f_str)
    w.pack()
    root.mainloop()


def send_email(from_addr, to_addr_list, cc_addr_list,
               subject, message,
               login, password,
               smtpserver='smtp.gmail.com:587'):
    '''
    example:
    sendemail(from_addr    = 'user1@gmail.com',
          to_addr_list = ['user2@gmail.com'],
          cc_addr_list = ['user2@gmail.com'],
          subject      = 'python sending email trail',
          message      = 'email from a python function',
          login        = 'user1@gmail.com',
          password     = 'userq's password')
    '''
    header = 'From: %s \n' % from_addr
    header += 'To: %s\n' % ', '.join(to_addr_list)
    header += 'Cc: %s\n' % ', '.join(cc_addr_list)
    header += 'Subject: %s\n' % subject
    message = header + message

    server = smtplib.SMTP(smtpserver)
    server.starttls()
    server.login(login, password)
    problems = server.sendmail(from_addr, to_addr_list, message)
    server.quit()

def sound_notification():
    '''
    Sound notification.
    need to install: sudo apt install speech-dispatcher
    need to install: sudo apt install sox
    :return:
    '''
    if platform == "linux" or platform == "linux2":
        duration = .5  # second
        freq = 440  # Hz
        os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (duration, freq))
        # os.system('spd-say "your program has finished"')
    elif platform == "win32" or 'darwin':
        import winsound
        duration = 500  # millisecond
        freq = 440  # Hz
        winsound.Beep(freq, duration)

# sound_notification()