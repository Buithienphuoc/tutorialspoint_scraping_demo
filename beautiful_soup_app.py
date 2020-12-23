from bs4 import BeautifulSoup
import requests
import lxml

tutorialspoint_website = requests.get('https://www.tutorialspoint.com/')
print("Status code:" + str(tutorialspoint_website.status_code))

# Header of the website
tutorialspoint_header = tutorialspoint_website.headers
print("Header:")
print(tutorialspoint_header)

# Content of the website
tutorialspoint_content = tutorialspoint_website.content
print("Content:")
print(tutorialspoint_content)

# Set up beautiful soup to start playing with tutorialspoint
soup = BeautifulSoup(tutorialspoint_content, 'lxml')

# Get <a> tag (tag contains hyperlinks) in the tutorialspoint homepage
a_tags = soup.find_all("a")

# extract all <a> tags
print("Hyperlinks in the tutorialspoint homepage:")
a_tag_index = 0

# print out <a> tags and det
for a_tag in a_tags:
    a_tag_index += 1
    print("Tag number " + str(a_tag_index) + ":")
    print(a_tag)
    print("\n")
    # Display the text in tag
    print("Text in this tag:")
    tag_text = a_tag.text
    print(tag_text)
    print("\n")
    # Display the link:
    print("Link:")
    try:
        link = a_tag.attrs['href']
        print(link)
    except:
        print("There is not any link")
        pass

    print("\n" + "-----------------------------------------------------------------------" + "\n")
