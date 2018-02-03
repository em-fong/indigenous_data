#!/usr/local/bin/python3

#import statements to use other technologies
import cgi
import sqlite3

#error reporting
import cgitb
cgitb.enable()

#print elements of the HTML file
print("Content-Type: text/html\r\n\r\n")
print("<html><head>")
print("<head>")
print('<title>Database Design Assignment #5</title>')
print('<link rel="stylesheet" type="text/css" href="native.css">')
print("</head>")
print("<body>")
print('<h1 align="CENTER">Assignment #5: Native/Indigenous Communities in the United States</h1>')

#open & connect database
sql_connection = sqlite3.connect("native.db")
sql_cursor = sql_connection.cursor()

#get html variables
form = cgi.FieldStorage()
population = form["pop"].value
limit_amt = form["records"].value
sort = form["sort"].value

#create SQLite query

query = "SELECT name, pop2010 FROM native WHERE pop2010 " + population + " ORDER BY pop2010 " + sort +" LIMIT "+ limit_amt

print("<p>Query: " + query + "</p>\n")
print("<hr />\n")

#execute query
sql_cursor.execute(query)

#format nicely in tables
print("<table>")
print("<tr>")
print("\t<th>Tribe/Community Name</th>")
print("\t<th>Population</th>")
print("</tr>")

#print data
for name, pop2010 in sql_cursor:
    print("<tr>")
    print("\t<td>" + name + "</td>")
    print("\t<td>" + str(pop2010) + "</td>")
    print("</tr>")

print("</table>\n")

#close connection and finish page
sql_cursor.close()
print("</body>")
print("</html>")
