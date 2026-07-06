# A sequence where some frames dropped out of nowhere!
captured_frames = [201, 202, 204, 205, 206, 209, 210]

missing = []

for i in range(len(captured_frames)-1):
    if captured_frames[i+1] - captured_frames[i] > 1:
        for j in range(captured_frames[i+1] - captured_frames[i]):
            if captured_frames[i] +  1 + j not in captured_frames:
                missing.append(captured_frames[i] +  1 + j)

print("missing frames:", missing)