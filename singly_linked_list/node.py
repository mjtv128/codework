class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        cur_node = self.head 
        while cur_node:
            print('a', cur_node.data)
            cur_node = cur_node.next

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return 
        last_node = self.head 
        while last_node.next:
            last_node = last_node.next 
        last_node.next = new_node
    
    def prepend(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node
    
    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print('Previous node does not exist')
            return 
        new_node = Node(data)

        new_node.next = prev_node.next
        prev_node.next = new_node
    
    def delete_node(self, key):
        cur_node = self.head 

        if cur_node and cur_node.data == key:
            self.head = cur_node.next
            cur_node = None
            return 
        
        prev = None
        while cur_node and cur_node.data != key:
            prev = cur_node
            cur_node = cur_node.next    

        if cur_node is None:
            return 
        
        prev.next = cur_node.next   
        cur_node = None
    
    def delete_node_at_pos(self, pos):
        if self.head:
            cur_node = self.head
            if pos == 0:
                self.head = cur_node.next
                cur_node = None
                return 

        prev = None 
        count = 0 

        while cur_node and count != pos:
            prev = cur_node 
            cur_node = cur_node.next 
            count += 1 
        
        if cur_node is None:
            return 
        
        prev.next = cur_node.next 
        cur_node = None
    
    def len_iterative(self):
        count = 0 
        cur_node = self.head 
        while cur_node:
            cur_node = cur_node.next 
            count += 1
        return count
    
    def len_recursive(self, node):
        if node is None:
            return 0 
        return 1 + self.len_recursive(node.next)

    def swap_nodes(self, key1, key2):
        if key1 == key2:
            return 

        prev_1 = None
        curr_1 = self.head 
        while curr_1 and curr_1.data != key1:
            prev_1 = curr_1 
            curr_1 = curr_1.next 
        
        prev_2 = None 
        curr_2 = self.head 
        while curr_2 and curr_2.data != key2:
            prev_2 = curr_2
            curr_2 = curr_2.next 
        
        if not curr_1 or not curr_2:
            return 

        if prev_1:
            prev_1.next = curr_2 
        else:
            self.head = curr_2 
        
        if prev_2:
            prev_2.next = curr_1
        else:
            self.head = curr_1 
        
        curr_1.next, curr_2.next = curr_2.next, curr_1.next

    def reverse_iterative(self):
        prev = None 
        cur = self.head 
        while cur:                                      
            nxt = cur.next 
            cur.next = prev  #pointer changes to the previous one
            prev = cur 
            cur = nxt
        self.head = prev

    def reverse_recursive(self):

        def _reverse_recursive(cur, prev):
            if not cur:
                return prev 
            
            nxt = cur.next 
            cur.next = prev 
            prev = cur
            cur = nxt
            return _reverse_recursive(cur, prev)
        
        self.head = _reverse_recursive(cur=self.head, prev=None)

    def merge_sorted(self, llist):
        p = self.head 
        q = llist.head 
        s = None

        if not p: 
            return q 
        if not q :
            return p

        if p and q: 
            if p.data  <= q.data:
                s = p
                p = s.next 
            else: 
                s = q 
                q = s.next 
            new_head = s
    
            while p and q:
                if p.data  <= q.data:
                    s.next = p 
                    s = p 
                    p = s.next 
                else:
                    s.next = q 
                    s = q 
                    q = s.next 
        if not p:
            s.next = q
        if not q:
            s.next = p 
        
        self.head = new_head
        return self.head
    
    def remove_duplicates(self):
        current = self.head 
        prev = None 
        dup_values = dict()

        while current:
            if current.data in dup_values:
                prev.next = current.next 
                current = None 
            else:
                dup_values[current.data] = 1
                prev = current 
            current = prev.next 
    
    def print_nth_from_last1(self, n):
        total_len = self.len_iterative()

        current = self.head 
        while current: 
            if total_len == n:
                print(current.data)
                return current.data 
            total_len -= 1
            current = current.next 
        
        if current is None: 
            return

    def print_nth_from_last2(self, n): #using pointers
        p = self.head 
        q = self.head

        if n > 0:
            count = 0 
            while q:
                count += 1
                if (count >= n):
                    break 
                q = q.next 
            
            if not q:
                print(str(n) + ' is greater than the number of nodes in the list')
                return 
            
            while p and q.next:
                p = p.next 
                q = q.next
            return p.data 

        else:
            return None
    
    def count_occurences_iterative(self,data):
        count = 0 
        current = self.head 

        while current:
            if current.data == data:
                count += 1
            current = current.next 
        
        return count
    
    def count_occurences_recursive(self, node, data):
        if not node:
            return 0 
        if node.data == data:
            return 1 + self.count_occurences_recursive(node.next, data)
        else:
            return self.count_occurences_recursive(node.next, data)

    def rotate(self, k):
        if self.head and self.head.next:
            p = self.head 
            q = self.head
            prev = None
            count = 0 

            while p and count < k:
                prev = p 
                p = p.next 
                q = q.next 
                count += 1
            p = prev 
            
            while q:
                prev = q
                q = q.next 
            q = prev 

            q.next = self.head 
            self.head = p.next
            p.next = None

# llist = LinkedList()
# llist.append("A")
# llist.append("B")
# llist.append("C")
# llist.prepend("D")
# print(llist.len_i/terative())
# llist.insert_after_node(llist.head.next, "D")
# llist.delete_node_at_pos(2)
# print(llist.len_recursive(llist.head))
# llist.reverse_iterative()
# llist.reverse_recursive()
# llist.swap_nodes("A", "B")
# llist.print_list() 

#MERGE
# llist_1 = LinkedList()
# llist_2 = LinkedList()

# llist_1.append(1)
# llist_1.append(5)
# llist_1.append(7)
# llist_1.append(9)
# llist_1.append(10)

# llist_2.append(2)
# llist_2.append(3)
# llist_2.append(4)
# llist_2.append(6)
# llist_2.append(8)

# llist_1.merge_sorted(llist_2)
# llist_1.print_list()

#Duplicate
# llist = LinkedList()
# llist.append(1)
# llist.append(6)
# llist.append(1)
# llist.append(4)
# llist.append(2)
# llist.append(2)
# llist.append(4)

# print("Original Linked List")
# llist.print_list()
# print("Linked List After Removing Duplicates")
# llist.remove_duplicates()
# llist.print_list()

# n-th to last
# llist = LinkedList()
# llist.append("A")
# llist.append("B")
# llist.append("C")
# llist.append("D")

# print('===A===',llist.print_nth_from_last1(2))
# print('====B===',llist.print_nth_from_last2(2))

#COUNT
# llist_2 = LinkedList()
# llist_2.append(1)
# llist_2.append(2)
# llist_2.append(1)
# llist_2.append(3)
# llist_2.append(4)
# llist_2.append(4)
# llist_2.append(1)
# print(llist_2.count_occurences_iterative(4))
# print(llist_2.count_occurences_recursive(llist_2.head, 4))

#ROTATE
llist = LinkedList()
llist.append(1)
llist.append(2)
llist.append(3)
llist.append(4)
llist.append(5)
llist.append(6)

llist.rotate(4)
llist.print_list()