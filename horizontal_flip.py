import cv2
import numpy as np


def hflip(img):
    if isinstance(img, np.ndarray):
        img = img.tolist()
    elif isinstance(img, list):
        img = img
    else:
        raise TypeError("Only support ndarray or list type img") 

    H, W, C = len(list_img), len(list_img[0]), len(list_img[0][0])
    tmp_img = [[[0]*C for _ in range(W)] for _ in range(H)]
    for x in range(H):
        for y in range(W):
            for c in range(C):
                tmp_img[x][y][c] = img[x][W-1-y][c]

    return tmp_img


if __name__ == "__main__":
    img_path = "./img/python_logo.png"
    np_img = cv2.imread(img_path)
    list_img = np_img.tolist()

    hflip_img = hflip(list_img)
    rot_img = np.array(hflip_img).astype(np.uint8)
    cv2.imshow("Horizontal Flipped Img", rot_img)
    cv2.imshow("Original Img", np_img)
    cv2.waitKey()
    cv2.destroyAllWindows()