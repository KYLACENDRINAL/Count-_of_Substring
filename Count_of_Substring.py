# Return the count of a given substring from a string

# pseudocode

# Define the function of counting emma occurences
def count_emma_occurences(input_string):
    return input_string.lower().count("emma")

given_string="Emma is a good developer. Emma is a writer"
result=count_emma_occurences(given_string)

# Print result
print (f"Emma appears {result} times")