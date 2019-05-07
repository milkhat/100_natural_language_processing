# q0
# 後で読む：http://d.hatena.ne.jp/redcat_prog/20111104/1320395840
test = 'stressed'
test[::-1]

# q1
test[::2]

# q2
car1 = 'パトカー'
car2 = 'タクシー'
c1 = list(car1)
c2 = list(car2)
s = ''
for i in range(0,len(c1)):
    s = s + c1[i]
    s = s + c2[i]

print(s)

# q3
q3_string = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
q3_replace = q3_string.replace(',','')
q3_replace = q3_replace.replace('.','')
q3_list = q3_replace.split(' ')
answer_list = []
for l in q3_list:
    answer_list.append(len(l))

print(answer_list)

# q4
q4_string = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

q4_words = q4_string.replace('.','')
q4_words = q4_words.replace(',','')
q4_words = q4_words.split(' ')

answer_map = {}
num_list = [1, 5, 6, 7, 8, 9, 15, 16, 19]
for i,v in enumerate(q4_words):
    if i+1 in num_list:
        answer_map[i]=v[:1]
    else:
        answer_map[i]=v[:2]

print(answer_map)
