# Timestamps of user actions throughout the day (in minutes)
click_timestamps = [3, 5, 7, 19, 21, 22, 24, 45, 46]

clip_timestamps = []
duration = []

for i in range(len(click_timestamps)):
    if i < len(click_timestamps) - 1 and click_timestamps[i + 1] - click_timestamps[i] < 5:
        clip_timestamps.append(click_timestamps[i])
    else:
        if clip_timestamps:
            time = click_timestamps[i] - clip_timestamps[0]
            duration.append(time)
            clip_timestamps = []



print("total unique sessions:", len(duration))
print("duration of first session:", duration[0])