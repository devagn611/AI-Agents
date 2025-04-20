import subprocess


# print("Child output:", result.stdout)
# print("Child error:", result.stderr)
# print("Child return code:", result.returncode)
# print("Child command:", result.args)

# result = subprocess.run(['python3', file_to_call, "abc!5def", "a#4bvc" , "ssss@f3hh"],text=True)

# def run_child_process(file_to_call):
#     try:
#         result = subprocess.run(['python3', file_to_call],text=True)
#         print("Child output:", result.stdout)
#         print("Child error:", result.stderr)
#         print("Child return code:", result.returncode)
#         print("Child command:", result.args)

# run_child_process(file_to_call)


# subprocess.check_output(['python3', file_to_call], input=b"abc!5def")
file_to_call = "child.py"

to_check = ["abc!5def", "a#4bvc", "ss:2ss@f3hh", 465465]

for strs in to_check:
    try:
        result = subprocess.run(['python3', file_to_call, strs],text=True, capture_output=True)
        print("output:", result.stdout)
    except Exception as e:
        print("Error:", e)

    # print("Child error:", result.stderr)
    # print("Child return code:", result.returncode)
    # print("Child command:", result.args)
    # print("Result:", result)

    # result2 = subprocess.check_output(["python3", file_to_call, strs])
    # print("Input:", strs, " -> Result2:", result2.decode("utf-8").strip())






# def dec(func):
#     def wrap(*args):
#         print("dec")
#         return func(*args)

# @dec
# def test():
#     print("test")
