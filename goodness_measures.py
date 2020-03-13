from collections import Counter, defaultdict
from utils import process_line

def ngrams(input, n):
    # Adapted from https://stackoverflow.com/a/13424002
    input = input.split(' ')
    output = {}
    for i in range(len(input)-n+1):
        g = ' '.join(input[i:i+n])
        output.setdefault(g, 0)
        output[g] += 1
    return output

def substring_reduction(line, lower=2, upper=4):
    process_line(line)  # handles leading and trailing whitespaces

    freq = dict()
    for i in range(lower, upper+1):
        freq.update(ngrams(line, i))    # get all ngrams of length i that appear at least once


    freq = {k: freq[k] for k in freq if freq[k] > 1}
    reduced = set()
    for str_i in freq.keys():
        for str_j in freq.keys():
            if str_i != str_j and str_i in str_j and freq[str_i] == freq[str_j]:
                # str_i is a substring of str_j and have the same frequency as str_j,
                # therefore str_i is reducable by str_j
                reduced.add(str_i)
    return [word for word in freq.keys() if word not in reduced]

def accessor_variety(line, lower=2, upper=4):
    if len(line) == 0:
      return None

    process_line(line)
    line = line.split(' ')
    line = '<sos> ' + line + ' <eos>'  # add start-of-sentence and end-of-sentence tokens

    vocab = Counter()
    predecessors, successors = defaultdict(set), defaultdict(set)

    for n in range(lower, upper+1):
        for i in range(1, len(line)-n):
          g = ' '.join(line[i:i+n])
          predecessors[g].add(line[i-1])
          successors[g].add(line[i+n])
          vocab[g] += 1

    # compute AV_score
    max_av_predescessor = (None, 0)
    max_av_successor = (None, 0)
    for g in vocab:
        if len(predecessors[g]) > max_av_predescessor[1]:
            max_av_predescessor = (g, len(predecessors[g]))
        if len(successors[g]) > max_av_successor[1]:
            max_av_successor = (g, len(successors[g]))

    return max_av_successor[0], min(max_av_predescessor, max_av_successor)

def description_length_gain(line):
    pass
