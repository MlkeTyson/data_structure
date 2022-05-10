from collections import deque

class Stack:
    
    def __init__(self):
        self.head = deque()
        
    def append_el(self, el):
        self.head.append(el)
    
    def pop_el(self):
        self.head.pop()
        
    def peek(self):
        print(self.head[-1])
    
    def print_stack(self):
        self.head.reverse()
        for i in self.head:
            print(i)


st = Stack()
st.append_el(1)
st.append_el(2)
st.append_el(3)
st.append_el(20)
st.pop_el()
st.peek()