def count_words(text):
    count = 0
    words = text.split()
    for word in words:
        count += 1
    return count

def count_characters(texts):
    character_counts = {}
    for text in texts.lower():
        if text in character_counts:
            character_counts[text] += 1
        else:
            character_counts[text] = 1
    return (character_counts)