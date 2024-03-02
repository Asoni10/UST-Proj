import threading
from password_checker import check_password_validity
from circular_queue import CircularQueue

def password_checker_thread(password):
    output = check_password_validity(password)
    print("Valid passwords:", output)

def circular_queue_thread():
    cq = CircularQueue(max_length=5)
    cq.enqueue(1)
    cq.enqueue(2)
    cq.enqueue(3)
    cq.enqueue(4)
    cq.enqueue(5)
    cq.display()

def main():
    password_input = "asqwr1234@1,aF145#,2w3E*,2We3345"
    cq_thread = threading.Thread(target=circular_queue_thread)
    password_thread = threading.Thread(target=password_checker_thread, args=(password_input,))
    cq_thread.start()
    password_thread.start()
    cq_thread.join()
    password_thread.join()

if __name__ == "__main__":
    main()
