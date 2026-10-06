import numpy as np

today = np.datetime64("today")

print("Yesterday:", today - np.timedelta64(1, "D"))
print("Today:", today)
print("Tomorrow:", today + np.timedelta64(1, "D"))