import time

print(time.asctime())
while True:
    r = time.localtime()
    m = r.tm_min
    s = r.tm_sec
    # m == choose specific minute
    # s == choose specific second
    if m == 16 and s == 0:
        #Place what you want to run here
        print("RUN.Successful")
        time.sleep(1)
# optional
 #   else:
 #       print(".")
 #       time.sleep(1)
