#task 1
my_list = [13.1, 1.7, 1.8, 7.8, 1.2, 12.9, 10.6, 5.8, 3.0, 9.7, 18.6, 0.5, 7.6, 0.1]
i = 0

my_list.sort(reverse=True)

#task2
for item in my_list:
    print(item)

count = len(my_list)
avg_value = sum(my_list) / len(my_list)

median = len(my_list) // 2
median_cont = (my_list[median] + my_list[~median]) / 2

average = avg_value
avg_value = round(average, 2)

new_median = median_cont
median_cont = round(new_median, 2) #set it to round to 2 decimal places but it round to 6.7 no matter what I do, it was 6.699... which I believe is why it won't add an extra 0 (6.70)
  

print('Count:', count)
print('average:', avg_value)
print("Median of list is:", median_cont)
print("Smallest number is:", min(my_list))
print("Largest number is:", max(my_list))

#task 3
index = int(input('Enter an index: '))
count = 0

num = my_list[index] 
print('the number at index:', index, 'is:', num)

new_num = int(input('Please enter a new number to replace this index: '))

my_list.insert(index, new_num)

print('Ok, you chose:', new_num, 'to be added at index:', index)
print('Here is your new, updated list!')

for item in my_list:
    print(item)


#bonus
print()
print('Bonus: ')
my_list = [13.1, 1.7, 1.8, 7.8, 1.2, 12.9, 10.6, 5.8, 3.0, 9.7, 18.6, 0.5, 7.6, 0.1]

reverse = len(my_list)

for item in range(int(reverse/2)):
    k = my_list[item]
    my_list[item] = my_list[reverse - item - 1]
    my_list[reverse - item - 1] = k

print(*my_list, sep=' ~ ')