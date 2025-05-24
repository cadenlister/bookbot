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

def sorting(dict): #used to act as a key to sort through the dict list
    return dict["num"]

def word_sort(words): #takes a dictionary as an input and then creates a list of dictionaries
    dict_list = []
    name_dict = {}
    for k,v in words.items():
        name_dict["char"] = k
        name_dict["num"] = v
        dict_list.append(name_dict)
        name_dict={}
    print(dict_list)
    dict_list.sort(reverse=True, key=sorting)
    print (dict_list)
    return dict_list
        
    
    
        
    
    