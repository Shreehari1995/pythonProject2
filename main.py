# s = input("enter the string: ")
# if s == s[::-1]:
#     print(f"{s} is a palindrome")
# else:
#     print(f"{s} is not a palindrome")
#
#
# class empty:
#     pass


# s = "AABBBCC"
# # o/p = 2A3B2C
#
# s1 = ""
#
# n = 0
# k = "l"
# if s[0] != k:
#     m = k
# else:
#     m = "k"
# for i in s:
#     if m == i:
#         continue
#     else:
#         m = i
#         count = 0
#         for j in s[n:]:
#             if i == j:
#                 count += 1
#             else:
#                 break
#         n += count
#         s1 += str(count) + i
# print(s1)

# import re
# s = "Iam Sri Hari, Am from Davangere"
# s1 = "".join(re.findall(r"\w+", s))
# a = 0
# s2 = ""
# for i in range(len(s1)):
#
#     if a == 4:
#         s2 += " " + s1[i]
#     else:
#         s2 += s1[i]
#         a += 1
#
# print(s2)




from time import sleep

for i in range(10):
    pg.write("hi")
    sleep(5)
    pg.press("enter")