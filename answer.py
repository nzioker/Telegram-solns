def decode(text_file):
    words_array = {} 
    # Read the text file and add the contents of the file in a dictionary
    with open(text_file,'r') as file:
        lines = file.readlines()
        for line in lines:
            words_array[int(line.split()[0])] = ''.join(line.split()[1:])

    py_list = [[1],[2,3],[4,5,6]]    # I'm not sure whether this pyramid should be dynamic. If so, I could produce the same list dynamically.
    # It could help handle text files with different lines.
    final_sentence = [] 
    for i in words_array.keys():
        for j in py_list:
            if i == j[-1]:
                final_sentence.append(i)
    
    final_sentence.sort() # I've sorted because because the pyramid increases numerically from the top.
    return " ".join([words_array[i] for i in final_sentence])

print(decode('words.txt'))