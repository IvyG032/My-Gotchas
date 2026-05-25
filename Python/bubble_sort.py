#Write a function called find_range. find_range should take
#as input a string representing a filename. The file
#corresponding to that filename will be a list of integers,
#one integer per line. find_range should return a tuple
#containing the smallest and largest numbers in the file
#(the smallest first, then the largest).
#
#For example, in the dropdown in the top left you'll find a
#file named FindRangeInput.txt. The smallest number in that
#file is 2, and the largest is 37. So, if you called
#find_range("FindRangeInput.txt"), the function would return
#(2, 37), a tuple with two integers.
#
#You may assume that all lines in the file will contain a
#positive integer (greater than 0). There may be duplicates.
#
#Hint: Remember, if you loop through all the lines in a file
#then you have to close and reopen the file to read it again,
#or by use file.seek(0) to start from the top. However, you
#can do this problem without having to read the file twice.


#Write your function here!
def find_range(filename):
    num_list = []
    with open(filename, "r") as file:
        for num in file:
            num = num.strip()
            num = int(num)
            num_list.append(num)

    n = len(num_list)

    for i in range(n):
        for j in range(n-i-1):
            if num_list[j] > num_list[j+1]:
                num_list[j], num_list[j+1] = num_list[j+1], num_list[j]
    
    return f"{num_list[0]}, {num_list[-1]}"


    

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: (2, 37)
print(find_range("Test.txt"))


8
6
16
26
10
18
10
27
13
22
6
35
32
36
37
2
14
14
16


# 解法2
def find_range(filename):
    num_list = []
    with open(filename, "r") as file:
        for num in file:
            num = num.strip()
            num = int(num)
            num_list.append(num)

    min_num = max_num = num_list[0]
    for i in range(len(num_list)):
        if num_list[i] < min_num:
            min_num = num_list[i]
        elif num_list[i] > max_num:
            max_num= num_list[i]
            
    return (min_num, max_num)