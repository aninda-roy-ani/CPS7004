'''
def combine_sort(text1, text2):
    even = ""
    odd = ""
    for i in range(len(text1)):
        if i%2 == 0:
            odd += text1[i]
        else:
            even += text1[i]

    for i in range(len(text2)):
        if i%2 == 0:
            odd += text2[i]
        else:
            even += text2[i]

    odd_sorted = sort_alphabetical(odd)
    even_sorted = sort_alphabetical(even)
    return(f"even sorted is {even_sorted} and odd sorted is {odd_sorted}")
'''


def combine_sort(text1, text2):
    odd = text1[0::2] + text2[0::2]
    even = text1[1::2] + text2[1::2]
    odd_sorted = sort_alphabetical(odd)
    even_sorted = sort_alphabetical(even)
    return (f"even sorted is {even_sorted} and odd sorted is {odd_sorted}")


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


print(combine_sort("abcd", "shdaj"))

