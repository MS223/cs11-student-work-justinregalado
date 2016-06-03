class kangaroo(object):
    def __init__(self,pouch_content):
        self.pouch_content = []
        # pouch_content = []
        # return str(self.pouch_content)
    #     i cant put a return init
    def __add__(self,other):
        self.pouch_content.append (other)
        return self.pouch_content


justin = kangaroo("...")
justin.__add__("banana")
justin.__add__("baby")
justin.__add__("angie")
print justin.pouch_content
