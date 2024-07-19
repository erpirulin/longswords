words = ["tree", "button", "cat", "window", "defenestrate"]

# Use a list comprehension to filter out words longer than four letters
longwords = [x for x in words if len(x) > 4]
# Display the filtered list
print(longwords)
