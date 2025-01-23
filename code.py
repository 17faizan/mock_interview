import re

index = {}  # Dictionary to store word -> [page numbers]

# Sample text with \f as page breaks
file_contents = "This is sample text. Also sample text. \f This is another page. This is another page. \f This is the last page."
#converts the entire text to lowercase before processing
file_contents = file_contents.lower()
#removes punctuation at the start and end of words but preserve internal punctuation
file_contents = re.sub(r'\b[^\w\s]+|[^\w\s]+\b', '', file_contents)
#splits text into pages
pages = file_contents.split("\f")  

for counter, page in enumerate(pages, start=1): 
    words = page.split(" ")  #splits page content into words
    
    for word in words:
        if word:  # Ensure word is not empty after cleaning
            if word not in index:
                index[word] = []  #initializes empty list if word is not already in dictionary
            if counter not in index[word]:  #avoids duplicate page numbers
                index[word].append(counter)  #appends the page number

#prints results alphabetically, mirroing an index of a textbook
for word, pages in sorted(index.items()):
    print(f"{word}: {pages}")

