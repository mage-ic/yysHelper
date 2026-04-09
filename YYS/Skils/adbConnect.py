from adb_shell.adb_device import AdbDeviceTcp
import cv2
import numpy as np
from random import randint


class AdbTools:
    def __init__(self, host='127.0.0.1', port=16384):
        self.device = AdbDeviceTcp(host, port)
        self.connected = False

    def connect(self):
        if self.connected:
            return True
        try:
            self.device.connect()
            self.connected = True
            return True
        except Exception as e:
            self.connected = False
            print(f'ADB connect filed:{e}')
            return False

    def get_page(self):
        if not self.connected:
            self.connect()
        data = self.device.shell('screencap -p', decode=False)
        arr = np.frombuffer(data, np.uint8)
        return cv2.imdecode(arr, cv2.IMREAD_GRAYSCALE)

    def human_like_swipe(self, start_point_x, start_point_y):
        int_rand = [randint(-3, 3), randint(-3, 3), randint(-3, 3), randint(-3, 3), randint(10, 30)]
        self.device.shell(
            f'input swipe {start_point_x + int_rand[0]} {start_point_y + int_rand[1]} {start_point_x + int_rand[2]} {start_point_y + int_rand[3]} {int_rand[4]}')
        return f'({start_point_x},{start_point_y})已被点击'


def adb_connect():
    adb = AdbTools()
    code = adb.connect()
    if not code:
        raise Exception('E00,ADB not connected')
    data = adb.device.shell('screencap -p', decode=False)
    arr = np.frombuffer(data, np.uint8)
    frame = cv2.imdecode(arr, cv2.IMREAD_GRAYSCALE)
    cv2.imwrite("../game page 720p.png", frame)


if __name__ == '__main__':
    adb_connect()
