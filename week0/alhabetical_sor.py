def sort_alphabetical(tex):
    text = list(tex)
    for i in range(len(text)):
        for j in range(len(text)-1):
            if text[j+1]<text[j]:
                temp = text[j]
                text[j] = text[j+1]
                text[j+1] = temp
    newt = ""
    for t in text:
        newt += t
    return newt