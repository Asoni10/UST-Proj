from password_checker import check_password_validity
from circular_queue import CircularQueue


def main():
    # Call functions from password_checker.py and circular_queue.py
    input_password = "asqwr1234@1,aF145#,2w3E*,2We3345"
    output = check_password_validity(input_password)
    print("Valid passwords:", output)

    cq = CircularQueue(max_length=5)
    cq.enqueue(1)
    cq.enqueue(2)
    cq.enqueue(3)
    cq.enqueue(4)
    cq.enqueue(5)
    cq.display()


if __name__ == "__main__":
    main()
