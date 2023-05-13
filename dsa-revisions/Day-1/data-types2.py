"""
 Part 2 of data-types:
    Now we some special things in python such as list, tuple ,sets and dictionaries

    List: is use to store multiple items in single varible in ordered format.
         So list is  collection of elements which is store in some particular order maintian by indexing
         and list can store any kind of data items and value of list can update, deleted due muttable nature.
         To create list we square brackets stu_name = ['name1', 'name2', ]

"""

# list
stu_name  = ['ankita', 'krishna', 'aman', 'karan', 'nisha'] # storing stu-names here
# store stu ids

stu_ids  = [12,34,5,4,34,45,56,34] #
expense_list = ['Tution fee', 400, 'collage fee', 1000, 'grocery',340]

# add new expense

expense_list.extend(['Asia Tour', 1000])
print(expense_list)

expense_list.append('Vocation Tour')
expense_list.remove('grocery')
expense_list.pop() # remove last elements default
expense_list.pop(2) # remove elm at index 2


# update
expense_list[3] = 'new Update expense data elements'
print(expense_list)


 
[12,45,32,34, 34,23]