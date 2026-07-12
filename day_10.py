raw_log = "Reviewer @user123 and participant @alex99 agreed to the study terms."

log = raw_log.split()
text = ''

for i in range(len(log)):
    if log[i].startswith('@'):
        log[i] = '****'

for i in log:
    text += i + ' '

print(text)