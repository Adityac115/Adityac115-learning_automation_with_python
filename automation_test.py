import shutil
import psutil

'''checks the disk space'''
du = shutil.disk_usage("/")
print(du)
print(du.free/du.total *100)

'''checks the cpu percent usage'''

print(psutil.cpu_percent(0.1))

'''health checks'''

def check_disk_usage(disk):
    du1 = shutil.disk_usage("/")
    free = du1.free/du1.total * 100
    return free>75

def check_cpu_usage():
    usage = psutil.cpu_percent(1)
    return usage<20



if not check_cpu_usage() or not check_disk_usage("/"):
    print("ERROR!")
else:
    print("everything is OK!")