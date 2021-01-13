example_sentence = input('Please enter a sentence you want to be camel cased ')

#Validating the input
while not example_sentence:
    print('Please enter something')
    example_sentence = input('Enter a sentence you want to be camel cased')

#Splitting the sentence 
split_sentence = [] 
split_sentence = example_sentence.split()
print(split_sentence)

# Creating the camel case sentence and print
camel_cased_sentence = ''.join(ele.lower() for ele in split_sentence[0:1]) + ''.join(ele.title() for ele in split_sentence[1:])
print('Your sentence in Camelcase is: ' + camel_cased_sentence)


# Test examples trying to find out how to make this work. I can get
example = 'tHe Words AreNt WorKinG MaSoN'

new_example = example.split()
print(new_example)

res = ''.join(ele.lower() for ele in  new_example[0:1]) + ''.join(ele.title() for ele in new_example[1:])

print(res)

