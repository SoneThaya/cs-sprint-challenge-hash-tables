# Your code here

def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    
    files_table = []
    words_table = {}
    
    for word in files:
        # split path by /
        path = word.split("/")
        # target last item
        name = path[-1]
        # checks if last item is in table
        if name not in words_table:
            words_table[name] = []
        # adds to table
        words_table[name].append(word)
    
    # loop through queries to check
    for word in queries:
        #checks table
        if word in words_table:
            # adds to files table
            files_table.extend(words_table[word])
            
    return files_table

    


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
