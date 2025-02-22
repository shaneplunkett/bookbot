import sys

from stats import get_num_words


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(get_file_content(file_path))} total words")
    print("--------- Character Count -------")
    char_report(get_char_count(get_file_content(file_path)))
    print("============= END ===============")


def get_file_content(path):
    with open(path) as f:
        return f.read()


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
        print(f"{dic['char']}: {dic['count']}")


main()
