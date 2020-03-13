def process_line(line):
    # Adapted from https://github.com/rsennrich/subword-nmt/blob/master/subword_nmt/apply_bpe.py
    """segment line, dealing with leading and trailing whitespace"""
    out = ""

    leading_whitespace = len(line)-len(line.lstrip('\r\n '))
    if leading_whitespace:
        out += line[:leading_whitespace]

        trailing_whitespace = len(line)-len(line.rstrip('\r\n '))
        if trailing_whitespace and trailing_whitespace != len(line):
            out += line[-trailing_whitespace:]

            return out
