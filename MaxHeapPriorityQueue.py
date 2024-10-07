"""
Program: Project 2 - Max-Heap Priority Queue
Author: Claire Louviere
Date: 2/11/22
Description: Implement a max-heap priority queue using a list.
Notes:
    Late submission- school has been unbelievably busy as I'm sure you understand
    Everything should work as described
CIS 313 Project 2
Priority Queues
"""


class QueueCapacityTypeError(Exception):
    """
    A type error was made while trying to build a queue.
    """
    pass


class QueueCapacityBoundError(Exception):
    """
    A type error was made while trying to build a queue.
    """
    pass


class QueueIsFull(Exception):
    """
    An exception was made while the queue was empty
    """
    pass


class QueueIsEmpty(Exception):
    """
    An exception was made while the Queue was empty
    """
    pass


class StackCapacityTypeError(Exception):
    """
    Stack capacity of wrong type
    """
    pass


class StackCapacityBoundError(Exception):
    """
    Stack capacity is not a positive integer
    """
    pass


class StackIsFull(Exception):
    """
    An exception was made while the Stack was full
    """
    pass


class StackIsEmpty(Exception):
    """
    An exception was made while the stack was empty
    """
    pass


class Node:
    """
    Description: The Node class. Nodes contain data and a 'next' pointer.
                Nodes can be implemented with Stacks, Queues, and other data structures
    """

    def __init__(self, data=None):
        """
        Description: Constructor for the Node class. Any input valid, data parameter defaults to None
                if no data is specified. Instance variables include a data variable for the node and a
                pointer to the next node.
        Usage:
            myNode = Node(data)
        """
        self.data = data
        self.next = None


class Queue:
    """
    Description: The Queue class. Queues follow a first-in, first-out discipline.
                Implemented using a linked list of nodes. Queues have a head pointer, tail pointer,
                capacity (provided by the user in the constructor call), and currentSize.
    Methods include enqueue, dequeue, front, isEmpty, and isFull.

    """

    def __init__(self, capacity):
        """
        Description: The constructor for the Queue class.
        Parameters:
            capacity: The maximum number of elements that can be stored in the Queue before it overflows.
                    Must be a positive integer, or an Exception is raised.
        Usage: myQueue = Queue(capacity)
        """
        if type(capacity) != int:
            raise QueueCapacityTypeError("ERROR: Queue capacity must be an int.")
        elif capacity < 0 or capacity == 0:
            raise QueueCapacityBoundError("ERROR: Queue capacity must be a positive integer.")

        self.capacity = capacity
        self.head = Node()
        self.tail = Node()
        self.currentSize = 0

    def enqueue(self, item):
        """
        Description: creates a new Node and sets said Node's data variable to item. Then, insert this new
            Node into the Queue at the tail. Raises Exception if called when the queue is full.
        Parameters:
            item: the data to be enqueued. Any type is valid.
        Returns: returns a boolean true/false value based on status of the addition of the new Node
        Usage:
            myQueue.enqueue(item)
        """
        returnValue = False

        if self.isFull():
            raise QueueIsFull("enqueue FAILED: Queue is full")
        else:
            new_node = Node(item)

            if self.isEmpty():
                self.head = new_node
                self.tail = self.head
            else:
                old_tail = self.tail
                self.tail = new_node
                old_tail.next = self.tail
            self.currentSize += 1
            returnValue = True
        return returnValue

    def dequeue(self):
        """
        Description: Removes the node at the head of the Queue and returns it to the user. Takes no parameters.
            Raises exception if called on an empty Queue.
        Returns: returns the data variable of the node at the head of the queue (i.e., the node that has been in
            the queue for the longest).
            If dequeue() fails to remove a node from the head of the queue, return false.
        Usage:
            myQueue.dequeue()
        """
        if self.isEmpty():
            raise QueueIsEmpty("dequeue error: queue is empty")
        else:
            returnValue = self.head.data

            if self.currentSize > 1:
                temp = self.head
                self.head = temp.next
                temp = None
                self.currentSize -= 1
            else:
                self.head = Node()
                self.tail = self.head
                self.currentSize -= 1

            return returnValue

    def front(self):
        """
        Description: Return the node at the head of the queue, i.e., the node that has been in the queue
            for the longest. Does NOT remove the head node from the queue. No parameters.
        Returns: returns the node at the head of the queue. If the queue is empty, returns false.
        Usage:
            head = myQueue.front()
        """
        if self.currentSize > 0:
            first = self.head.data
            return first
        else:
            returnValue = False
            return returnValue

    def isEmpty(self):
        """
        Description: Assess whether or not the queue is empty. No parameters.
        Returns: a boolean true/false value depending on whether the currentSize variable is 0.
        Usage:
            status = myQueue.isEmpty()
        """
        return self.currentSize == 0

    def isFull(self):
        """
        Description: Assess whether or not the queue is full. No parameters.
        Returns: a boolean true/false value depending on whether the currentSize variable is equal to the
            capacity variable. The capacity variable is provided by the user in the constructor call.
        Usage:
            status = myQueue.isFull()
        """
        return self.currentSize == self.capacity


