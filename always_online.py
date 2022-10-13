import os
import time
import argparse
from BitSrunLogin.LoginManager import LoginManager

def is_connect_internet(testip):
    status = os.system(u"ping {} -c 8".format(testip))
    return status == 0

def always_login(username, password, testip, checkinterval):
    lm = LoginManager()
    login = lambda : lm.login(username=username, password=password)
    timestamp = lambda : print(time.asctime(time.localtime(time.time())))

    timestamp()
    try:
        login()
    except Exception:
        pass
    while 1:
        time.sleep(checkinterval) 
        if not is_connect_internet(testip):
            timestamp()
            try:
                login()
            except Exception:
                pass


def get_args():
    parser = argparse.ArgumentParser(description='PyTorch Training script')
    parser.add_argument('--username', type=str, default='', 
                        help='the user id to login')
    parser.add_argument('--password', type=str, default='', 
                        help='the password')
    args = parser.parse_args()

    return args


if __name__ == "__main__":
    args = get_args()
    
    testip = "114.114.114.114" # IP to test whether the Internet is connected
    checkinterval = 5 * 60
    # checkinterval = 10
    
    always_login(args.username, args.password, testip, checkinterval)
