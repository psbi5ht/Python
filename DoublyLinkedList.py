class Node:
    """Represents a single node in a doubly linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None  # Points to the next node
        self.prev = None  # Points to the previous node


class DoublyLinkedList:
    """Manages the doubly linked list structure."""
    def __init__(self):
        self.head = None

    def append(self, data):
        """Adds a new node to the end of the list."""
        new_node = Node(data)
        
        # Case 1: If the list is empty, make the new node the head
        if not self.head:
            self.head = new_node
            return
            
        # Case 2: Traverse to the last node
        current = self.head
        while current.next:
            current = current.next
            
        # Link the last node and the new node together
        current.next = new_node
        new_node.prev = current  # The new node points back to the old tail

    def display_forward(self):
        """Prints the entire list from head to tail."""
        current = self.head
        if not current:
            print("The list is empty.")
            return

        print("Forward:  ", end="")
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

    def display_backward(self):
        """Prints the entire list from tail to head using prev pointers."""
        current = self.head
        if not current:
            print("The list is empty.")
            return

        # 1. First, navigate to the very last node (the tail)
        while current.next:
            current = current.next

        # 2. Walk backward using the 'prev' pointers
        print("Backward: ", end="")
        while current:
            print(current.data, end=" <-> ")
            current = current.prev
        print("None")


# --- Main User Interaction Logic ---
if __name__ == "__main__":
    dllist = DoublyLinkedList()
    print("--- Build Your Doubly Linked List ---")
    print("Enter integers to add to the list. Type 'stop' to finish.\n")

    while True:
        user_input = input("Enter a number (or 'stop'): ").strip()
        
        if user_input.lower() == 'stop':
            break
            
        try:
            number = int(user_input)
            dllist.append(number)
        except ValueError:
            print("Invalid input. Please enter a valid integer or 'stop'.")

    # Display the final structured list in both directions
    print("\nYour final Doubly Linked List:")
    dllist.display_forward()
    dllist.display_backward()
