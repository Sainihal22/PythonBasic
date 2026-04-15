# Exception Handling

# An Exception is an error that happens while program is running

# print(10/0)
# print(int("abc"))
# print(x)

# Without handling

# Program crashes
# All code after error --> never runs
# User sees ugly error message

# With handling

# Program handles eror gracefully
# Shows friendly message
# Continues running

# Exception              When it happens
# ──────────────────────────────────────────────────────
# ZeroDivisionError      divide by zero
# ValueError             wrong value type  int("abc")
# TypeError              wrong type        "a" + 1
# NameError              variable not defined
# IndexError             list index out of range
# KeyError               dict key not found
# FileNotFoundError      file does not exist
# AttributeError         method does not exist on object
# ImportError            module not found

# Basic structure

# try:
#     # code
# except:
#     # runs if error occurs

# logs : Loggings / logging : it is a way of displaying errors, warnings, output in production/deployment based env.

# import logging
# logging.basicConfig(level=logging.DEBUG)
# logging.basicConfig(level=logging.INFO)
# logging.basicConfig(level=logging.WARNING)
# logging.basicConfig(level=logging.ERROR)
# try:
#     result = 10/0
#     logging.info(result)
#     # print(result)
# except:
#     logging.info(" Something went wrong")

# logging.debug(" Debug Checkpoint")
# logging.info(" App is still running")
# logging.warning(" App is giving warning")
# logging.error(" There is an error in the APP")

# ERROR
# WARNING
# INFO
# DEBUG

# try:
#     result = 10/0
#     logging.info(result)
# # except ZeroDivisionError:
# #     logging.info("Cannot divide by zero")
# # except Exception as e:
# #     logging.info("Something went wrong : ", e)
# except ZeroDivisionError:
#     logging.info("Cannot divide by zero")

# logging.info("App is running")

# try:
#     n = int("ABC")
# # except Exception as e:
# #     logging.info("Something went wrong : ", e)
# except ValueError:
#     logging.info("Invalid Literal")

# def divide(a,b):
#     result = a / b
#     print(result)

# try:
#     divide(5, 10) # Happy Path
#     divide(4, 0)
#     divide("a", 10)   
# except TypeError:
#     print("Enter only numbers")
# except ZeroDivisionError:
#     print("Cannnot divide by zero")

# else : Runs when no Error

# try:
#     result = 10/5
# except ZeroDivisionError:
#     print("Not divided by zero")
# else:
#     print(f"Success : {result}")

# finally : Always Runs
# Its useful for cleanup like : closing files, closing connections(db, aws, s3, etc)

# try:
#     result = 10/5
# except ZeroDivisionError:
#     print("Not divided by zero")
# else:
#     print(f"Success : {result}")
# finally:
#     print("This always runs")

# Full structure

# try:
#     # risky code
# except SpecificError as e:
#     # Handle it
# except Exception as e:
#     # handle it
# else:
#     # runs only if there is no error
# finally:
#     # always runs

# Custom Exceptions

# def check_age(age):
#     if age < 0:
#         raise Exception("Age cannot be negative")
#     if age > 100:
#         raise Exception("Age is too large")
#     print(f"Age : {age}")

# try:
#     check_age(-25)
# except Exception as e:
#     print("Invalid Age Error : ", e)

# Exception Handling, try catch block, try except block