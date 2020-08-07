from functools import reduce

def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    hash_table = {}
    
    for temp_arr in arrays:
        for j in temp_arr:
            if j in hash_table:
                hash_table[j] += 1
            else:
                hash_table[j] = 1
        
    # Doesn't work right
        
    

    
    

if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
