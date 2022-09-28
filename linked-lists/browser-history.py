class ListNode():
    def __init__(self, url):
        self.url = url
        self.prev = None
        self.next = None


class BrowserHistory():
    def __init__(self, homepage):
        self.homepage = ListNode(homepage)
        self.current = self.homepage
        """
        :type homepage: str
        """
        

    def visit(self, url):
        new_page = ListNode(url)
        self.current.next = new_page
        new_page.prev = self.current
        self.current = new_page
        

    def back(self, steps):
        current = self.current

        while (steps and current.prev != None):
            current = current.prev
            steps -= 1

        self.current = current
        return current.url
        

    def forward(self, steps):
        current = self.current

        while (steps and current.next != None):
            current = current.next
            steps -= 1

        self.current = current
        return current.url
        


# Your BrowserHistory object will be instantiated and called as such:
obj = BrowserHistory("www.leetcode.com")
obj.visit("www.google.com")
obj.visit("www.facebook.com")
obj.visit("www.apple.com")
obj.visit("www.ups.com")
obj.back(3)