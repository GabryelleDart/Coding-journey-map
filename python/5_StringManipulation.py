nome= " maria silva "

# removing spaces
print(nome.strip())
# Upper on the first letter of each word
print(nome.title().strip())
# Upper case
print(nome.upper())
#Replace
print(nome.replace("a","h"))
#F-string
print(f"A {nome.title().strip()} é legal.")
