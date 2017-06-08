# https://www.codewars.com/kata/5202ef17a402dd033c000009


def title_case(title, minor_words=''):
    minor_list = list(minor_words.lower().split(" "))
    title_list = list(title.lower().split(" "))
    title_list[0] = title_list[0].title()
    return " ".join(list(map(lambda w: w if w in minor_list else w.title(), title_list)))
