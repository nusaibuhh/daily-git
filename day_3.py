sample_text = "Cats love matrix grids, but some cats prefer pixel grids"

def count_words(text):
    words = text.split()
    word_count = {}
    for word in words:
        word = word.lower().strip(",.?!;:")
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

counts = count_words(sample_text)
print(counts)