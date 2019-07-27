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
#     for i in range(len(str1)):
#         if str1[i] in str2:
#             last_index = str2.find(str1[i], last_index) + 1
#             order.append(last_index)
#     return order == sorted(order) and len(str1) == len(order)


# Вариант 3
# def fuzzysearch(fnd, text):
#     ind = 0
#     for l in fnd:
#         if l in text[ind:]:
#             ind += 1 + text[ind:].index(l)
#         else:
#             return False
#     return True


# Вариант 4
# def fuzzysearch(str_1, str_2):
#     str_1, str_2 = list(str_1), list(str_2)
#     while len(str_1) != 0:
#         if len(str_2) == 0:
#             return False
#         if str_1[-1] == str_2.pop():
#             str_1.pop()
#     return True


# Вариант 5
# def fuzzysearch(str_1, str_2):
#     pos = 0
#     for x in str_1:
#         while True:
#             if pos == len(str_2):
#                 return False
#             pos += 1
#             if str_2[pos - 1] == x:
#                 break
#     return True


# Вариант 6
# def fuzzysearch(str_1, str_2):
#     j = 0
#     for x in str_2:
#         if x == str_1[j]:
#             j += 1
#             if j == len(str_1):
#                 return True
#     return False


# Вариант 7 TODO
def fuzzysearch(s1, s2):
   pass


# Возвращает наибольшую общую подпоследовательность
# def fuzzysearch(s1, s2):

#    m = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]

#    for i, item_1 in enumerate(s1, start=1):
#       for j, item_2 in enumerate(s2, start=1):
#          if item_1 == item_2:
#             m[i][j] = m[i -1][j -1] + 1
#          else:
#             m[i][j] = max(m[i][j - 1], m[i -1][j])

#    i, j = len(s1), len(s2)
#    result = []
   
#    while i > 0 and j > 0 and m[i][j] != 0:
#       if m[i - 1][j] == m[i][j] and m[i - 1][j - 1] < m[i][j] and m[i][j - 1] < m[i][j]:
#          i -= 1
#       elif m[i][j - 1] == m[i][j] and m[i - 1][j - 1] < m[i][j] and m[i - 1][j] < m[i][j]:
#          j -= 1
#       elif m[i - 1][j - 1] < m[i][j]:
#          result.append(s1[i - 1])
#          i, j = i - 1, j - 1
#       else:
#          i, j = i - 1, j - 1

#    result.reverse()
#    result = ''.join(result)

#    return result


print(fuzzysearch('car', 'cartwheel'))
print(fuzzysearch('cwhl', 'cartwheel'))
print(fuzzysearch('cwheel', 'cartwheel'))
print(fuzzysearch('cartwheel', 'cartwheel'))
print(fuzzysearch('cwheeel', 'cartwheel'))
print(fuzzysearch('lw', 'cartwheel'))