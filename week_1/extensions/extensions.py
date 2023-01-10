# Prompts the user for the name of a file
file = input("File name: ").lower().strip()

# Output the file extension
if "gif" in file:
    print("image/gif")
elif "jpg" in file:
    print("image/jpeg")
elif "jpeg" in file:
    print("image/jpeg")
elif "png" in file:
    print("image/png")
elif "pdf" in file:
    print("application/pdf")
elif "txt" in file:
    print("text/plain")
elif "zip" in file:
    print("application/zip")
else:
    print("application/octet-stream")

"""
Be sure to test each of the other file formats
vary the casing of your input and “accidentally” add spaces
on either side of your input before pressing enter.
Your program should behave as expected, case- and space-insensitively.
"""