# Question1a
def replaces(list1,list2):
    return list1[:3] + list2
list1 = [1,2,3,4]
list2 = [-1,0,10]
print(replaces(list1,list2))


# Question1b
def insertElement(mylist,element):
    for i in range(len(mylist)):
        mylist.insert(2*i,element)
    return mylist
mylist = ["happy", "new", "year"] 
element = 2020
# print(insertElement(mylist,element))


# Question2a
def check_critetia(number):
    convert_str = str(number)
    convert_list = list(convert_str)
    if len(convert_list) == 6:
        for i in range(len(convert_list)-1):
            if convert_list[i] == convert_list[i+1]:
                    for i in range(len(convert_list)-1):
                        if convert_list[i] <= convert_list[i+1]:
                            return True   
    return False
print(check_critetia(135679))


# Question2b
def count_criteria(start,end):
     count = 0
     for num in range(start,end+1):
          if check_critetia(num):
               count +=1
     return count
start = 111111
end = 123455
print(count_criteria(start,end))



# Question3
def count_del_characters(character):
     count = 0
     for i in range(len(character)-1):
          if character[i] == character[i+1]:
               count +=1
     return character, count
character = "AABAABBBBAAA"
print(count_del_characters(character))

# Question4a
list1 = [78,61,50,78,50,71,78,90]
list2 = [8, 8, 5, 2, 9]
def find_mode(mylist):
     max = 0
     for i in range(len(mylist)):
          if mylist.count(mylist[i]) > max:
               max=mylist.count(mylist[i])
               mode = mylist[i]
     return mode
print(find_mode(list2))


# Question4b
def studen_mode(mylist):
     modes = []
     for i in range(len(mylist[0])):
          temp_column = []
          for j in range(len(mylist)):
               temp_column.append(mylist[j][i] )
          modes.append(find_mode(temp_column))
     return modes

M= [[8,8,5,2,9],[8,9,7,6,6],[2,9,5,2,1],[10,9,8,8,9]]

print(studen_mode(M))
          

# Question5aiii  time complexity is  n**2 (quadratic) 
     
def mistery_function(data):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(data)-1):
            if data[i] > data[i+1]:
                data[i],data[i+1] = data[i+1],data[i]
                swapped = True
data = [9, 1, 7, 6, 2, 8, 5, 3, 4, 0]
mistery_function(data)
print(data)

# Question5aiv   time complexity is factorial n!(something else)
def heap_permutation(data, n): 
    if n == 1:
        print(data)
        return
    for i in range(n):
        heap_permutation(data, n - 1)
        if n % 2 == 0:
            data[i], data[n-1] = data[n-1], data[i]
        else:
            data[0], data[n-1] = data[n-1], data[0]
data = [1, 2, 3]
heap_permutation(data, len(data))

# Question5b 
def f1(x, y):
 print('f1:', x, y)
 return x + y
def f2(x, y):
 print('f2:', x, y)
 return x * y
print(f1(f2(6, 5), f1(2, 4)))


# Question5c
data = ['M', 'A', 'D', 'E', 'B', 'F', 'C']
for i in range(len(data)-1):
   candi = data[i]
   candi_index = i
   for j in range(candi_index, len(data)):
       if data[j] < candi:
           candi = data[j]
           candi_index = j
   data[candi_index]= data[i] 
   data[i] = candi
print(data)
     