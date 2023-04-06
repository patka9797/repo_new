def sum_word_in_string(string):
    counts = dict()
    str_split = str.split(string)
    for word in str_split:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts


print(sum_word_in_string("babka, jajko,babka, kurczak"))
