import re

index = {} 

#opens and read the text file
file_path = "/Users/faizanshamsi/Desktop/input.txt"
with open(file_path, "r", encoding="utf-8") as file:
    file_contents = file.read()

#converts "\f" into an actual page break character
file_contents = file_contents.replace("\\f", "\f")

#converts text to lowercase before processing
file_contents = file_contents.lower()

#removes punctuation at the start and end of words but preserve internal punctuation
file_contents = re.sub(r'\b[^\w\s]+|[^\w\s]+\b', '', file_contents)

#splits text into pages using actual form feed (\f)
pages = file_contents.split("\f")

#iterate over pages and index words
for counter, page in enumerate(pages, start=1):
    words = re.findall(r'\b\w+\b', page)  #extracts only valid words

    for word in words:
        if word not in index:
            index[word] = []  #initializes empty list if word is not already in dictionary
        if counter not in index[word]:  #avoids duplicate page numbers
            index[word].append(counter)  #appends the page number

#prints results alphabetically, mirroring an index of a textbook
for word, pages in sorted(index.items()):
    print(f"{word}: {pages}")
