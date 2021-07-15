import cv2
import numpy as np

def getTranslatedPos(x, y, dx, dy, H, W):
    return min(H-1, max(0, x+dx)), min(W-1, max(0, y+dy))


def translate(img, move=30):
    if isinstance(img, np.ndarray):
        img = img.tolist()
    elif isinstance(img, list):
        img = img
    else:
        raise TypeError("Only support ndarray or list type img")

    if isinstance(move, int):
        move = [move] * 2
    elif isinstance(move, float) or isinstance(move[0], float):
        raise TypeError("Only support int type translate.")


    H, W, C = len(img), len(img[0]), len(img[0][0])
    tmp_img = [[[0]*C for _ in range(W)] for _ in range(H)]
    for x in range(H):
        for y in range(W):
            nx, ny = getTranslatedPos(x, y, move[0], move[1], H, W)
            
            for c in range(C):
                tmp_img[nx][ny][c] = img[x][y][c]
    return tmp_img

if __name__ == "__main__":
    img_path = "./img/python_logo.png"
    np_img = cv2.imread(img_path)
    list_img = np_img.tolist()

    translated_img = translate(list_img, move=[10, -50])
    translated_img = np.array(translated_img).astype(np.uint8)
    cv2.imshow("Translated Img", translated_img)
    cv2.imshow("Original Img", np_img)
    cv2.waitKey()
    cv2.destroyAllWindows()