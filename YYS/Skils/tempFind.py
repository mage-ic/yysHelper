from random import randint
import cv2
import numpy as np


class TempFind:
    @staticmethod
    def return_randint():
        return randint(-3, 5)

    @staticmethod
    def find_temp(full_gray: np.ndarray,
                  template: np.ndarray,
                  roi: tuple,
                  threshold=0.6):
        x1, y1, x2, y2 = roi
        roi_frame = full_gray[y1:y2, x1:x2]
        h, w = template.shape[:2]

        res = cv2.matchTemplate(roi_frame, template, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, max_loc = cv2.minMaxLoc(res)

        if max_val < threshold:
            return None, None

        px, py = max_loc
        cx = x1 + px + w // 2 + TempFind.return_randint()
        cy = y1 + py + h // 2 + TempFind.return_randint()
        return cx, cy
