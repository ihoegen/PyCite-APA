#Created 2015 By Ian Hoegen, Hoegen Developments
def apa():
    #Picks what type of work is being cited
    document_type = raw_input('Are you citing a website, a newspaper, a book,'\
                              ' or a journal? ')
    print""
    document_type = document_type.lower()
    if document_type == 'website':
        website()
    elif document_type == 'newspaper':
        newspaper()
    elif document_type == 'book':
        book()
    elif document_type == 'journal':
        journal()
    else:
        print "Please choose a website, a newspaper, a book, or a journal"
        apa()
             

def print_m(citation):
    #helper function to print to file and to console
    print "Your citation is: "
    print ""
    print citation
    f = open('references.odt', 'a')
    f.write(citation + '\n')
    f.write('')
    
def year():
    #Defines the year of the work
    year = raw_input("What year was this published, followed by the month and"\
                     "date. Enter n.d if unknown ")
    print""
    return  "(%s) " % (year)

def title():
    #Recieves and formats the title
    title = raw_input("What is the title of the work? ")
    print""
    title_first = title[0].upper()
    title_rest = title[1:].lower()
    title = title_first + title_rest
    return  "%s. " % (title)

def info():
    #Recieves and formats the author info, and joins it with the year and title
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
        author_cite = "".join(author_list)
    else:
        print "You need to enter a number between 1 and 4"
        print ''
        info()
    return author_cite + title() + year()

def website():
    #Website citations
    retrieved_from = raw_input("What is the address of the website? ")
    print''
    date = raw_input("What day did you visit this site? ")
    print''
    retrieved_from = "Retrieved %s from %s" % (date, retrieved_from)
    
    citation = info() + retrieved_from
    print_m(citation)
    exit_messages()

def newspaper():
    #Newspaper Citations
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
    
    citation = info() + publisher + site
    print_m(citation)
    exit_messages()

def book():
    #Book citations
    location = raw_input('Where was the book published? ')
    print''
    location = location[0].upper() + location[1:].lower()
    location = "%s: " % (location)
    publisher = raw_input("What is the name of the publishing company? ")
    print''
    publisher = publisher[0].upper() + publisher[1:].lower()
    publisher = "%s." % (publisher)
    citation = info() + location + publisher
    print_m(citation)
    exit_messages()

def journal():
    #Journal Citation
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
    citation = info() + journal_name + web_and_date
    print_m(citation)
    exit_messages()

def exit_messages():
    #messages displayed after the citation
    print ""
    print "Your file can be found in the document references.odt"
    print""
    print "To copy  from here, right click the title bar, highlight over the"\
          "edit item and select mark. Highlight the citation and hit enter on"\
          "your keyboard. Your citation is now ready for use"
    print ""
    more = raw_input('Would you like to PyCite another item? y/n ')
    if more.lower() == "y":
        apa()
    else:
        print "Goodbye"
        exit()
        
print "Welcome to PyCite APA Free Edition"
apa()