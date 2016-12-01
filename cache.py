class Node(object):
    def __init__(self,key=None,value=None):
        self.key = key
        self.value = value
        self.rightNeigh = None 
        self.leftNeigh = None
        
    def __str__(self):
        return "key: {}, value: {}".format(self.key,self.value)

class Cache(object):
    """
    Cache is implemented as a Doubly Linked list with
    size : size of cache
    head : pointing to first node
    tail : pointing to last node
    num_keys: number of (key,value) pairs stored in the cache
    """
    def __init__(self,size):
        self.size = size
        self.num_keys = 0
        self.head = None
        self.tail = None
        
    
    def loadKey(self,key):
        """
        Gets a value from the cache
        
        Args:
         key: string object
         
        Returns:
          None
          
        Prints:
          GOT 'value' if value in cache
          ERROR if key has spaces
          NOTFOUND if key not in the cache
        """
        # Searching will take O(cache_size) operations
        if key.find(" ") != -1:
            print "ERROR"
        else:
            try:
                curr = self.head
                found = False
                while curr != None:
                    if key == curr.key:
                        found = True
                        print "GOT {}".format(curr.value)
                        break
                    else:
                        curr = curr.rightNeigh
                if not found:
                    print "NOTFOUND"
            except:
                print "Error"
    
    
    def storeKey(self,key,value):
        """
        Adds a new (key,value) to the cache
        
        Args:
         key: string object
         value: string object
         
        Returns:
          None
          
        Prints:
          SET OK if value successfully added
          ERROR if failed to add value
        """
        # Adding a new key will be O(1) operation 
        
        if key.find(" ") != -1 or value.find(" ") != -1:
            print ("ERROR")
        else:
            try:
             

                # insert node at the end
                if self.head != None:
                    
                    # Search if key is already present
                    curr = self.head
                    found = False
                    while curr != None:
                        if key == curr.key:
                            found = True
                            curr.value = value
                            break
                        else:
                            curr = curr.rightNeigh
                     
                        
                    if not found:
                       if self.num_keys == self.size:  
                           self.removeLRU()  # cache is full
                       elif self.num_keys > self.size:
                           raise Error("Something wrong with setting values")
                        # If key not present add newNode
                        newNode = Node(key,value)
                        self.tail.rightNeigh = newNode
                        newNode.leftNeigh = self.tail
                        self.tail = newNode
                        self.num_keys += 1
                else:
                    self.head = Node(key,value)
                    self.tail = self.head
                    self.num_keys += 1
                
                print('SET OK')
            except:
                print "ERROR"
    
    
    def removeLRU(self):
        """Removes the least recently used (key,value) from
        the cache.
        """
        # It will be O(1) time complexity
        if self.head != None:
            self.head = self.head.rightNeigh
            self.head.leftNeigh = None
        self.num_keys -= 1
        if self.head == None:
            self.tail = self.head
            
        