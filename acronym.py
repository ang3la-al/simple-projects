user_input = input("Input the phrase you would like as an acronym: ")

words = user_input.split(" ")
acronym = ""

for w in words:
    acronym += w[0]

print(acronym.upper())