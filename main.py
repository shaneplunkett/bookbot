def main():
    frankenstein = "books/frankenstein.txt"
    print(get_file_content(frankenstein))
    print(get_word_count(get_file_content(frankenstein)))
    print(get_char_count(get_file_content(frankenstein)))
    print(f"--- Begin report of {frankenstein} ---")
    print()
    print(f"{get_word_count(get_file_content(frankenstein))} words found in document")
    print()
    print(char_report(get_char_count(get_file_content(frankenstein))))
    print()
    print(f"--- End report ---")



def get_file_content(path):
    with open(path) as f:
        return f.read()


def get_word_count(string):
    words = string.split()
    return len(words)


def get_char_count(string):
    char_count = {}
    lst = []
    lowered_string = string.lower()
    for char in lowered_string:
        lst.append(char)
    for char in lst:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count


def char_report(char_count):
    list_of_dics = []
    for char, count in char_count.items():
        char_dict = {"char": char, "count": count}
        if char.isalpha():
            list_of_dics.append(char_dict)
    list_of_dics.sort(reverse=True, key=lambda x: x["count"])
    for dic in list_of_dics:
        print(f"The {dic['char']} was found {dic['count']} times")


main()
