class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class ListaDuplamenteEncadeada:
    def __init__(self):
        self.head = None
        self.tail = None

    def inserir_inicio(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def inserir_depois_de(self, elemento, data):
        new_node = Node(data)
        current = self.head
        while current:
            if current.data == elemento:
                if current.next is None:
                    self.inserir_final(data)
                else:
                    new_node.next = current.next
                    new_node.prev = current
                    current.next.prev = new_node
                    current.next = new_node
                return
            current = current.next
        print("Elemento não encontrado na lista.")

    def inserir_final(self, data):
        new_node = Node(data)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def remover_inicio(self):
        if self.head is None:
            print("A lista está vazia.")
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None

    def remover_apos_elemento(self, elemento):
        current = self.head
        while current:
            if current.data == elemento:
                if current.next is None:
                    print("Não é possível remover após o último elemento.")
                    return
                if current.next == self.tail:
                    self.tail = current
                current.next = current.next.next
                if current.next:
                    current.next.prev = current
                return
            current = current.next
        print("Elemento não encontrado na lista.")

    def remover_final(self):
        if self.tail is None:
            print("A lista está vazia.")
            return
        if self.tail == self.head:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

    def localizar(self, data):
        current = self.head
        index = 0
        while current:
            if current.data == data:
                return index
            index += 1
            current = current.next
        return -1

    def imprimir_lista(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
