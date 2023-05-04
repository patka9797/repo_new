# def sum_word_in_string(string):
#     counts=dict()
#     words=str.split(string)
#     for word in words:
#         if word in counts:
#             counts[word] +=1
#         else: 
#             counts[word]=1
#     return counts
# print(sum_word_in_string('babka, jajko,babka, kurczak'))

from collections import Counter

def sum_word_in_string(string):

    return dict(Counter(string))

print(sum_word_in_string('babka, jajko,babka, kurczak'))  
