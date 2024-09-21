my_list = [2, 4, 7, 76, 98, 76, 43]
s_juft = 0
s_toq = 0
for i in my_list:
    if i % 2 == 0:
        s_juft += i
    else:
        s_toq += i
print(s_juft)
print(s_toq)
