import re

text = '''
11
a = 1;
b = input();

if a + b > 0 && a - b < 0:
    start()
elif a*b > 10 || a/b < 1:
    stop()
print set(list(a)) | set(list(b)) 
#Note do not change &&& or ||| or & or |
#Only change those '&&' which have space on both sides.
#Only change those '|| which have space on both sides.
'''
# text = input()

new_text = re.sub("*[a =]", "", text)
new_text = re.sub(r"\&\&", " and ", text)
newest_text = re.sub(r"\|\|", " or ", new_text)

print(newest_text)