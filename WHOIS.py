import whois
import socket
import sys

#this is a list of websites that we will be using to test the whois module
sites = ["facebook.com", "google.com", "spotify.com","whatsapp.com"]

#this shows the organization of the site using the whois module in this list comprehension
companies = [whois.whois(s).org for s in sites]
creation_dates = [whois.whois(s).creation_date for s in sites]
server_name = [whois.whois(s).name_servers for s in sites]
emails = [whois.whois(s).emails for s in sites]

print(companies)
print(creation_dates)
print(server_name)
print(emails)

#this is the code that will print the site with the earliest creation date
print(sites[creation_dates.index(min(creation_dates))])