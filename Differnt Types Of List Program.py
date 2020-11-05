#Defining lists
print('\t\tSummary Table')

nums_strings = ["15","100","55","42"]
nums_ints = [15,100,55,42]
nums_floats = [12.3,22.8,1.4,5.2]
nums_lists = [[1,2,3],[4,5,6],[7,8,9]]
#Summary of each list
print('The variable nums_strings is a ',type(nums_strings))
print('It contains the elements ',nums_strings)
print('the element ',nums_strings[0],' is a ',type(nums_strings[0]))

print('\nThe variable num_ints is a ',type(nums_ints))
print('It contains the elements ',nums_ints)
print('The element ',nums_ints[0],' is a ',type(nums_ints))

print('\nThe variable num_floats is a ',type(nums_floats))
print('It contains the elements ',nums_floats)
print('The element ',nums_floats[0],' is a ',type(nums_floats[0]))

print('\nThe variable num_lists is a ',type(nums_lists))
print('It contains the elements ',nums_lists)
print('The element ',nums_lists[0],' is a ',type(nums_lists[0]))

#List sorting
print('\nNow sorting num_strings and num_ints...')
nums_strings.sort()

print('\nSorted num_strings: ',nums_strings)
nums_ints.sort()

print('\nSorted num_ints: ',nums_ints)

print('\n\nTherefore, Strings are sorted alphabetically while integers are sorted numerically') 