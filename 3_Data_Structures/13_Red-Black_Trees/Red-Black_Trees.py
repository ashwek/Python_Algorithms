"""
A red–black tree is a kind of self-balancing binary search tree in computer science.
Each node of the binary tree has an extra bit, and that bit is often interpreted as
the color (red or black) of the node. These color bits are used to ensure the tree
remains approximately balanced during insertions and deletions.

https://en.wikipedia.org/wiki/Red%E2%80%93black_tree

https://www.cs.usfca.edu/~galles/visualization/RedBlack.html
"""

from random import randint

class Node:

    def __init__(self, parent = None, value = None, left = None, right = None, colour = "R"):
        self.parent = parent
        self.value = value
        self.left = left
        self.right = right
        self.colour = colour

    def __str__(self):
        return str(self.value) + ", " + self.colour

class RBT:

    __nill = Node(colour = "B")    # NULL Node

    def __init__(self):
        self.__root = None

    def insert_fix_up(self, current):
        while( current.colour == "R" and current.parent.colour == "R" ):
            cur_parent = current.parent
            if( cur_parent.parent.left == cur_parent ):
                if( cur_parent.parent.right.colour == "R" ):
                    cur_parent.colour = cur_parent.parent.right.colour = "B"
                    cur_parent.parent.colour = "R"
                    current = cur_parent.parent
                else:
                    if( cur_parent.right == current ):
                        self.left_rotate(cur_parent)
                        current, cur_parent = cur_parent, current
                    cur_parent.colour = "B"
                    cur_parent.parent.colour = "R"
                    self.right_rotate(cur_parent.parent)
            else:
                if( cur_parent.parent.left.colour == "R" ):
                    cur_parent.colour = cur_parent.parent.left.colour = "B"
                    cur_parent.parent.colour = "R"
                    current = cur_parent.parent
                else:
                    if( cur_parent.left == current ):
                        self.right_rotate(cur_parent)
                        current, cur_parent = cur_parent, current
                    cur_parent.colour = "B"
                    cur_parent.parent.colour = "R"
                    self.left_rotate(cur_parent.parent)

            self.__root.colour = "B"

    def insert(self, value):
        if( self.__root == None ): self.__root = Node(RBT.__nill, value, RBT.__nill, RBT.__nill, "B")
        else:
            temp_parent = temp = self.__root
            while temp != RBT.__nill:
                temp_parent = temp
                temp = temp.left if( value <= temp.value ) else temp.right

            new_node = Node(temp_parent, value, RBT.__nill, RBT.__nill)
            if( value <= temp_parent.value ): temp_parent.left = new_node
            else: temp_parent.right = new_node

            self.insert_fix_up(new_node)

    def left_rotate(self, current):

        change = current.right
        if( change != RBT.__nill ):
            change.parent = current.parent
            if( current.parent == RBT.__nill ): self.__root = change
            elif( current.parent.left == current ): current.parent.left = change
            else: current.parent.right = change

            current.parent = change
            current.right = change.left
            if( current.right != RBT.__nill ): current.right.parent = current
            change.left = current

    def right_rotate(self, current):

        change = current.left
        if( change != RBT.__nill ):
            change.parent = current.parent
            if( current.parent == RBT.__nill ): self.__root = change
            elif( current.parent.left == current ): current.parent.left = change
            else: current.parent.right = change

            current.parent = change
            current.left = change.right
            if( current.left != RBT.__nill ): current.left.parent = current
            change.right = current

    def level_order(self, current = []):

        if( self.__root == None ): return []

        Ret = []
        nxt_lvl = []

        if( not isinstance(current, list) ): current = [current]
        elif( len(current) == 0 ): current = [self.__root]

        for each in current:
            Ret.append((each.value, each.colour))
            if( each.left != RBT.__nill ): nxt_lvl.append(each.left)
            if( each.right != RBT.__nill ): nxt_lvl.append(each.right)

        if( nxt_lvl ):
            Ret.extend( self.level_order(nxt_lvl) )

        return Ret

    def in_order(self, current = None):

        if( self.__root == None ): return []

        if( current == None ): current = self.__root

        Ret = []
        if( current.left != RBT.__nill ): Ret.extend(self.in_order(current.left))
        Ret.append((current.value, current.colour))
        if( current.right != RBT.__nill ): Ret.extend(self.in_order(current.right))

        return Ret

    def pre_order(self, current = None):

        if( self.__root == None ): return []

        if( current == None ): current = self.__root

        Ret = [(current.value, current.colour)]
        if( current.left != RBT.__nill ): Ret.extend(self.pre_order(current.left))
        if( current.right != RBT.__nill ): Ret.extend(self.pre_order(current.right))

        return Ret

    def post_order(self, current = None):

        if( self.__root == None ): return []

        if( current == None ): current = self.__root

        Ret = []
        if( current.left != RBT.__nill ): Ret.extend(self.post_order(current.left))
        if( current.right != RBT.__nill ): Ret.extend(self.post_order(current.right))
        Ret.append((current.value, current.colour))

        return Ret

    def search(self, value):

        if( self.__root == None ): return None

        temp = self.__root
        while( temp != RBT.__nill ):
            if( temp.value == value ): return temp
            elif( value < temp.value ): temp = temp.left
            elif( value > temp.value ): temp = temp.right
        return None

if __name__ == "__main__":
    A = RBT()

    for i in range(10):
        Temp = randint(0,100)
        A.insert(Temp)

    print(A.level_order())
    print(A.in_order())
    print(A.pre_order())
    print(A.post_order())
