def generate_combinations(string: str) -> set[str]:
    combinations = set()
    if ' ' in string:
        combinations.add('')
    if len(string) > 1:
        for i in range(len(string)):
            for char in generate_combinations(string[:i] + string[i + 1:]):
                combinations.add(char)
                combinations.add(string[i] + char)
    combinations.add(string)
    return combinations


input_string = input("Введите строку: ")
result = generate_combinations(input_string)
print(result)