class Stack:
    """
    Description: The Stack class. Stacks follow a last-in, first-out (LIFO) discipline.
        Implemented using a linked list of nodes. Stacks have a head node pointer,
        capacity (provided by the user in the constructor call), and currentSize.
    Methods include push, pop, peek, isEmpty, and isFull
    """

    def __init__(self, capacity):
        """
        Description: The constructor for the Stack class.
        Parameters:
            capacity: The maximum number of elements that can be stored in the Stack before it overflows.
                    Must be a positive integer, or an exception is raised.
        Usage: myStack = Stack(capacity)
        """
        if type(capacity) != int:
            raise StackCapacityTypeError("ERROR: Stack capacity must be type int")
        if capacity <= 0:
            raise StackCapacityBoundError("ERROR: Stack Capacity must be a positive int")
        self.capacity = capacity
        self.head = Node()
        self.currentSize = 0

    def push(self, item):
        """
        Description: Creates a new node and sets the node's 'data' variable to item. Then, pushes/inserts this new
            node onto the top/head of the Stack. Raises Exception if called when the Stack is full.
        Parameters:
            item: the data to be pushed onto the Stack. Any type is valid.
        Returns: returns boolean true/false value based on status of the addition of the new node
        Usage:
            myStack.push(item)
        """
        returnValue = False

        if self.isFull():
            raise StackIsFull("ERROR: Stack is full")
        else:
            new_node = Node(item)

            if self.isEmpty():
                self.head = new_node
                self.currentSize += 1
                returnValue = True
            else:
                temp = self.head
                self.head = new_node
                self.head.next = temp
                self.currentSize += 1
                returnValue = True

        return returnValue

    def pop(self):
        """
        Description: removes the node at the head of the stack (i.e., the node that was added most recently)
            to maintain LIFO structure. Returns the removed node to the user. Takes no parameters. Raises
            exception if called on an empty Stack.
        Returns: returns the data variable of the node that was removed from the Stack. if the call fails to
            remove the node, return false.
        Usage:
            myStack.pop()
        """
        returnValue = False
        if self.isEmpty():
            raise StackIsEmpty("ERROR: Stack is Empty")
        else:
            returnValue = self.head.data
            if self.currentSize > 1:
                temp = self.head
                self.head = temp.next
                temp.next = None
                self.currentSize -= 1
            else:
                self.head = Node()
                self.currentSize -= 1
        return returnValue

    def peek(self):
        """
        Description: Allows the user to view the head item of the stack (i.e., the item that is next to be
            removed by a call to pop()). No parameters.
        Returns: returns the head node's data variable, if it exists. If the stack is empty and there is not
            a head node, return false.
        Usage:
            head = myStack.peek()
        """
        returnValue = False
        if not self.isEmpty():
            returnValue = self.head.data
        return returnValue

    def isEmpty(self):
        """
        Description: Assess whether or not the Stack is empty. No parameters.
        Returns: returns a boolean true/false based on whether the Stack's currentSize is 0.
        Usage:
            status = myStack.isEmpty()
        """
        return self.currentSize == 0

    def isFull(self):
        """
        Description: Assess whether or not the Stack is full. No parameters.
        Returns: returns a boolean true/false based on whether the Stack's currentSize variable is equal to
            the capacity variable provided by the user in the constructor call.
        Usage:
            status = myStack.isFull()
        """
        return self.capacity == self.currentSize


