import time
import sys

def main():
    while True:
        print("test")
        sys.stdout.flush()  # Flush stdout to ensure immediate output
        time.sleep(5)

if __name__ == "__main__":
    main()
