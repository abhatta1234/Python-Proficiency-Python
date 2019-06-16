#Given a HTML code snippet of N Lines, print start, end tags and empty tags separately.

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :",tag)
        for _ in attrs:
            print("->",_[0],">",_[1])

    def handle_endtag(self, tag):
        print("End :",tag)

    def handle_startendtag(self,tag,attrs):
        print("Empty :",tag)
        for _ in attrs:
            print("->",_[0],">",_[1])

parser = MyHTMLParser()

for i in range(int(input())):
    parser.feed(input())

