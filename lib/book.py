#!/usr/bin/env python3


# class Book:
#     def __init__(self, title='', page_count=''):
#         self.title = title
#         self.page_count = page_count

#     @property
#     def page_counter(self):
#         return self._page_count

#     @page_counter.setter
#     def page_counter(self, value):
#         if  isinstance(value, int):
#             self._page_count = value
#         else:
#             print("page_count must be an integer")

class Book:
    def __init__(self, title='', page_count=0):
        self.title = title
        self._page_count = page_count
        # self.current_page = 0

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        if not isinstance(value, int):
            print('page_count must be an integer')
            return
        self._page_count = value

    def turn_page(self):
        print('Flipping the page...wow, you read fast!')    