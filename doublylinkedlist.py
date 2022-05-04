class Box:
    def __init__ (self,cat = None):
        self.cat = cat
        self.nextcat = None
        self.prevcat = None


class LinkedList:
    def __init__(self):
        self.head = None

    def contains (self, cat): # Содержится ли элемент в списке
        lastbox = self.head
        while (lastbox):
            if cat == lastbox.cat:
                return True
            else:
                lastbox = lastbox.nextcat
        return False

    def addToEnd(self, newcat): # Добавить элемент в конец списка
        newbox = Box(newcat)
        if self.head is None:
            self.head = newbox
            return
        lastbox = self.head
        while (lastbox.nextcat):
            lastbox = lastbox.nextcat
        lastbox.nextcat = newbox

    def get(self, catIndex): # получени элемента по индексу
        lastbox = self.head
        boxIndex = 0
        while boxIndex <= catIndex:
            if boxIndex == catIndex:
                return lastbox.cat
            boxIndex = boxIndex + 1
            lastbox = lastbox.nextcat

    def push(self, NewVal):
        NewNode = Box(NewVal)
        NewNode.nextcat = self.head
        if self.head is not None:
            self.head.prevcat = NewNode
        self.head = NewNode

    def removeBox(self, rmcat): # удалить узел
        headcat = self.head

        if headcat is not None:
            if headcat.cat == rmcat:
                self.head = headcat.nextcat
                headcat = None
                return
        while headcat is not None:
            if headcat.cat == rmcat:
                break
            lastcat = headcat
            headcat = headcat.nextcat
        if headcat == None:
            return
        lastcat.nextcat = headcat.nextcat
        headcat = None

    def listprint(self, node):
        while (node is not None):
            print(node.cat),
            last = node
            node = node.nextcat

    def insert(self, prev_node, NewVal):
        if prev_node is None:
            return
        NewNode = Box(NewVal)
        NewNode.nextcat = prev_node.nextcat
        prev_node.nextcat = NewNode
        NewNode.prevcat = prev_node
        if NewNode.nextcat is not None:
            NewNode.nextcat.prevcat = NewNode


a = LinkedList()
a.push(10)
a.push(20)
a.push(50)
a.insert(a.head.nextcat, 100)
a.listprint(a.head)
