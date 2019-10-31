#############################
#     Midterm Practice
#############################

# First Run at it
vowels = ['a', 'e', 'i', 'o', 'u']
def vowel_counter_dict(str, vowels):
    counter = 0
    str2 = str.lower()
    for letter in str2:
        if letter in vowels:
            counter += 1
        else:
            pass
    print(counter)
    return counter
vowel_counter_dict('HellO My FRIENDly monkey', vowels)

#   Vowel Counter with List Comprehension
def vowel_counter_2(str, vowels):
    list_comp = [letter for letter in str.lower() if letter in vowels]
    print('Number of Vowels Detected: ', len(list_comp))
    list_comp = sorted(list_comp)
    return list_comp
print(vowel_counter_2('Mario is my teacher', 'aeiou'))

#   Vowel Counter with Dictionary Comprehension
def vowel_counter_dict_2(str):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowel_list = {vowel: str.lower().count(vowel) for vowel in vowels}
    count = {vowel: sum([1 for letter in str.lower() if letter == vowel]) for vowel in vowels}
    print(vowel_list, ' is the same as ', count)
    return vowel_list, count
vowel_counter_dict_2('What is happening with this COURSE!')

#   Determine if it is a prime #
def is_num_prime(number):
    number = int(number)
    if number == 1:
        return False
    if number == 2:
        return True
    for i in range(2, number):
        if number % i == 0:
            return False
        else:
            return True
print('Is this a prime =', is_num_prime(2))

#   Newton's Method for approximating a square root
def newtons_root(number):
    number = int(number)
    root = number/2
    for i in range(1, 21):
        root = (root + number/root)/2
    return root
print(newtons_root(99))