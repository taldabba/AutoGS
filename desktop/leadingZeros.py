import time

print("Start time")

start_time = time.time()
print(start_time)
start_time = start_time + 60
print(start_time)
stopper = input("press enter to stop")
end_time =time.time()
print("you have finished")
print(end_time)
print("---------------")
duration = int(end_time - start_time)
print(duration)
if duration > 5:
    print("Bad Luck you were not fast enough")
else:
    print("well done you are very quick")