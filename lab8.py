import cv2


def task_1():
    img = cv2.imread('variant-8.jpg')
    w, h = img.shape[:2]
    cx = w // 2
    cy = h // 2
    cropped = img[cx - 200:cx + 200, cy - 200:cy + 200]
    cv2.imwrite('new_pic.jpg', cropped)


def task_2_3():
    cap = cv2.VideoCapture('sample.mp4')
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21, 21), 0)
        ret, thresh = cv2.threshold(gray, 110, 255, cv2.THRESH_BINARY_INV)
        countours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        if len(countours) > 0:
            c = max(countours, key=cv2.contourArea)
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.line(frame, (x + w // 2, y), (x + w // 2, y + h), (0, 255, 0), 2)
            cv2.line(frame, (x, y + h // 2), (x + w, y + h // 2), (0, 255, 0), 2)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()


def task_additional():
    cap = cv2.VideoCapture('sample.mp4')
    fly = cv2.imread('fly64.png')
    fly = cv2.resize(fly, (32, 32))
    fly_h, fly_w = fly.shape[:2]
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21, 21), 0)
        ret, thresh = cv2.threshold(gray, 110, 255, cv2.THRESH_BINARY_INV)
        countours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        if len(countours) > 0:
            c = max(countours, key=cv2.contourArea)
            x, y, w, h = cv2.boundingRect(c)
            center_x = x + (w // 2)
            center_y = y + (h // 2)
            frame[center_y - fly_h // 2:center_y + fly_h // 2, center_x - fly_w // 2:center_x + fly_w // 2] = fly
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()


task_1()
#task_2_3()
#task_additional()
