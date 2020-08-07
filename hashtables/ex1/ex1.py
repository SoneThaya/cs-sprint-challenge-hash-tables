def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    hash_table = {}
    # loop through array
    for i in range(length):
        weight = weights[i]
        # check if weight is in hash table
        if weight in hash_table:
            value = hash_table[weight]
            return [i, value]
        # finds the difference
        difference = limit - weight
        hash_table[difference] = i

    return None
