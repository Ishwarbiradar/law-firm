class TREE:
    def search_ele(self,val):
        if val>self.data:
            if self.prev is None:
                print(val,'Not Found')
            else:
                self.prev.search_ele(val)
        elif val>self.data:
            if self.next is None:
                print()