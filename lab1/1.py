# number
number1 = 10
number2 = 15
result = number1 + number2
print(result)  # out: 25


# word and string
word1 = 'First'
word2 = 'second'
string = word1 + ' ' + word2
print(string)  # out: First second


# list
list = []
n = 0
for i in range(5):
    list.append(n)
    n += 1

for element in list:
    print(element)  # out: 1 2 3 4 5


# tuple
example = (1, 'string', [2, 5, 9])
for element in example:
    print(element)  # out: 1 string [2, 5, 9]
