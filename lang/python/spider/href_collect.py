from html.parser import HTMLParser



class HrefCollector(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tag_stack = []
        self.href_stack = []
        self.hrefs = []

    def handle_starttag(self, tag, attrs):
        self.tag_stack.append(tag)
        if(tag == 'a'):
            for key, value in attrs:
                if(key == 'href'):
                    self.href_stack.append(value)
                    break

    def handle_endtag(self, tag):
        if(tag == self.tag_stack[-1]):
            self.tag_stack.pop()
            if(tag == 'a' and len(self.href_stack) > 0):
                self.href_stack.pop()
        else:
            pass

    def handle_data(self, data):
        if(len(self.tag_stack) > 0 and self.tag_stack[-1] == 'a' and len(self.href_stack) > 0):
            self.hrefs.append((self.href_stack[-1], data))




if __name__ == '__main__':
    parser = HrefCollector()
    parser.feed(open('demo.html', 'r', encoding='UTF-8').read())
    # 选链接名开头是'第'的
    for x in [ x  for x in parser.hrefs if x[1][0]=='第' ]:
        print(f'{x[0]} : {x[1]}')
