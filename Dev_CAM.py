import cv2

def Cam(index):
    cap = cv2.VideoCapture(index, cv2.CAP_DSHOW)

    while True:
        ret, frame= cap.read()

        if ret:
            frame= cv2.flip(frame,1)
            cv2.imshow('frame', frame)
        k = cv2.waitKey(1)
        if k == ord('q'):
            print("Exit camera!")
            break
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    Cam(0)