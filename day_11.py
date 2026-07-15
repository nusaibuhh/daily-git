# A stream of heart rate readings over time
heart_rates = [70, 72, 71, 75, 82, 80, 78, 79, 75]

sampled = []


for i in range(len(heart_rates)):
    if i == 0 or i == len(heart_rates) - 1:
        continue
    if heart_rates[i] > heart_rates[i - 1] and heart_rates[i] > heart_rates[i + 1]:
        sampled.append(heart_rates[i])

print(sampled)