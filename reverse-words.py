# Challenge Notebook
# Problem: Implement an algorithm to reverse words in a string.
# Example:
# Input: "Don't write better error messages, write code that doesn't need them. (Jason C. McDonald)"
# Output: "Nod't etirw retteb rorre segassem, etirw edoc taht nseod't deen meht. (Nosaj C. Dlanodcm)"

    # Constraints
    # Test Cases
    # Algorithm
    # Code
    # Unit Test
    # Solution Notebook

# Constraints

#     Can we assume the string is ASCII?
#         Yes
#     Note: Unicode strings could require special handling depending on your language
#     Can we assume this is case sensitive?
#         Yes
#     Can we use additional data structures?
#         Yes
#     Can we assume this fits in memory?
#         Yes

sentence = "Don't write better error messages, write code that doesn't need them. (Jason C. McDonald)"

x = sentence.split()
y = "pala'vra"
symbols = "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"

for i in symbols:
    if i in y:
        w = y[:y.find(i)] + " " + y[y.find(i):]
        print(y)
        print(w)

def put_symbol_correctly(word):
    symbols = ".,!?$"
    z = word
    for i in symbols:
        if i in word[0]:
            z = word.replace(i, "") + i
    if ")" in word[0] and "(" in word[-1]:
        z = word.replace("(", "").replace(")", "(") + ")"
    return z

def inverte_words(x):
    z = []
    for i in x:
        z.append(i[::-1])
    return z

def case_check(word):
    if word[-1] is word.upper()[-1]:
        return word.lower().capitalize()
    else:
        return word

print(case_check("ase"))
print(inverte_words(x))
print(put_symbol_correctly(")word("))