class PriorityQueue:
    """
    Description: the Priority Queue class.
            Priority queue is implemented as a max-heap priority queue.
    Methods include the constructor, the string method, insert, extractMax, peekMax,
    isEmpty, and isFull.
    """

    def __init__(self, capacity):
        """
        Description: The constructor for the PriorityQueue class.
        Parameters:
            capacity: The maximum number of elements that can be stored in the PriorityQueue before it
                    overflows. Must be a positive integer, or an Exception is raised.
        Usage:
            myPQ = PriorityQueue(capacity)
        """
        if type(capacity) != int:
            raise QueueCapacityTypeError("ERROR: PriorityQueue capacity must be an int.")
        elif capacity < 0 or capacity == 0:
            raise QueueCapacityBoundError("ERROR: PriorityQueue capacity must be a positive integer.")

        self._heap = []
        self.capacity = capacity
        self.currentSize = 0

    def __str__(self):
        """
        Description: returns the string representation of the heap. No input parameters.
            String representation takes the form of a list of tuples, (a, b) where
            'a' is the priority and 'b' is the item.
        Format: [(<prio1>, <item>), (<prio2>, item), ...
                if the queue is empty, return an empty list, []
        Usage:
            str(myPQ)
        """
        return str(self._heap)

    def getParent(self, index):
        """
        Description: input parameter index is an integer representing the index of a tuple in the list.
            returns the index of the input node's parent node.
        Usage:
            parent_index = myPQ.getParent(index)
        """
        assert type(index) == int
        if index == 0:
            parent_index = 0
        else:
            assert index > 0
            if (index % 2) == 0:
                parent_index = (index - 2) // 2
            else:
                parent_index = (index - 1) // 2
        return parent_index

    def swap(self, p_node, c_node, p_index, c_index):
        """
        Description: Swaps parent and child node in the heap.
        Parameters:
            p_node: the parent node
            c_node: the child node,
            p_index the parent node's index
            c_index:the child node's index
        Usage:
            myPQ.swap(parent, child, p_index, c_index)
        """
        self._heap[c_index] = p_node
        self._heap[p_index] = c_node
        ctemp = self._heap[p_index]
        tpi = self.getParent(p_index)
        temp_parent = self._heap[tpi]
        if ctemp[0] > temp_parent[0]:
            self.increaseKey(c_node, temp_parent, p_index)

    def increaseKey(self, item, p_node, item_index):
        """
        Description: increase the key of an item to satisfy max-heap property-  A[PARENT[i] >= A[i]
        Parameters:
            item: is the node that is moving to a higher position, i.e., the node moving to a lower index.
            p_node: the item node's parent node.
            item_index: which is the item's index on the heap
        Usage:
            myPQ.increaseKey(new_node, p_node, new_node_index)
        """
        p_index = self.getParent(item_index)
        self.swap(p_node, item, p_index, item_index)

    def insert(self, item):
        """
        Description: insert a tuple, item, into the priority queue, based on its priority.
            Valid input is a tuple containing the following:
                priority: A positive integer in the bound (0, infinity]
                item: any python object
        Error Handling: raises exception if called on a full queue.
        Returns: true if the tuple is successfully added to the heap
                false if else.
        Usage:
            myPQ.insert(prio, item)
        """
        returnValue = False
        if type(item[0]) != int:
            return returnValue
        if not (item[0] > 0):
            return returnValue
        if self.isFull():
            raise QueueIsFull("insert FAILED: Queue is full")

        else:
            item_index = self.currentSize
            self._heap.append(item)
            parent_index = self.getParent(item_index)
            parent_node = self._heap[parent_index]
            if item[0] > parent_node[0]:
                self.increaseKey(item, parent_node, item_index)
            self.currentSize += 1
            returnValue = True
        return returnValue

    def left_child(self, index):
        """
        Description: returns the index of the left child of the given index.
        Parameters:
            index: the index of the parent node whose left child we are computing
        Usage:
            left_index = myPQ.left_child(parentindex)
        """
        left_index = 2 * index + 1
        return left_index

    def right_child(self, index):
        """
        Description: returns the index of the right child of the given index.
        Parameters:
            index: the index of the parent node whose right child we are computing
        Usage:
            right_index = myPQ.right_child(parentindex)
        """
        right_index = (2 * index) + 2
        return right_index

    def heapify(self, index):
        """
        Description: reorder the max-heap priority queue if necessary after extractMax is called.
            Compares the priorities of the index node and each of its children.
            If the index node is less than either of its children, exchange the index node with
            the larger of its two children. Then, reassess the status of the heap.
        Parameters:
            index: the index of the root node of the sub-heap we are verifying.
        Usage:
            myPQ.heapify(0)
        """
        retVal = False
        li = self.left_child(index)
        ri = self.right_child(index)
        if li <= (self.currentSize-1) and self._heap[li][0] > self._heap[index][0]:
            mi = li
        else:
            mi = index
        if ri <= (self.currentSize-1) and self._heap[ri][0] > self._heap[mi][0]:
            mi = ri
        if not mi == index:
            self.swap(self._heap[index], self._heap[mi], index, mi)
            self.heapify(mi)
        else:
            retVal = mi
            print(retVal)
            """
            self._heap.pop(mi)
            self.currentSize -= 1"""
        return retVal


    def extractMax(self):
        """
        Description: extract the root/max node from the priority queue and return it. If the priority queue
            is empty and extractMax() is called, return False.
        Usage:
            max_node = myPQ.extractMax()
        """
        returnValue = False
        if self.isEmpty():
            raise QueueIsEmpty("extractMax error: queue is empty")
        returnValue = self._heap[0]
        self._heap[0] = self._heap[self.currentSize-1]
        status = self.heapify(0)
        #======================== INSTRUCTOR COMMENTS =========================
        # Even if we dont heapify we still need to pop the node from the heap
        # and decrement the heaps size. This should occure outside of the if before calling heapify.
        #======================================================================
        if status:
            self._heap.pop(status)
            self.currentSize -= 1
        return returnValue

    def peekMax(self):
        """
        Description: returns the node in the priority queue with the maximum priority.
        Usage:
            pq_max = myPQ.peekMax()
        """
        #======================== INSTRUCTOR COMMENTS =========================
        # Needed to return False if the heap was empty.
        #======================================================================
        return self._heap[0]

    def isEmpty(self):
        """
        Description: Assess whether or not the queue is empty. No parameters.
        Returns: a boolean true/false value depending on whether the currentSize variable is 0.
        Usage:
            status = myPQ.isEmpty()
        """
        return self.currentSize == 0

    def isFull(self):
        """
        Description: Assess whether or not the queue is full. No parameters.
        Returns: a boolean true/false value depending on whether the currentSize variable is equal to the
            capacity variable. The capacity variable is provided by the user in the constructor call.
        Usage:
            status = myPQ.isFull()
        """
        return self.currentSize == self.capacity





