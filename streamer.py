import streamlit as st
import cv2



from threading import Thread
import cv2, time

class ThreadedCamera(object):
    def __init__(self, src=0):
        self.capture = cv2.VideoCapture(src)
        self.capture.set(cv2.CAP_PROP_BUFFERSIZE, 2)

        # FPS = 1/X
        # X = desired FPS
        self.FPS = 1/30
        self.FPS_MS = int(self.FPS * 1000)

        # Start frame retrieval thread
        self.thread = Thread(target=self.update, args=())
        self.thread.daemon = True
        self.thread.start()

    def update(self):
        while True:
            if self.capture.isOpened():
                (self.status, self.frame) = self.capture.read()
            time.sleep(self.FPS)

    def show_frame(self):
        cv2.imshow('frame', self.frame)
        cv2.waitKey(self.FPS_MS)

# if __name__ == '__main__':

image_placeholder = st.empty()
if st.button('Start'):
    # video = cv2.VideoCapture('https://cdn.dribbble.com/users/702789/screenshots/15739140/media/0e05ae046822a4169924c634f2c3bdbc.mp4')
    # while True:
    #     success, image = video.read()
    #     image_placeholder.image(image)


    # src = 'https://cdn.dribbble.com/users/702789/screenshots/15739140/media/0e05ae046822a4169924c634f2c3bdbc.mp4'
    src = 0
    threaded_camera = ThreadedCamera(src)
    while True:
        try:
            image_placeholder.image(cv2.cvtColor(threaded_camera.frame, cv2.COLOR_BGR2RGB))
        except AttributeError:
            pass