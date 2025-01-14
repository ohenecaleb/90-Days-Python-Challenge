#Creating a program to read the contents of a file and printing the number of lines and words in the file
#Insert your file path in the file_path variable
f = open("file_path", "r")
#Reading the contents in the file
content = f.read()
# Resetting the file pointer to the beginning of the file
f.seek(0)

#Counting the number of lines in the file
lines = f.readlines()
no_of_lines = len(lines)

#Spliting the content to words
words = content.split()
#Counting the number of words in the file
no_of_words = len(words)



print(content)
print("The number of lines in the file is: ", no_of_lines)
print("The number of words in the file is: ", no_of_words)

#Code by Ohene Caleb