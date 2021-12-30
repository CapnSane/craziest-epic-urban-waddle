import re
S = input("Digite S: ")

# s = re.findall(r'(?<=[^aeiouAEIOU0-9\+\-\s])[aeiouAEIOU]{2,}(?=[^aeiouAEIOU0-9\+\-\s])', S)

# for i in s:
#   if len(i)<=1:
#     pass
#   else:
#     print(i)
# if len(s)==0:
#     print(-1)

jorge = list(re.finditer(r'(?<=[^aeiouAEIOU0-9\+\-\s])([aeiouAEIOU]+)([aeiouAEIOU])(?=[^aeiouAEIOU0-9\+\-\s])', S))
for i in jorge:
    print(i.group(0))
    
if len(jorge) <= 0:
  print(-1)