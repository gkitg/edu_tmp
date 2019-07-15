'''
fuzzysearch('car', 'cartwheel');        // true
fuzzysearch('cwhl', 'cartwheel');       // true
fuzzysearch('cwheel', 'cartwheel');     // true
fuzzysearch('cartwheel', 'cartwheel');  // true
fuzzysearch('cwheeel', 'cartwheel');    // false
fuzzysearch('lw', 'cartwheel');         // false
'''


# Вариант 1
# def fuzzysearch(s1, s2):
#     i = 0
#     for c in s2:
#         if i < len(s1) and s1[i] == c:
#             i += 1
#     return i == len(s1)


# Вариант 2
# def fuzzysearch(str1, str2):
#     order = []
#     last_index = 0
#
#     for i in range(len(str1)):
#         if str1[i] in str2:
#             last_index = str2.find(str1[i], last_index) + 1
#             order.append(last_index)
#
#     return order == sorted(order) and len(str1) == len(order)


# Вариант 3
def fuzzysearch(fnd, text):
    ind = 0
    for l in fnd:
        if l in text[ind:]:
            ind += 1 + text[ind:].index(l)
        else:
            return False
    return True


print(fuzzysearch('car', 'cartwheel'))
print(fuzzysearch('cwhl', 'cartwheel'))
print(fuzzysearch('cwheel', 'cartwheel'))
print(fuzzysearch('cartwheel', 'cartwheel'))
print(fuzzysearch('cwheeel', 'cartwheel'))
print(fuzzysearch('lw', 'cartwheel'))
