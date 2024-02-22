import time
import sys

def main():
    i = 0
    while True:
        i = i + 1
        print("Ez host test log" + str(5))
        sys.stdout.flush()
        time.sleep(5)

if __name__ == "__main__":
    main()
