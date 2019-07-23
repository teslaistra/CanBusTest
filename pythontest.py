import threading

def print_thread():
    print("a")

sendjoyframethread = threading.Thread(target=print_thread, args=())
sendjoyframethread.start()