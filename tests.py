from functions.get_files_info import get_files_info


print("====================================")
print("Testing get_files_info(\"calculator\", \".\")")
get_files_info("calculator", ".")
print("====================================")
print("Testing get_files_info(\"calculator\", \"pkg\")")
get_files_info("calculator", "pkg")
print("====================================")
print("Testing get_files_info(\"calculator\", \"/bin\")")
get_files_info("calculator", "/bin")
print("====================================")
print("Testing get_files_info(\"calculator\", \"../\")")
get_files_info("calculator", "../")
print("====================================")

print("End of tests")