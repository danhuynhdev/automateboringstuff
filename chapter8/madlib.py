import re

text = ''

with open('text.txt') as f:
    text = f.read()

regex = re.compile(r'ADJECTIVE|NOUN|VERB|ADVERB')

for mo in regex.finditer(text):
    sub = mo.group()
    text = text.replace(sub, input('Enter a {}\n'.format(sub.lower())), 1)

print(text)

with open('text_out.txt', 'w') as f:
    f.write(text)
