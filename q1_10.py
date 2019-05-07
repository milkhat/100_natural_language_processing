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

# q5
q5_string = "I am an NLPer"

def  create_n_gram(n,list_type,target_string):
    """
    n-gram関数

    文字列をオプション引数list_typeで文字gramと単語gramのどちらかを作成する
    単語gram: I am an NLper -> I am, am an, an NLper
    文字gram: I am an NLper -> I , a,am,m , a,an,n , N,NL,Lp,pe,er,r  

    @return list
    """
    s_list = []
    if list_type == 'word':
        words = target_string.split(' ')
        for i in range(0, len(words)-n+1):
            s_list.append(words[i:i+n])
    else :
        for i in range(0, len(target_string)-n+1):
            s_list.append(target_string[i:i+n])
    return s_list

print(create_n_gram(2,'word',q5_string))
print(create_n_gram(2,'chara',q5_string))

# q6
q6_s1 = "paraparaparadise"
q6_s2 = "paragraph"
def  create_n_gram(n,list_type,target_string):
    """
    n-gram関数

    文字列をオプション引数list_typeで文字gramと単語gramのどちらかを作成する
    単語gram: I am an NLper -> I am, am an, an NLper
    文字gram: I am an NLper -> I , a,am,m , a,an,n , N,NL,Lp,pe,er,r  

    @return list
    """
    s_list = []
    if list_type == 'word':
        words = target_string.split(' ')
        for i in range(0, len(words)-n+1):
            s_list.append(words[i:i+n])
    else :
        for i in range(0, len(target_string)-n+1):
            s_list.append(target_string[i:i+n])
    return s_list

x = create_n_gram(2,'chara',q6_s1)
y = create_n_gram(2,'chara',q6_s2)

x = set(x)
y = set(y)
print(x,y)
xy_union = x | y
xy_intersection = x&y
xy_difference = x-y

print(xy_union,xy_intersection,xy_difference)

if 'se' in xy_union:
    print('It founds se in xy_union.')

if 'se' in xy_intersection:
    print('It founds se in xy_intersection.')

# q7
def get_message(x,y,z):
    message = str(x) + '時の' + y + 'は' + str(z)
    return message

print(get_message(12,'気温',22.4))

# q8
import string
string1 = "I wish I were a bird!"

def cipher(target_string):
    answer_list = ''
    for i in target_string:
        if i in string.ascii_lowercase:
            target_code = ord(i)
            answer_list = answer_list + chr(219-target_code)
        else :
            answer_list = answer_list + i
    return answer_list

# 暗号化
print(string1 + ':' + cipher(string1))

# 復号化
print(string1 + ':' + cipher(cipher(string1)))

