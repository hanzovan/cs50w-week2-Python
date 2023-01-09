import time
def announce(f):
    def wrapper(*args, **kwargs):
        print("Prepare to run")
        time.sleep(2)
        f(*args, **kwargs)
        time.sleep(2)
        print("Done running")
    return wrapper

@announce
def hello(name):
    print(f"Good morning, {name}")

hello("Archer")