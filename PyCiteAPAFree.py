#helper function to print
def print_m():
    print "Your citation is: "
    print ""
#Starts the cylce
def apa():
    apa_start()
type_of_document = None
#in case someone screws up
def apa_error():
    global type_of_document
    type_of_document = raw_input('Please choose website, book, journal or newspaper ')
    type_of_document = type_of_document.lower()
    if type_of_document == 'website':
        apa_web()
    elif type_of_document == 'newspaper':
        apa_news()
    elif type_of_document == 'book':
        apa_book()
    elif type_of_documet == 'journal':
        apa_journal()
    else:
        apa_error()
#Picks what type of work is being cited
def apa_start():
    global type_of_document
    type_of_document = raw_input('Are you citing a website, a newspaper, a book, or a journal? ')
    type_of_document= type_of_document.lower()
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
    return "%s. " %(title)
#Figures out names of the author(s)
author_first = None
author_last = None       
def author_1():
    global author_first, author_last
    author_first = raw_input("What is the author's first name? ")
    author_last = raw_input("What is the author's last name? ")
    author_last = author_last[0].upper() + author_last[1:].lower()
    author_first = author_first[0].upper()
author_first2 = None
author_last2 = None 

def author_2():
    global author_first2, author_last2
    author_first2 = raw_input("What is the second author's first name? ")
    author_last2 = raw_input("What is the second author's last name? ")
    author_last2 = author_last2[0].upper() + author_last2[1:].lower()
    author_first2 = author_first2[0].upper()
author_first3 = None
author_last3 = None   

def author_3():
    global author_first3, author_last3
    author_first3 = raw_input("What is the third author's first name? ")
    author_last3 = raw_input("What is the third author's last name? ")
    author_last3 = author_last3[0].upper() + author_last3[1:].lower()
    author_first3 = author_first3[0].upper()
author_first4 = None
author_last4 = None    

def author_4():
    global author_first4, author_last4
    author_first4 = raw_input("What is the fourth author's first name? ")
    author_last4 = raw_input("What is the fourth author's last name? ")
    author_last4 = author_last4[0].upper() + author_last4[1:].lower()
    author_first4 = author_first4[0].upper() 
#Compiles the author info
def apa_author():
    amount_authors = raw_input("How many authors are there? Select 1-4. If you have more than 4 authors, enter 4+ ")
    if amount_authors == "1":
        author_1()
        return "%s, %s. " %(author_last, author_first)
    elif amount_authors == "2":
        author_1()
        author_2()
        return "%s, %s., & %s, %s. " %(author_last, author_first, author_last2, author_first2)    
    elif amount_authors == "3":
        author_1()
        author_2()
        author_3()
        return "%s, %s., %s, %s., %s, %s. " %(author_last, author_first, author_last3, author_first3, author_last2, author_first2) 
    elif amount_authors == "4":
        author_1()
        author_2()
        author_3()
        author_4()
        return "%s, %s., %s, %s., %s, %s., %s, %s. " %(author_last, author_first, author_last4, author_first4, author_last2, author_first2, author_last3, author_first3)     
    elif amount_authors == "4+":
        author_1()
        author_2()
        author_3()
        author_4()
        return "%s, %s., %s, %s., %s, %s., %s, %s. et al. " %(author_last, author_first, author_last4, author_first4, author_last2, author_first2, author_last3, author_first3) 
    else: 
        print "Please enter a valid number"
        apa_author()
def apa_year():
    year = raw_input("What year was this published, followed by the month and date. Enter n.d if unknown ")
    return "(%s). " %(year)
title = None
author = None
year = None
def apa_info():
    global title, author, year
    title = apa_title()
    author = apa_author()
    year = apa_year()
def apa_web():
    apa_info()
    retrieved_from = raw_input("What is the address of the website? ")
    date = raw_input("What day did you visit this site? ")
    retrieved_from = "Retrieved %s from %s" %(date, retrieved_from)
    print_m()
    print author + year + title + retrieved_from
    copy()
    again()
def apa_news():
    apa_info()
    publisher = raw_input("What is the name of the publishing company? ")
    page = raw_input("What page(s) did you find the article on? ")
    publisher = ("%s, pp. %s.") % (publisher, page)
    electronic =  raw_input("Was this retrieved from a website? ")
    electronic = electronic.lower()
    if electronic == 'yes':
        site = raw_input('What is the website you found it on? ')
        date = raw_input("What day did you last visit this site? ")
        site = "Retrieved %s from %s" %(date, site)
    else:
        site = " "
    print_m()
    print author + year + title + publisher + site
    copy()
    again()
def apa_book():
    apa_info()
    location = raw_input('Where was the book published? ')
    location = "%s: " %(location)
    publisher = raw_input("What is the name of the publishing company? ")
    publisher = "%s." % (publisher)
    print_m()
    print author + year + title + location + publisher
    copy()
    again()
def apa_journal():
    apa_info()
    journal_name = raw_input('What is the name of the journal? ')
    volume = raw_input('What volume number is it? ')
    pages = raw_input('What is the page range of the article? ')
    doi = raw_input("What is the DOI number? ")
    journal_name = "%s, %s, %s. doi: %s"%(journal_name, volume, pages, doi)
    print_m()
    print author + year + title + journal_name
    copy()
    again()
    
#Welcome Messages
def copy():
    print ""
    print "To copy, right click the title bar, highlight over the edit item and select mark. Highlight the citation and hit enter on your keyboard. Your citation is now ready for use"
def again():
    more = raw_input('Would you like to PyCite another item? ')
    if more.lower() == "yes":
        welcome()
    else:
        exit()
print "Welcome to PyCite APA Free Edition, for MLA and CMS be sure to download the full version."
apa()
