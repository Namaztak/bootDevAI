from functions.write_file import write_file

print("Start of tests")
print("====================================")
print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))
print("====================================")
print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
print("====================================")
print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))
print("End of tests")