#============================= Instructor Comments =============================
# Overall: Excellent Submission
# Correctness: 56/60 pts
# Completeness: 25/25 pts
# Elegence: 15/15 pts
# Total: 96/100 pts
# Grade: A
#
#======================== Unit Testing Results (Complex) =======================
# Section-01: Method Validation Tests (Correct/Complete)
# Test-01: Valid Constructor Implementation (Queue/Stack/Node) - PASS
# Test-02: Valid Insert Implementation - PASS
# Test-03: Valid extractMax Implementation - FAIL
#    ERROR: The node was not actually removed from the list when <PriorityQueue>.extractMax() called on PQ with 1 node.
#    Current heap: [(30, 'data')]
#    ERROR: <PriorityQueue>.currentSize should be 0 after <PriorityQueue>.extractMax() called on PQ with 1 node.
# Test-04: Valid peekMax() Implementation - FAIL
#    ERROR: <PriorityQueue>.peekMax() crashed on valid call when PQ is empty.
#        Exception: IndexError('list index out of range')
# Test-05: Valid isEmpty() Implementation - PASS
# Test-06: Valid isFull() Implementation - PASS
#
# Section-02: Proper Error Handeling Tests
# Error Test-01: Proper Constructor Error Handeling - PASS
# Error Test-02: Proper Insert Error Handeling - PASS
# Error Test-03: Proper ExtractMax Error Handeling - PASS
#
# Section-3 (Extra Credit): Sorted Array (heap_sort) - FAIL
#    ERROR: <PriorityQueue>.heapSort(self, array) not implemented.
#        Exception: AttributeError("'PriorityQueue' object has no attribute 'heapSort'")
#================================ End of Testing ===============================
#===============================================================================
