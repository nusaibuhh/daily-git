# A sequence of sequential frame IDs captured over a few seconds
video_frames = [101, 102, 103, 104, 105, 106, 107, 108, 109, 110]

sampled = []

for i in range(len(video_frames)):
    if i % 3 == 0:
        sampled.append(video_frames[i])

print("sampled frames:", sampled)
