from time import *

stopwatch = input("1 - start. 0 - stop: ")
while stopwatch != "0":
    if stopwatch == "1":
        start_timer = time()
    stopwatch = input("0 - End Timer: ")
end_timer = time()
total = end_timer - start_timer
print("TOtal timer: ", total, "sec")
