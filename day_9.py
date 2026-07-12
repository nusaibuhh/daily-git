messy_text = "   Natural   Language   Processing    is     awesome!  "

mess = messy_text.split()
text = ''

for i in mess:
    text += i + ' '

print(text)