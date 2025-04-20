import sys


def string_check(s):
    if not s:
        return "Please Enter a string"
    special_characters = ["$", "@", "#", "%", "^", "&", "*", "!"]
    for i in range(len(s) - 1):
        if s[i] in special_characters and s[i + 1].isdigit():
            return s[i + 1]
    return -1


if __name__ == "__main__":
    # print("sys.argv from child.py:", sys.argv)
    print(string_check(sys.argv[1]))
    # string_check("input2:", sys.argv[2])
    # string_check("input3:", sys.argv[3])

print