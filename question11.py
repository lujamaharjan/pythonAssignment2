"""
1. Create a variable, filename. Assuming that it has
a three-letter extension, and using slice operations, 
find the extension. For README.txt, the extension should
be txt. Write code using slice operations that will give the
name without the extension. Does your code work on filenames
of arbitary length?
"""

filename = 'abcdefghi.docx'

# Assuming extension is only 3 char
# name_without_extenison = filename[:-4] 

# for arbitary extension length
index = filename.index('.')
name_without_extension = filename[:index] 
print(name_without_extension)
