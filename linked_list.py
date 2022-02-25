class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    """ implementing the Linked List"""
    def __init__(self):
        self.head=None

    def print(self):
        """printing the Linked List"""
        if self.head is None:
            print("Empty")
            return
        llstr = []
        itr = self.head
        while itr:
            llstr.append(str(itr.data))
            # print(llstr)
            itr = itr.next
        print(" --> ".join(llstr))


    def get_length(self):
        """prints the length of the Linked List"""
        count = 0
        itr = self.head
        while itr:
            itr = itr.next
            count+= 1
        return count



    def insert_values(self,data_list):
        """adding list a element to the end of Linked List"""
        for value in data_list:
            self.insert_at_end(value)

    def insert_at_begining(self, data):
        """adding a element to the bengining of Linked List"""
        node = Node(data, next=self.head)
        self.head = node
    def insert_at_end(self,data):
        """adding a element to the ending of Linked List"""
        if self.head == None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def insert_at_index(self,data,index):
        """instertig data at specfic index"""
        if index<0 or index >= self.get_length():
            raise Exception(f"invalid index")
        if index==0:
            self.head = Node(data,self.head)
            return
        count = 0
        itr= self.head

        while itr:
            if count == index-1:
                # print(f"removing {itr.next.data}")
                itr.next = Node(data,itr.next)
                break

            itr= itr.next
            count+=1


    def delete(self,data):
        """delete the first accurance of the given data """
        if self.head == None:
            raise Exception("list is empty")
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        itr = self.head
        while itr:
            if itr.next.data == data:
                itr.next=itr.next.next
                return
            itr = itr.next




    def remove_at_index(self,index):
        """remove element at specific index"""


        if index<0 or index >= self.get_length():
            raise Exception(f"invalid index")
        if index==0:
            self.head = self.head.next
            return
        count = 0
        itr= self.head

        while itr:
            if count == index-1:
                print(f"removing {itr.next.data}")
                itr.next = itr.next.next
                break

            itr= itr.next
            count+=1








if __name__ == '__main__':
    linkList = LinkedList()
    print("insert elements 0,1,2,3,4,5,6,7")
    linkList.insert_values([0,1,2,3,4,5,6,7])
    linkList.print()
    print("length of the linked list")
    print(f"the length of the Linked list is {linkList.get_length()}")
    print("insert 'mat' at index 7")
    linkList.insert_at_index("mat",7)
    linkList.print()
    print("length of the linked list")
    print(f"the length of the Linked list is {linkList.get_length()}")
    print("delete element 'mat'")
    linkList.delete("mat")
    linkList.print()
