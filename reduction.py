def ngrams(input, n):
    # Adapted from https://stackoverflow.com/a/13424002
    input = input.split(' ')
    output = {}
    for i in range(len(input)-n+1):
        g = ' '.join(input[i:i+n])
        output.setdefault(g, 0)
        output[g] += 1
    return output

def substring_reduction(line, lower=1, upper=4):
    freq = dict()
    # get ngram vocab
    for i in range(lower, upper+1):
        freq.update(ngrams(line, i))    # get all substrings of length i that appear at least once
   
    
    freq = {k: freq[k] for k in freq if freq[k] > 1}
    reduced = set()#wc = {key: 0 for key in freq}     # a string is a word candidate if it is irreducable
    for str_i in freq.keys():
        for str_j in freq.keys():
            if str_i != str_j and str_i in str_j and freq[str_i] == freq[str_j]:
                # str_i is a substring of str_j and have the same frequency as str_j,
                # therefore str_i is reducable by str_j
                reduced.add(str_i)
    return [word for word in freq.keys() if word not in reduced]  

#l = "the door handle is broken because where can i buy a new door handle ."
#l2 = "working in the same familiar print environment of QuarkXPress 8 you can take existing print jobs to Flash or create new Flash projects in minutes - no additional purchase or coding required ! watch a video on how to create sophisticated Flash designs in QuarkXPress 8 "
#print(substring_reduction(l))