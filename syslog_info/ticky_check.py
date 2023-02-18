#!/usr/bin/env python3
import re
import csv
import operator
import sys

per_user = {}
errors = {}

logfile = './syslog_info/syslog.log'
f = open(logfile, 'r')

errorfile = './syslog_info/error_message.csv'
userfile = './syslog_info/user_statistics.csv'

for log in f:
        result = re.search(r"ticky: ([\w+]*):? ([\w' ]*) [\[[0-9#]*\]?]? ?\((.*)\)$", log)
        # if result.group(2) not in errors.keys():
        errors[result.group(2)]=errors.get(result.group(2),0) + 1
        if result.group(3) not in per_user.keys():
                per_user[result.group(3)] = {}
                per_user[result.group(3)]["INFO"] = 0
                per_user[result.group(3)]["ERROR"] = 0

        if result.group(1) == "INFO":
                per_user[result.group(3)]["INFO"] += 1
        elif result.group(1) == "ERROR":
                per_user[result.group(3)]["ERROR"] += 1


errors = sorted(errors.items(), key = operator.itemgetter(1), reverse = True)
per_user = sorted(per_user.items())
per_user_stats=[]
[per_user_stats.append((i,val["INFO"],val["ERROR"])) for i,val in per_user]

# for i,val in per_user:
#         # a=(val[0],val[1]["INFO"],val[1]["ERROR"])
#         per_user_stats.append((i,val["INFO"],val["ERROR"]))
#         # print(val["INFO"])

# print(per_user)
print(per_user_stats)
f.close()
errors.insert(0, ('Error', 'Count'))

with open(errorfile, 'w') as f:
        writer=csv.writer(f)
        writer.writerows(errors)
# for error in errors:
#         a,b = error
#         f.write(str(a)+','+str(b)+'\n')


f = open(userfile, 'w')
# f.write("Username,INFO,ERROR\n")
writer=csv.DictWriter(f,fieldnames=["Username","INFO","ERROR"])
writer.writeheader()
writer=csv.writer(f)
writer.writerows(per_user_stats)
# for stats in per_user:
#         a, b = stats
#         f.write(str(a)+','+str(b["INFO"])+','+str(b["ERROR"])+'\n')
f.close()
sys.exit(0)