import time
for x in range(101):
    print("\r{:3}%".format(x),end="")
    time.sleep(0.1)