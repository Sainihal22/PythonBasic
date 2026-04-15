# File Handling

# File handling means reading from and writing to files using Python

# Open() : Function

# file = open("filename.txt", "mode")

# 1. Mode : r --> Read only (default)
#             --> file must exist 
#             --> if no file it raises an error

# 2. Mode : w --> Write only
#             --> Creates a file if not exists
#             --> OVERWRITES if exists

# 3. Mode : a --> Append
#             --> creates a file if not exists
#             --> if file exists then whatever content comes it adds at the end

# 4. Mode : r+ --> Reads and Writes
#              --> file must exist
#              --> if no file it raises an error

# 5. Mode : x --> Creates a file
#             --> Creates new file
#             --> error if file already exists

# with statement : Always use this

# file = open("test.txt", "r")
# content = file.read()
# file.close()    # must statement

# with open("test.txt", "r") as file:  # automatically closes the file
#     content = file.read()

# 1. It Automatically closes the file
# 2. Even if errors occurs inside, there is no need to call file.close()
# 3. Production Safe

# Writing to a file

# with open("student.txt", "w") as file:
#     file.write("Alice\n")
#     file.write("Bob\n")
#     file.write("Charlie\n")

# writelines() : Write List of Strings

# students = ["Alice\n", "Bob\n", "Charlie\n"]

# with open("student_writelines.txt", "w") as file:
#     file.writelines(students)

# Append Mode : Add to end
# with open("student.txt", "a") as file:
#     file.write("David\n")
#     file.write("Eve\n")

# Reading from a file

# read() : Read Entire File

# with open("student.txt") as file:
#     content = file.read()
#     print(content)

# readline() : Read one line at a time

# with open("student.txt") as file:
#     line1 = file.readline()
#     line2 = file.readline()
#     line3 = file.readline()
#     line4 = file.readline()
#     line5 = file.readline()
#     line6 = file.readline()
#     line7 = file.readline()
#     # print(line1)
#     print(line1.strip())
#     print(line2.strip())
#     print(line3.strip())
#     print(line4.strip())
#     print(line5.strip())
#     print(line6.strip())
#     print(line7.strip())

# readlines() : Reads all lines as a list

# with open("student.txt") as file:
#     lines = file.readlines()
#     # print(lines)
#     for line in lines:
#         print(line.strip())

# Loop directly : Most Efficient

# with open("student.txt") as file:
#     for line in file:
#         print(line.strip())

# read()       →  entire file into one string   →  small files
# readlines()  →  entire file into list         →  small files
# loop         →  one line at a time            →  large files

# File Handling with Exception

# try:
#     with open("student.txt", "r") as file:
#         content = file.read()
#         print(content)
# except FileNotFoundError:
#     print("File does not exist")
# except PermissionError:
#     print("No permission to read file")
# except Exception as e:
#     print(f"Error : {e}")

# If any modules / packages not present in .venv then below is the command to install

# pip install <package-name>

# os Module : File Operations

# import os

# check if file exists or not
import os

# if os.path.exists(r"C:\Users\Sai_nihal_Kothi\Downloads\Sample\downloads_1.txt"):
#     print("File exists")
# else:
#     print("File not found")

# Unicodeescape Error

# print(os.path.isfile("student.txt"))
# print(os.path.isdir("features"))

# Create a folder or directory

# folder_name = "features"
# os.makedirs(folder_name,exist_ok=True)

# Get File Size

# size = os.path.getsize("student.txt")
# print(f"Size : {size} bytes")

# List of files in directory

# files = os.listdir(".") # . means current directory

# for f in files:
#     print(f)

# Delete file

# os.remove("student.txt")

# if os.path.exists("student_writelines.txt"):
#     os.remove("student_writelines.txt")
#     print("Deleted")

# Rename File

# os.rename("student_1.txt", "student.txt")

# Joining a folder and a file

folder = "features"
filename = "feature.txt"

path = os.path.join(folder, filename) # / : linux / mac, \ : windows

with open(path, "w") as file:
    file.write("David\n")
    file.write("Eve\n")




