import urllib2
import cgi

def get_page(url):
    try:
        return urllib2.urlopen(url).read()
    except:
        return ""

def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1: 
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote

def get_all_links(page):
    links = []
    while True:
        url, endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links

def escape_html(string):
    return cgi.escape(string, quote = True)

def html_removal(contents):  ## Removes all html tags from each cell.
    html_start = contents.find('<')
    if html_start == -1:
        return contents
    html_end = contents.find('>')
    if html_end == -1:
        return contents
    return html_removal(contents[:html_start]) + html_removal(contents[html_end + 1:])

def replace_half(contents):  ## Changes "&#189;" to ".5"
    for i in range(len(contents) - 5):
        if contents[i:i + 6] == '&#189;':
            return contents[:i] + '.5' + replace_half(contents[i + 6:])
    return contents

def remove_junk(contents, junk_list):  ## Removes all additional html junk for cleaner-looking output.
    found = True
    while found:
        found = False
        for junk in junk_list:
            if len(contents) >= len(junk):
                for char in range(len(contents) - (len(junk) - 1)):
                    if contents[char:char + len(junk)] == junk:
                        contents = contents[:char] + contents[char + len(junk):]
                        found = True
                        break
    return contents

def clean_up(contents):  ## Removes all additional html code that may have been missed by the previous procedures.
    for i in range(len(contents)):
        if contents[i] == '>':
            return contents[i + 1:]
    return contents

def remove_spaces(contents): ## Recursively eliminates all white space.
    if len(contents) == 0:
        return contents
    if contents[0] == ' ':
        return remove_spaces(contents[1:])  ## Eliminates leading white space.
    if contents[-1] == ' ':
        return remove_spaces(contents[:-1])  ## Eliminates trailing white space.
    for char in range(len(contents) - 1):
        if contents[char] == ' ':
            if contents[char + 1] == ' ':
                return remove_spaces(contents[:char] + contents[char + 1:])  ## Eliminates spaces between words if there is more than 1 space.
    return contents

## The following procedure, get_all_tables, is based on the get_next_target procedure we used in class.
## It takes as its input the raw html from a url and returns a list of tables as its output.
## Each table is a list of rows, and each row is a list of cells. If there are no tables, the output is an empty list.

def get_all_tables(page):
    start_point = 0
    end_point = len(page)
    all_tables = []
    tables = 0
    while start_point < end_point:
        start_table = page.find('<table', start_point)  # finds the next table in the page.
        if start_table == -1:  # no more tables have been found.
            #print 'found', tables, 'tables'
            return all_tables  # returns our list of tables.
        tables += 1
        end_table = page.find('</table>', start_table)  # finds the end of this table.
        table = []
        while start_table < end_table:  # makes sure we have not moved on to the next table.
            start_row = page.find('<tr', start_table)  # finds the next row in the current table.
            if start_row < end_table and start_row != -1:
                end_row = page.find('</tr>', start_row)  # finds the end of the current row.
                row = []
                header = False
                while start_row < end_row:  # makes sure we have not moved on to the next row.
                    start_cell = page.find('<td', start_row)  # finds the next cell in this row.
                    start_header = page.find('<th', start_row)  # finds the next header cell in this row.
                    if start_header >= 0 and start_header < start_cell and start_header < end_row:  # tests whether or not the header is the next cell in this row.
                        start_cell = start_header
                        header = True
                    if start_cell < end_row and start_cell != -1:  # tests if we have reached the end of the row.
                        start_contents = page.find('>', start_cell)  # finds the beginning of the cell's contents.
                        if header:
                            end_contents = page.find('</th>', start_contents + 1)
                        else:
                            end_contents = page.find('</td>', start_contents + 1)  # finds the end of the cell's contents.
                        contents = page[start_contents + 1:end_contents]  # the contents of the cell.

                        ## The following 5 procedures are explained above.
                        ## They are supposed to remove all unwanted html tags from the contents.
                        
                        contents = html_removal(contents)
                        contents = remove_junk(contents, ['&nbsp;', '\n', '\t', '\x93', '\x94', '&#177;', '\r'])  # This is a list of all the junk you want to remove.
                        contents = replace_half(contents)
                        contents = remove_spaces(contents)
                        contents = clean_up(contents)

                        contents = escape_html(contents)
                        
                        row.append(contents)  # adds this cell to the current row.
                        start_row = end_contents  # establishes the point from which we will be searching for the next cell.
                    else:
                        break
                table.append(row)  # adds this row to the current table.
                start_table = end_row  # establishes the point from which we will be searching for the next row.
            else:
                break
        all_tables.append(table)  # adds this table to the list of all tables.
        start_point = end_table  # establishes the point from which we will be searching for the next table.
            
    return all_tables

## Uncomment and run the following code to view a sample of the output. Try some different urls to see if it works with different pages.

#url = 'http://espn.go.com/nba/standings'
##url = "http://www.nfl.com/stats/categorystats?tabSeq=2&statisticCategory=GAME_STATS&conference=ALL&role=TM&season=2012&seasonType=REG"
##print 'retreiving page...'
##page = get_page(url)
##print
##
##tables = get_all_tables(page)
##
##for table in tables:
##    print '--------------------------------'
##    for row in table:
##        print row
