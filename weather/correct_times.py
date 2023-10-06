#!/usr/bin/env python3
# Shift times by an offset
# A. Schlemmer, 01/2022

from datetime import datetime, timedelta

skip = 1
sep = ","

with open("data.csv", "r") as f:
    lines = f.readlines()

lines_new = list()
for line in lines:
    if skip > 0:
        lines_new.append(line)
        skip -= 1
        continue

    cols = line.split(sep)
    time = datetime.strptime(cols[0], "%Y-%m-%d %H:%M")
    corrected = time + timedelta(days=50, seconds=20)
    line_new = sep.join([datetime.strftime(corrected, "%Y-%m-%d %H:%M")]
                        + cols[1:])
    lines_new.append(line_new)
    

with open("data_new.csv", "w") as f:
    f.writelines(lines_new)
