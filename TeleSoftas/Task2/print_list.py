def print_list(a_list):
    """
    - The first argument of the range function is the start index,
    - The start index provided in this function (start = 1)
    - Python uses zero-based indexing, this means that zero is used to represent the 
    start of a sequence
    - Thus 0 => First element, 1 => second element ...... n => n-1 element
    - This function print out the element of the list incorrectly because the start 
    index specified was 1, which means the list will be printed from the second element 
    onwards, therefore ignoring the first elemment of the list
    """
    for i in range(1, len(a_list)):
        print('Element {} = {}'.format(str(i),str(a_list[i])))


def print_list_modified(a_list):
    """
    - This function is the corrrect version of `print_list` function above
    - It prints all the elements in the list by specifying the start index correctly (start = 0)
    - Also the format function of the `print_list` function has been modified from 
    format(str(i), ==> format(str(i+1) to reflect the correct Element position (outisde the python world)
    """
    for i in range(0, len(a_list)): 
        print('Element {} = {}'.format(str(i+1),str(a_list[i])))


    
if __name__ == '__main__':
    a_list = [1, 2, 3, 5, 7, 9]
    print("{0} Incorrect list {1}".format("="*15, "="*15))
    print_list(a_list) 

    print("{0} Correct list {1}".format("="*15, "="*15))
    print_list_modified(a_list)
