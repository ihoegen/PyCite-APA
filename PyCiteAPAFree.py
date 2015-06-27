#Created 2015 By Ian Hoegen, Hoegen Developments
#Picks what type of work is being cited
def apa():
    type_of_document = raw_input('Are you citing a website, a newspaper, a book, or a journal? ')
    print""
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
        print "Please choose a website, a newspaper, a book, or a journal"
        apa()
#helper function to print
def print_m(citation):
    print "Your citation is: "
    print ""
    print citation
    f = open('references.odt', 'w+')
    f.write(citation)
    f.write('')
#Defines the year
def year():
    year = raw_input("What year was this published, followed by the month and date. Enter n.d if unknown ")
    print""
    return  "(%s)" % (year)
#Helper function for title
def apa_title():
    title = raw_input("What is the title of the work? ")
    print""
    title_first = title[0].upper()
    title_rest = title[1:].lower()
    title = title_first + title_rest
    return  "%s. " % (title)
#Compiles the author info
def apa_author():
    author_list = []
    x = 1
    amount_authors = raw_input("How many authors are there? Select 1-4. ")
    print''
    amount_authors = int(amount_authors)
    if amount_authors >= 1 and amount_authors <= 4:
        n = amount_authors
        while x <= n:
            author_first = raw_input("What is the author's first name? ")
            author_last = raw_input("What is the author's last name? ")
            print''
            author_last = author_last[0].upper() + author_last[1:].lower()
            author_first = author_first[0].upper()
            author_full = "%s, %s. " % (author_last, author_first)
            author_list.append(author_full)
            x += 1
        if n == 1:
            author_cite = str(author_list[0])
        elif n == 2:
            author_cite = str(author_list[0]) + str(author_list[1])
        elif n  == 3:
            author_cite = str(author_list[0]) + str(author_list[1]) + str(author_list [2])
        else:
            author_cite = str(author_list[0]) + str(author_list[1]) + str(author_list[2]) + str(author_list[3])
    else:
        print "You need to enter a number between 1 and 4"
        print ''
        apa_author()
    return author_cite + apa_title() + year()
#Website citations
def apa_web():
    retrieved_from = raw_input("What is the address of the website? ")
    print''
    date = raw_input("What day did you visit this site? ")
    print''
    retrieved_from = "Retrieved %s from %s" % (date, retrieved_from)
    citation = apa_author() + retrieved_from
    print_m(citation)
    copy()
#News Citations
def apa_news():
    publisher = raw_input("What is the name of the publishing company? ")
    print''
    page = raw_input("What page(s) did you find the article on? ")
    print ''
    publisher = ("%s, pp. %s.") % (publisher, page)
    electronic = raw_input("Was this retrieved from a website? y/n ")
    print ''
    electronic = electronic.lower()
    if electronic == 'y':
        site = raw_input('What is the website you found it on? ')
        print ''
        date = raw_input("What day did you last visit this site? ")
        print ''
        site = "Retrieved %s from %s" % (date, site)
    else:
        site = " "
    citation = apa_author() + publisher + site
    print_m(citation)
    copy()
#Book citations
def apa_book():
    location = raw_input('Where was the book published? ')
    print''
    location = location[0].upper() + location[1:].lower()
    location = "%s: " % (location)
    publisher = raw_input("What is the name of the publishing company? ")
    print''
    publisher = publisher[0].upper() + publisher[1:].lower()
    publisher = "%s." % (publisher)
    citation = apa_author() + location + publisher
    print_m(citation)
    copy()
#Journal Citation
def apa_journal():
    journal_name = raw_input('What is the name of the journal? ')
    journal_name = journal_name[0].upper() + journal_name[1]
    print ''
    volume = raw_input('What volume number is it? ')
    print ''
    pages = raw_input('What is the page range of the article? ')
    print ''
    doi = raw_input("What is the DOI number? ")
    print ''
    web = raw_input('Was it found on a website? y/n ')
    web = web.lower()
    if web == "y":
        site = raw_input('What website was it found on? ')
        date = raw_input("What day did you visit it? ")
        web_and_date = " Retrieved from: %s on %s " % (site, date)
    else:
        web_and_date = " "
    journal_name = " %s, %s, %s. doi: %s." % (journal_name, volume, pages, doi)
    citation = apa_author() + journal_name + web_and_date
    print_m(citation)
    copy()
#Welcome Messages
def copy():
    print ""
    print "Your file can be found in the document references.odt"
    print""
    print "To copy  from here, right click the title bar, highlight over the edit item and select mark. Highlight the citation and hit enter on your keyboard. Your citation is now ready for use"
    print ""
    more = raw_input('Would you like to PyCite another item? y/n ')
    if more.lower() == "y":
        apa()
    else:
        print "Goodbye"
        exit()
print "Welcome to PyCite APA Free Edition, for MLA and CMS be sure to download the full version."
apa()