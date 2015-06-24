__author__ = "Ian Hoegen"
__date__ = "$Jun 24, 2015 10:55:26 AM$"
#Created 2015 By Ian Hoegen, Hoegen Developments
#helper function to print
def print_m(citation):
    print "Your citation is: "
    print ""
    print citation
    f = open('references.odt', 'w+')
    f.write(citation )
    f.write('')
#Starts the cylce
#in case someone screws up
def apa_error():
    type_of_document = raw_input('Please choose website, book, journal or newspaper ')
    type_of_document = type_of_document.lower()
    if type_of_document == 'website':
        apa_web()
    elif type_of_document == 'newspaper':
        apa_news()
    elif type_of_document == 'book':
        apa_book()
    elif type_of_document == 'journal':
        apa_journal()
    else:
        apa_error()
#Picks what type of work is being cited
def apa():
    type_of_document = raw_input('Are you citing a website, a newspaper, a book, or a journal? ')
    type_of_document = type_of_document.lower()
    if type_of_document == 'website':
        apa_web()
    elif type_of_document == 'newspaper':
        apa_news()
    elif type_of_document == 'book':
        apa_book()
    elif type_of_document == 'journal':
        apa_journal()
    else:
        apa_error()
#Helper functin for title
def apa_title():
    title = raw_input("What is the title? ")
    title_first = title[0].upper()
    title_rest = title[1:].lower()
    title = title_first + title_rest
    return "%s. " % (title)
#Compiles the author info
x = 0
n = 0
author_list = []
def apa_author_error():
    apa_author()
def apa_author():
    global author_list, x, n
    amount_authors = raw_input("How many authors are there? Select 1-4.")
    if amount_authors == "1" or amount_authors == "3" or amount_authors == "2" or amount_authors == "4":
        n = int(amount_authors)
        while x < n:
            x += 1
            author_first = raw_input("What is the author's first name? ")
            author_last = raw_input("What is the author's last name? ")
            author_last = author_last[0].upper() + author_last[1:].lower()
            author_first = author_first[0].upper()
            author_full = "%s, %s. " % (author_last, author_first)
            author_list.append(author_full)
    else:
        print "You need to enter a number between 1 and 4"
        apa_author_error()
def author_declare(z):
    if n == 1:
        return str(author_list[0])
    elif n == 2:
        return str(author_list[0]) + str(author_list[1])
    elif n  == 3:
        return str(author_list[0]) + str(author_list[1]) + str(author_list [2])
    else:
        return str(author_list[0]) + str(author_list[1]) + str(author_list[2]) + str(author_list[3])
title = None
author = None
year = None
author_cite = None
def apa_info():
    global title, author, year, author_cite
    title = apa_title()
    author = apa_author()
    year = raw_input("What year was this published, followed by the month and date. Enter n.d if unknown ")
    year =   str(year)+ " "
    author_cite = author_declare(n)
def apa_web():
    apa_info()
    retrieved_from = raw_input("What is the address of the website? ")
    date = raw_input("What day did you visit this site? ")
    retrieved_from = "Retrieved %s from %s" % (date, retrieved_from)
    citation = author_cite + year + title + retrieved_from
    print_m(citation)
    copy()
    again()
def apa_news():
    apa_info()
    publisher = raw_input("What is the name of the publishing company? ")
    page = raw_input("What page(s) did you find the article on? ")
    publisher = ("%s, pp. %s.") % (publisher, page)
    electronic = raw_input("Was this retrieved from a website? ")
    electronic = electronic.lower()
    if electronic == 'yes':
        site = raw_input('What is the website you found it on? ')
        date = raw_input("What day did you last visit this site? ")
        site = "Retrieved %s from %s" % (date, site)
    else:
        site = " "
    citation = author_cite + year + title + publisher + site
    print_m(citation)
    copy()
    again()
def apa_book():
    apa_info()
    location = raw_input('Where was the book published? ')
    location = location[0].upper() + location[1:].lower()
    location = "%s: " % (location)
    publisher = raw_input("What is the name of the publishing company? ")
    publisher =publisher[0].upper() + publisher[1:].lower()
    publisher = "%s." % (publisher)
    citation = author_cite + year + title + location + publisher
    print_m(citation)
    copy()
    again()
def apa_journal():
    apa_info()
    journal_name = raw_input('What is the name of the journal? ')
    volume = raw_input('What volume number is it? ')
    pages = raw_input('What is the page range of the article? ')
    doi = raw_input("What is the DOI number? ")
    journal_name = " %s, %s, %s. doi: %s" % (journal_name, volume, pages, doi)
    citation = author_cite + year + title + journal_name
    print_m(citation)
    copy()
    again()
#Welcome Messages
def copy():
    print ""
    print "Your file can be found in the document references.odt"
    print "To copy  from here, right click the title bar, highlight over the edit item and select mark. Highlight the citation and hit enter on your keyboard. Your citation is now ready for use"
def again():
    more = raw_input('Would you like to PyCite another item? ')
    if more.lower() == "yes":
        apa()
    else:
        print "Goodbye"
        exit()
print "Welcome to PyCite APA Free Edition, for MLA and CMS be sure to download the full version."
apa()
