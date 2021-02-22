numbers = {'first': 1, 'second': 2, 'third': 3}

squared_numbers = {key: value ** 2 for key, value in numbers.items()}
print(squared_numbers)

print('*' * 10)
numbers = {num: num**2 for num in range(1, 10)}
print(numbers)

print('*' * 10)
str1 = 'ABC'
str2 = '123'
combo = {str1[i]: str2[i] for i in range(len(str1))}
print(combo)

print('*' * 10)
num_parity = {num: ('even' if num % 2 == 0 else 'odd') for num in range(1, 5)}
print(num_parity)
