import sys
import time

SPIN_CHARS = ['.', '..', '...']

def loading_animation(duration=0.9):
    start_time = time.time()
    cycle = 0
    while time.time() - start_time < duration:
        sys.stdout.write(f'\rLoading {SPIN_CHARS[cycle]}')
        sys.stdout.flush()
        time.sleep(0.3)
        cycle = (cycle + 1) % len(SPIN_CHARS)
    

    sys.stdout.write('\r             \n')
    sys.stdout.flush()

if __name__ == '__main__':
    loading_animation()

