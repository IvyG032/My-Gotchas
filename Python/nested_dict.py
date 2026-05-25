#Write a function called pivot_library. pivot_library takes
#as input one parameter, a list of 3-tuples. Each tuple in
#the list has three items: the first item is a book title
#(a string), the second item is the book's author (a
#string), and the third item is the book's ISBN number (a
#string).
#
#pivot_library should return a dictionary. In the dictionary
#that it returns, the keys should be the ISBN numbers, and
#the values should be new dictionaries. Each new dictionary
#should have two keys: "title" and "author". Their values
#should correspond to the first and second items from the
#original 3-tuple.
#
#For example:
#
# books = [("Of Mice and Men", "John Steinbeck", "978-0-140-17739-8"),
#          ("Introduction to Computing", "David Joyner", "978-1-260-08227-2")]
# pivot_library(books)
#   -> {"978-0-140-17739-8": {"title": "Of Mice and Men", "author": "John Steinbeck"},
#       "978-1-260-08227-2": {"title": "Introduction to Computing", "author": "David Joyner"}}


#Write your function here!
def pivot_library(book_info):
    library_dict = {}

    # 通过解包给元组里的每一项直接命名
    for title, author, isbn in book_info:
        # 直接构建内层字典，清晰明了
        library_dict[isbn] = {
            "title": title,
            "author": author
        }

    return library_dict

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print (although the order of the keys may vary):
#
#{"978-0-140-17739-8": {"title": "Of Mice and Men", "author": "John Steinbeck"}, 
# "978-1-260-08227-2": {"title": "Introduction to Computing", "author": "David Joyner"}}

books = [("Of Mice and Men", "John Steinbeck", "978-0-140-17739-8"), ("Introduction to Computing", "David Joyner", "978-1-260-08227-2")]
print(pivot_library(books))


# 原解法：
# def pivot_library(book_info):
#     book_ISBN = {}

#     for info in book_info:
#         book_ISBN[info[2]] = {}
#         book_ISBN[info[2]]["title"] = info[0]
#         book_ISBN[info[2]]["author"] = info[1]

#     return book_ISBN