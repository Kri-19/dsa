#lab-1 
my_list = [10, 20, 30, 40, 50]
print("Elements in the list:")
for element in my_list:
    print(element) #task 1

element_to_insert = 25
insert_index = 2  
my_list.insert(insert_index, element_to_insert)
print("Updated list after insertion:")
print(my_list) #task 2
delete_index = 1
my_list = my_list[:delete_index] + my_list[delete_index + 1:]
print("Updated list after deletion:")
print(my_list)# task 3
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  
    return -1  
target = 30
index = linear_search(my_list, target)
if index != -1:
    print(f"Element {target} found at index {index}.")
else:
    print(f"Element {target} not found.") #task 4
update_index = 2  
new_value = 35    
if 0 <= update_index < len(my_list):
    my_list[update_index] = new_value
    print("Updated list:")
    print(my_list)
else:
    print("Error: Index out of range.")#task 5
   
