# Raw heart rate readings with a sudden sensor spike (the 120)
raw_signal = [72, 75, 74, 120, 78, 76, 74]
raw_avg = []
for i in range(len(raw_signal)-2):
    avg = (raw_signal[i] + raw_signal[i + 1] + raw_signal[i + 2]) / 3
    raw_avg.append(f"{avg:.2f}")

print("Smoothed heart rate readings:", raw_avg)
