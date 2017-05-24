from bs4 import BeautifulSoup
from urllib2 import urlopen

BASE_URL = "http://profiles.asee.org"

def make_soup(url):
    html = urlopen(url).read()
    return BeautifulSoup(html, "lxml")

def get_school_links(profiles_url):
    soup = make_soup(profiles_url)
    link = soup.find("tbody")
    school_links = []
    for td in link.findAll("tr.td"):
        school_links.append(BASE_URL + td.a["href"]) 
    return school_links

def get_undergrad_enrollment(link_list):
    undergrad_enrollment_links = []
    for link in link_list:
        undergrad_enrollment = link.replace("screen/1", "screen/20")
        undergrad_enrollment_links.append(undergrad_enrollment)
    return undergrad_enrollment_links

def get_undergrad_degrees(link_list):
    undergrad_degree_links = []
    for link in link_list:
        undergrad_degrees = link.replace("screen/1", "screen/21")
        undergrad_degree_links.append(undergrad_degrees)
    return undergrad_degree_links

def get_grad_enrollment(link_list):
    grad_enrollment_links = []
    for link in link_list:
        grad_enrollment = link.replace("screen/1", "screen/27")
        grad_enrollment_links.append(grad_enrollment)
    return grad_enrollment_links

def get_grad_degrees(link_list):
    grad_degree_links = []
    for link in link_list:
        grad_degrees = link.replace("screen/1", "screen/28")
        grad_degree_links.append(grad_degrees)
    return grad_degree_links

if __name__ == '__main__':
    profiles_page = ("http://profiles.asee.org")

    school_links = get_school_links(profiles_page)

    #undergrad_enrollment_links = get_undergrad_enrollment(school_links)
    #undergrad_degrees = get_undergrad_degrees(school_links)
    #grad_enrollment = get_grad_enrollment(school_links)
    #grad_degrees = get_grad_degrees(school_links)

    data = []

    #for link in schools:
    #    winner = get_undergrad_enrollments(link)
    #    data.append(winner)
    #    sleep(1) # be nice

    print school_links
