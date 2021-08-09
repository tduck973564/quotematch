def pushStringTo(string, array):
    if string != "":
        array.append(string)
    return ("", array)

def quoteMatch(input): 
    current = ""
    output = []
    inQuote = False

    for character in input:
        if inQuote:
            if character == '"':
                inQuote = False
                current, output = pushStringTo(current, output)
                current = ""
            else:
                current += character

        elif not inQuote:
            if character == '"':
                inQuote = True
                current, output = pushStringTo(current, output)
                current = ""
            elif character == ' ':
                current, output = pushStringTo(current, output)
                current = ""
            else:
                current += character

    current, out = pushStringTo(current, output)

    return out

print(
    quoteMatch(
        'Hello "Hello there" ghgh"hello""hello world"hello, world vhialjklh vsfdkjlkjhvsfd sfdvlkjhsfdkjhsfdkjh fdskjhsdfjhfdh fds fdskj hsfdkjh sfdkfd hsfdvsdf sfdkjhdfsfdsa'
    )
)
